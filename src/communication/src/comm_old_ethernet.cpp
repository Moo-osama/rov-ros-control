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

/**

 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
// %Tag(CALLBACK)%
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
 
  
 
  // Send a message to the server.

  sendto(sock,msg->data.c_str(),strlen(msg->data.c_str()),0,(sockaddr *)&serverAddr,sin_size);
        //if(sendto(sock,"sth",3,0,(sockaddr *)&serverAddr,sin_size))ROS_INFO("testing");


  /*memset(buffer,0,1024);


  //ROS_INFO("I also heard: [%s]", buffer);
  
  recv(sock, buffer, 1024,0);

  ROS_INFO("ham naaaaw %s\n",buffer);*/
 
}
// %EndTag(CALLBACK)%

int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line.
   * For programmatic remappings you can use a different version of init() which takes
   * remappings directly, but for most command-line programs, passing argc and argv is
   * the easiest way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "comm");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  /**
   * The subscribe() call is how you tell ROS that you want to receive messages
   * on a given topic.  This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing.  Messages are passed to a callback function, here
   * called chatterCallback.  subscribe() returns a Subscriber object that you
   * must hold on to until you want to unsubscribe.  When all copies of the Subscriber
   * object go out of scope, this callback will automatically be unsubscribed from
   * this topic.
   *
   * The second parameter to the subscribe() function is the size of the message
   * queue.  If messages are arriving faster than they are being processed, this
   * is the number of messages that will be buffered up before beginning to throw
   * away the oldest ones.
   */
// %Tag(SUBSCRIBER)%
  ros::Subscriber sub = n.subscribe("comm_out", 1000, chatterCallback);



        if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1){ // Try to create a socket, print error message and exit if failed
 
 perror("Error Creating Socket");
 //ROS_INFO("testing");
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
 
// %EndTag(SUBSCRIBER)%

  /**
   * ros::spin() will enter a loop, pumping callbacks.  With this version, all
   * callbacks will be called from within this thread (the main one).  ros::spin()
   * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
   */

  //ROS_INFO("something");
// %Tag(SPIN)%
  //ros::spin();

  
  ros::Publisher in_pub = n.advertise<std_msgs::String>("in", 1000);

  while(ros::ok){
      memset(buffer,0,1024);


  //ROS_INFO("I also heard: [%s]", buffer);
  
  recv(sock, buffer, 1024,0);


  std_msgs::String msg;

  msg.data = buffer;

  ROS_INFO("ham naaaaw %s\n",buffer);
       
  in_pub.publish(msg);

      ros::spinOnce();
  }

  //ros::spin();
//close(sock);// Close Socket

// %EndTag(SPIN)%

  return 0;
}

