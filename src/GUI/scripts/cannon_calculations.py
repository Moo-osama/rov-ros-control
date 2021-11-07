#!/usr/bin/env python

import rospy
from GUI.msg import cannonNumbers
from std_msgs.msg import String
import numpy as np

canon_calc_pub = rospy.Publisher('calculated_cannon_numbers', cannonNumbers, queue_size=10)

cannon_numbers = cannonNumbers()
specific_gravity = 0.0

def calculate_cannon():
    global cannon_numbers
    global specific_gravity
    arg1 = ((1.0/3.0) * pow (cannon_numbers.r3 - cannon_numbers.r1,2))   # arg1 = (r3 - r1)^2 
    arg2 = (cannon_numbers.r1 * (cannon_numbers.r3 - cannon_numbers.r1)) # arg2 = (r1 * r3) - r1
    arg3 = pow(cannon_numbers.r1, 2)					 # arg3 = r1^2
    arg4 = pow(cannon_numbers.r2, 2)					 # arg4 = r2^2
    cannon_numbers.vol = round(np.pi * cannon_numbers.l * ((arg1 + arg2) + (arg3) - (arg4)),1) #volume = pi * length * ((r3 - r1)^2 + (r1 * r3) - r1 + r1^2 - r2^2)
    
    density = specific_gravity * 1000
    print(density)
    Mass = (cannon_numbers.vol * 1e-6) * density
    print(Mass)
    weight_in_air = 9.81 * Mass
    print(weight_in_air)
    water_weight = 1000 * cannon_numbers.vol * 1e-6 * 9.81
    print(water_weight)
    cannon_numbers.weight = round(weight_in_air - water_weight, 1)
    print(cannon_numbers.weight)

def cannon_callback(msg):
    global cannon_numbers
    cannon_numbers = msg
    calculate_cannon()
    canon_calc_pub.publish(cannon_numbers)


def flag_callback(msg):
    global specific_gravity
    if(str(msg.data) == 'start_AF'):
        specific_gravity = 8.03
    elif(str(msg.data) == 'start_else'):
        specific_gravity = 7.87

def listener():
     rospy.init_node('calculations', anonymous=True)
     rospy.Subscriber('cannon_numbers', cannonNumbers, cannon_callback)
     rospy.Subscriber('cannon_flag', String, flag_callback)
     rospy.spin()
 

if __name__ == '__main__':
    listener()
