#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time

f = open("sample_1.txt", "r")
prev_time = time.time()

def talker():
     global prev_time
     pub = rospy.Publisher('joy_values', String, queue_size=10)
     rospy.init_node('joystick', anonymous=True)
     
     while not rospy.is_shutdown():
         time_read = float(f.readline())
         time.sleep(time_read)
         #pub.publish(message)
         print(str(f.readline()))
 
if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass

f.close()





