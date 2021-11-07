#include <ros/ros.h>
#include <sensor_msgs/Joy.h>
#include <std_msgs/String.h>
#include "std_msgs/Float64.h"
#include <stdio.h>
#include <string.h>
#include <cstring>
#include <sstream>
#include <stdlib.h>
#include <string>


ros::Publisher vehicle_pub_;
ros::Subscriber joy_sub_;
void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
std_msgs::String pub_msg, prev_pub_msg;


void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
void ConcatenateString();

//Message to be published
int DirL, DirR, fwd =0, rot =0;
int PIDOn, PilotSP;

int main(int argc, char** argv)
{
    ros::init(argc, argv, "map_motors");  
    ros::NodeHandle nh_;  
    ROS_INFO_STREAM("Executing main");
    vehicle_pub_ = nh_.advertise<std_msgs::String>("motor_values", 1000); 
    joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 1000, &joyCallback);
    ros::spin();
  
    return 0;
}

void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
    fwd = 0;
    rot = 0;
    if(joy->axes[1] !=0) //Left Wheels
    {
        if(joy->axes[1] < 0)
        {   
            fwd = -255*joy->axes[1];
        }
        else
        {
            fwd = 255*joy->axes[1]; 
        }      
    }

    

    if(joy->axes[0] !=0) //Right Wheels
    {
        if(joy->axes[0] < 0)
        {   
            rot = -255*joy->axes[0];
        }
        else
        {
            rot = 255*joy->axes[0]; 
        }      
    }


    if (joy->axes[0] == 0 &&  joy->axes[1] == 0)
    {
        fwd = 0;
        rot = 0;
    }

    ConcatenateString();
    vehicle_pub_.publish(pub_msg);
}

void ConcatenateString()
{
    std::stringstream ss;
    ss << "A" << fwd << "B" << rot << "C";
    pub_msg.data = ss.str();

}