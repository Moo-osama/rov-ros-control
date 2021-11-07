#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time
file_object = open(r"sample_1.txt","w+")

prev_time = time.time()

def callback(data):
     global prev_time
     curr_time = time.time()
     rospy.loginfo("Motor_values_are %s", data.data)
     motor_sample = str(data.data)
     time_elapsed = str(curr_time - prev_time)
     prev_time = curr_time
     file_object.write(time_elapsed)
     file_object.write('\n')
     file_object.write(motor_sample)
     file_object.write('\n')

     
def listener():
 
     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('listener', anonymous=True)
 
     rospy.Subscriber("motor_values", String, callback)
 
     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()
 
if __name__ == '__main__':
    listener()

file_object.close()