#!/usr/bin/env python
# license removed for brevity
import rospy
#from std_msgs.msg import String
from GUI.msg import motors
 
flag = 0

def talker():
     pub = rospy.Publisher('joy_values', motors, queue_size=10)
     
     rospy.init_node('joystick', anonymous=True)
     rate = rospy.Rate(1) # 10hz
     while not rospy.is_shutdown():
         global flag
         message = motors()
         if (flag == 0):
            message.motorA = 1500
            message.motorB = 1500
            message.motorC = 1500
            message.motorD = 1500
            message.motorE = 1500
            message.motorF = 1500
            message.PH_button = True
            message.TEMP_button =True
            message.MAG_button = False
            message.WATER_button = False
            flag = 1
         else:
            message.motorA = 1600
            message.motorB = 1650
            message.motorC = 1700
            message.motorD = 1500
            message.motorE = 1300
            message.motorF = 1500
            message.PH_button = False
            message.TEMP_button =True
            message.MAG_button = False
            message.WATER_button = False
            flag = 0
         pub.publish(message)
         rate.sleep()
 
if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass