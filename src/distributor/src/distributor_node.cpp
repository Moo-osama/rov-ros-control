#include <iostream> 
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float64.h"
#include "std_msgs/Bool.h"
#include <sensor_msgs/Joy.h>
#include <stdio.h>
#include <string.h> 
#include <cstring> 
#include <sstream>
#include <stdlib.h>  
#include "distributor/rov_msgs.h" 
#include <sstream>
#include <cmath>

using namespace std;
string stabilize_lf_str = "v0.5"; 
distributor::rov_msgs feedMsg;
std::stringstream ss;
std_msgs::String x; 
float yaw_raw_setpoint, pitch_raw_setpoint, lf_raw_val;   
std_msgs::Float64 yaw_pid_state, pitch_pid_state, lf_stabilize_pid_state;
std_msgs::Bool enable_var;
float yaw_actual_setpoint = 0, pitch_actual_setpoint = 0;
std_msgs::Float64 yaw_pid_direction, pitch_pid_direction, lf_stabilize_pid_setpoint, depth_actual_setpoint;

int pid_prev, pid_current, prev_enable_var = 0;

float previous = 2.0;
float current = 2.0;
float yaw_difference = 0.0, pitch_difference = 0.0;

string activate = "stop";

bool yaw_setpoint_flag = true, pitch_setpoint_flag = true, depth_setpoint_flag = true, 
activate_flag = true, changing_in_depth = false, changing_in_pitch = false;

 ros::Subscriber sub; 
 ros::Subscriber stabilize_lf_sub; 
 ros::Subscriber joy_sub;
 ros::Subscriber activate_linefollower_sub;
 ros::Publisher chatter_pub; 

 ros::Publisher enable_pub;
 ros::Publisher yaw_state_pub; 
 ros::Publisher yaw_setpoint_pub;

 ros::Publisher pitch_state_pub; 
 ros::Publisher pitch_setpoint_pub;

 ros::Publisher lf_stabilize_setpoint_pub; 
 ros::Publisher lf_stabilize_state_pub;

//parsing functions prototype 

void ParseString(string inp, distributor::rov_msgs &feedMsg, string stabilize_lf_str);
void get_yaw_actual_setpoint();
void get_pitch_actual_setpoint();
void get_depth_actual_setpoint();
void get_yaw_pid_direction(float state);
void get_pitch_pid_direction(float state);
std_msgs::Float64 get_pid_state(float current_state, float setpoint);



void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  if (!prev_enable_var && joy -> buttons[1])
    {
      enable_var.data = enable_var.data? 0:1; 
      pid_current = enable_var.data? 1:0;
    }


  if (joy -> buttons[2] || joy -> buttons[4])
    changing_in_depth = true;
  else
    changing_in_depth = false;

  if (joy->axes[5] != 0)
    changing_in_pitch = true;
  else
    changing_in_pitch = false;


  prev_enable_var = joy -> buttons[1];
  previous = joy->axes[2]; 
}

void sensors_msg_Callback(const std_msgs::String::ConstPtr& msg)
{
  // ROS_INFO("I'm in chatter callback");
  ParseString(msg->data, feedMsg, stabilize_lf_str);  
  chatter_pub.publish(feedMsg);
}

void stabilize_lf_Callback(const std_msgs::String::ConstPtr& msg)
{
  stabilize_lf_str = msg -> data;
}

void activateCallback(const std_msgs::String::ConstPtr& msg)
{
  activate = msg -> data;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "parsing_node");
  ros::NodeHandle n;

  ROS_INFO("I'm in main");

  sub = n.subscribe<std_msgs::String>("read", 1000, &sensors_msg_Callback);
  stabilize_lf_sub = n.subscribe<std_msgs::String>("stabilize_lf", 1000, &stabilize_lf_Callback);
  joy_sub = n.subscribe<sensor_msgs::Joy>("joy", 1000, &joyCallback);
  activate_linefollower_sub = n.subscribe<std_msgs::String>("line_follower_flag", 1000, &activateCallback);

  chatter_pub = n.advertise<distributor::rov_msgs>("sensors_response_topic", 1000);

  enable_pub = n.advertise<std_msgs::Bool>("pid_enable", 1000); 
  
  yaw_setpoint_pub = n.advertise<std_msgs::Float64>("yaw_setpoint", 1); 
  yaw_state_pub = n.advertise<std_msgs::Float64>("yaw_state", 1000);

  pitch_setpoint_pub = n.advertise<std_msgs::Float64>("pitch_setpoint", 1); 
  pitch_state_pub = n.advertise<std_msgs::Float64>("pitch_state", 1000);

  lf_stabilize_setpoint_pub = n.advertise<std_msgs::Float64>("depth_setpoint", 1); 
  lf_stabilize_state_pub = n.advertise<std_msgs::Float64>("depth_state", 1000);

  ros::spin();
}

void ParseString(string inp, distributor::rov_msgs &feedMsg, string stabilize_lf_str) 
{

  feedMsg.yaw = atof(inp.substr(inp.find('A') + 1, inp.find('B')).c_str());   //pitch
  feedMsg.pitch = atof(inp.substr(inp.find('B') + 1, inp.find('C')).c_str());    //roll
  feedMsg.roll = atof(inp.substr(inp.find('C') + 1, inp.find('D')).c_str());     //yaw
  feedMsg.acc_x = atof(inp.substr(inp.find('D') + 1, inp.find('E')).c_str());   //acc_x
  feedMsg.acc_y = atof(inp.substr(inp.find('E') + 1, inp.find('F')).c_str());   //acc_y
  feedMsg.acc_z = atof(inp.substr(inp.find('F') + 1, inp.find('G')).c_str());   //acc_z
  feedMsg.gyro_x = atof(inp.substr(inp.find('G') + 1, inp.find('H')).c_str());  //gyro_x
  feedMsg.gyro_y = atof(inp.substr(inp.find('H') + 1, inp.find('I')).c_str());  //gyro_y
  feedMsg.gyro_z = atof(inp.substr(inp.find('I') + 1, inp.find('J')).c_str());  //gyro_z
  feedMsg.paro = atof(inp.substr(inp.find('J') + 1, inp.find('K')).c_str());    //paro
  feedMsg.mag1 = atof(inp.substr(inp.find('E') + 1, inp.find('F')).c_str());
  feedMsg.PH = atof(inp.substr(inp.find('D')+1, inp.find('E')).c_str());       //PH
  feedMsg.water = atof(inp.substr(inp.find('W')+1, inp.find('W')+2).c_str());    //water
  feedMsg.temp = atof(inp.substr(inp.find('C')+1, inp.find('D')).c_str());     //temperature

  yaw_raw_setpoint = feedMsg.yaw;
  pitch_raw_setpoint = feedMsg.pitch;
  lf_raw_val = atof(stabilize_lf_str.substr(1, stabilize_lf_str.length()).c_str());;
  lf_stabilize_pid_state.data = lf_raw_val;
  // determine actual setpoint
  if (activate == "start" && activate_flag)
  {
    yaw_actual_setpoint = yaw_raw_setpoint; 
    pitch_actual_setpoint = pitch_raw_setpoint;
    activate_flag = false;
  }
  if (activate == "stop")
  {
    activate_flag = true;
    get_yaw_actual_setpoint();
    get_pitch_actual_setpoint();
   // get_depth_actual_setpoint();
    pid_prev = pid_current;
  }
  if (activate == "start")
  {
    lf_stabilize_pid_setpoint.data = 0.5; 
    enable_var.data = true;
  }
  else 
  lf_stabilize_pid_setpoint.data = lf_raw_val; 
  

  // determine left-or-right direction
  get_yaw_pid_direction(feedMsg.yaw);
  get_pitch_pid_direction(feedMsg.pitch);

  // calulate pid_state
  
  yaw_pid_state = get_pid_state(feedMsg.yaw, yaw_actual_setpoint);
  pitch_pid_state = get_pid_state(feedMsg.pitch, pitch_actual_setpoint);


  if (previous != current && activate == "stop")
  {
    ROS_INFO_STREAM("joy change");
    yaw_pid_state.data = 0.0;
  }
  if (changing_in_pitch && activate == "stop")
  pitch_pid_state.data = 0.0;
  
  

  enable_pub.publish(enable_var);
  yaw_state_pub.publish(yaw_pid_state);
  yaw_setpoint_pub.publish (yaw_pid_direction);
  pitch_state_pub.publish(pitch_pid_state);
  pitch_setpoint_pub.publish (pitch_pid_direction);
  lf_stabilize_state_pub.publish(lf_stabilize_pid_state);
  lf_stabilize_setpoint_pub.publish (lf_stabilize_pid_setpoint);
}



void get_yaw_actual_setpoint()
{
  if(previous == current && yaw_setpoint_flag || (pid_prev == 0 && pid_current ==1)) 
    {yaw_actual_setpoint = yaw_raw_setpoint; yaw_setpoint_flag = false;}
    
  if (previous != current)
    {yaw_setpoint_flag = true; yaw_actual_setpoint = yaw_raw_setpoint;}
    current = previous;
}

void get_pitch_actual_setpoint()
{
  if (changing_in_pitch)
  {
    pitch_setpoint_flag = true; 
    pitch_actual_setpoint = pitch_raw_setpoint;
  }
  else if (pitch_setpoint_flag || (pid_prev == 0 && pid_current ==1))
  {
   pitch_actual_setpoint = pitch_raw_setpoint; 
   pitch_setpoint_flag = false; 
  }
}

void get_depth_actual_setpoint()
{
  if (changing_in_depth)
  {
    depth_setpoint_flag = true; 
    depth_actual_setpoint.data = lf_raw_val;
  }
  else if (depth_setpoint_flag)
  {
   depth_actual_setpoint.data = lf_raw_val; 
   depth_setpoint_flag = false; 
  }
}
/////////////end of parsing 

void get_yaw_pid_direction(float state)
{
   yaw_difference = abs(state - yaw_actual_setpoint);

  if ( (state >= yaw_actual_setpoint && yaw_difference < 180) || (state < yaw_actual_setpoint && yaw_difference >= 180) )
  // right
  {
    yaw_pid_direction.data = 2.0;
  }
  else if ( (state >= yaw_actual_setpoint && yaw_difference >= 180) || (state < yaw_actual_setpoint && yaw_difference < 180) )
  // left
  {
    yaw_pid_direction.data = 1.0;
  }
}

void get_pitch_pid_direction(float state)
{
   pitch_difference = abs(state - pitch_actual_setpoint);

  if ( (state >= pitch_actual_setpoint && pitch_difference >= 180) || (state < pitch_actual_setpoint && pitch_difference < 180) )
  // right
  {
    pitch_pid_direction.data = 2.0;
  }
  else if ( (state >= pitch_actual_setpoint && pitch_difference < 180) || (state < pitch_actual_setpoint && pitch_difference >= 180) )
  // left
  {
    pitch_pid_direction.data = 1.0;
  }
}

std_msgs::Float64 get_pid_state(float current_state, float setpoint)
{
  current_state = current_state - setpoint;
  std_msgs::Float64 pid_state;
  
  if (current_state < 0)
  current_state += 360;

  if (current_state > 180)
  pid_state.data = 360 - current_state;
  else
  pid_state.data = current_state;

  return pid_state;
}