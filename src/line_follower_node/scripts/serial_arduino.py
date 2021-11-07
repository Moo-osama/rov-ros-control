#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from serial import Serial

ser = Serial('/dev/ttyACM0', 9600)
ser.flush()
pub = rospy.Publisher('sensor_values', String, queue_size=10)
rospy.init_node('serial_node', anonymous=True)


def callback(data):
     ser.write(str(data.data))
     if(ser.in_waiting > 10):
         message = str(ser.readline()) 
         print(message)
         pub.publish(message)
     rospy.loginfo("Joy values sent to arduino: %s", data.data)
     

def listener():
     rospy.Subscriber('joy_values', String, callback)
     if(ser.in_waiting > 10):
         message = str(ser.readline()) 
         print(message)
         pub.publish(message)
     rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
      
