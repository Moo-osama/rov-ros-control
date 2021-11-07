#include "ros/ros.h"
#include <sensor_msgs/Joy.h>
#include <sensor_msgs/JoyFeedbackArray.h>
#include "std_msgs/String.h"
#include <iostream>
#include <math.h>
#include "std_msgs/Float64.h"
#include <sstream>
#include <chrono>
#include <algorithm>

#define min(a,b) (a<b? (a):(b))

sensor_msgs::Joy msg;
std_msgs::String out;
ros::Publisher* pub;
int pid=0,f=0;
float x=0.0;

void chatterCallback(const sensor_msgs::Joy::ConstPtr& in)
{
  f=1;
	msg=*in;
}

void controlEffortCallback(const std_msgs::Float64::ConstPtr& in)
{
  x=in->data;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "motor");
  ros::NodeHandle n;
  ros:: Rate rate(100);

  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("comm_out", 1000);
  pub=&chatter_pub;

  ros::Subscriber sub = n.subscribe("joy", 1000, chatterCallback);
  ros::Subscriber controlEffort = n.subscribe("control_effort", 1000, controlEffortCallback);
  while(ros::ok()){

    ROS_INFO("%d", f);
    if(f){

      bool direction0, direction1;
      double value0, value1, h0, h1;
      direction0=1;
      direction1=1;
      h0=(msg.axes[1])*255.0;
      h1=(msg.axes[3])*255.0;
      value0=min(h0+h1/2,255);
      value1=min(h0-h1/2,255);
      if(value0<0||value0==-0)direction0=0,value0*=-1;
      if(value1<0||value1==-0)direction1=0,value1*=-1;




      int flags=0,pwm0=0,pwm1=0;
      flags|=(direction0? 1<<7:0);
      flags|=(direction1? 1<<6:0);
      flags|=1<<5;//(msg->buttons[11]? 1<<5:0);
      flags|=1<<4;//(msg->buttons[12]? 1<<4:0);
      flags|=(msg.buttons[4]? 1<<3:0);
      flags|=(msg.buttons[6]? 1<<2:0);
      flags|=(msg.buttons[5]? 1<<1:0);
      flags|=(msg.buttons[7]? 1<<0:0);
      pwm0=(int)value0;
      pwm1=(int)value1;

      char send[3];
      send[0]=flags;
      send[1]=pwm1;
      send[2]=pwm0;
      std::stringstream ss;
      ss<<flags<<" "<<pwm1<<" "<<pwm0;
      out.data=ss.str();
      ROS_INFO("%s", out.data);
      pub->publish(out);
  }
    ros::spinOnce();
    rate.sleep();
  }

  //ros::spin();
  return 0;
}
