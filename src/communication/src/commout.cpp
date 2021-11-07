#include "ros/ros.h"
#include "std_msgs/String.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <errno.h>
#include <netdb.h>
#include <thread>
using namespace std;


int sock; // Socket handler
struct sockaddr_in serverAddr; // Server address
struct hostent *server = gethostbyname("192.168.0.101");  // convert the host name into a network host structure
socklen_t sin_size = sizeof(struct sockaddr_in); // get size of server address

struct timeval tv;
int recVal = 0;
int sockLen = sizeof(serverAddr);
bool timePassed = false;
time_t startListenTime = time(NULL);


void terminate_with_error (const char * error_msg,int sock) {
  printf ("%s\n",error_msg); // printing error
  perror("Socket Error:"); // printing system error
  if (sock != -1) // Close socket and exit is socket opened
  {
    close (sock);
    exit(1);
  }
}


char buffer[1024];


void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", (msg->data.c_str()));
  int flag,pwm1,pwm0;
  stringstream ss(msg->data);

  ss>>flag;
  ss>>pwm1;
  ss>>pwm0;

  char buffer[3];

  buffer[0]=flag;
  buffer[1]=(pwm1==255? pwm1:pwm1+1);
  buffer[2]=(pwm0==255? pwm0:pwm0+1);


  ROS_INFO("%u %u %u", (unsigned int)buffer[0],(unsigned int)buffer[1],(unsigned int)buffer[2]);

  sendto(sock,buffer,strlen(buffer),0,(sockaddr *)&serverAddr,sin_size);
}



int main(int argc, char **argv)
{
  ros::init(argc, argv, "CommOut");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("comm_out", 1, chatterCallback);
  ros::Publisher in_pub = n.advertise<std_msgs::String>("Sensors", 1000);
  ros:: Rate rate (30);

  if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1){ // Try to create a socket, print error message and exit if failed
	 perror("Error Creating Socket");
	 exit(1);	 
  } 
  memset((char *) &serverAddr, 0,sizeof(serverAddr));  // initialize the server address data structure
  serverAddr.sin_family = AF_INET; // Set up the communication family
  serverAddr.sin_port = htons(9999); //set the port of the server
  if ( server == NULL ) terminate_with_error("Server is not found!!",sock); // if failed terminate with an error message
  // copy Server address data into server address strcuture
  memcpy((char *)&serverAddr.sin_addr.s_addr,(char *)server->h_addr, server->h_length);
  memset(&(serverAddr.sin_zero), 0, 8);
  sendto(sock,"hello",strlen("hello"),0,(sockaddr *)&serverAddr,sin_size);

  while(ros::ok){

    fd_set rfds;
    FD_ZERO(&rfds);
    FD_SET(sock, &rfds);
    tv.tv_sec = 0.01;
    tv.tv_usec = 0.0;
    recVal = select(sock +1, &rfds, NULL, NULL, &tv);
    switch(recVal)
    {
        case(0):
        {
            ROS_INFO("timeout");
            break;
        }
        case(-1):
        {
            
            ROS_INFO("Fuck");
             break;
        }
        default:
        {
            memset(buffer,0,1024);
            recv(sock, buffer, 1024,0);


            //ROS_INFO("%s\n",buffer);
    		
            for(int i=0;i<4;i++){
    			buffer[i]&=((buffer[4]>>i)&1)<<7;
			}

			int encoderValue=0;
			for(int i=3;i>=0;i--){
				encoderValue<<=8;
				encoderValue|=buffer[i];
			}

			std::stringstream ss;
			ss<<"("<<encoderValue<<", "<<((buffer[4]>>6)&1)<<", "<<((buffer[4]>>5)&1)<<", "<<((buffer[4]>>4)&1)<<")";//(encoder, IR, metal, switch)

		    std_msgs::String m;
            m.data = ss.str();
            ROS_INFO("ham naaaaw %s\n",ss.str().c_str());
            in_pub.publish(m);
            break;
        }
    }

      ros::spinOnce();
      rate.sleep();
  }
  return 0;
}