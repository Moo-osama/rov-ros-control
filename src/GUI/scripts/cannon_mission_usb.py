#!/usr/bin/env python
#1- Press either '1', '2', '3', or 'l' to start working on radius 1, radius 2, radius 3, and length respectively
#2- After pressing the letter, draw the first line (the reference) **don't press enter now
#3- draw the second line that u wanna measure and press 't'
#4- repeat for the rest
#5- u can repeat for a previously-calculated radius, by pressing the same letter, and its value will be updated
#6- once all values are updated as you want, press 'c' and the GUI will be updated with the calculated values.
# Numbers are rounded to nearest decimal place....make sure to change the reference(s)
import array as arr
import math
from math import sqrt
import numpy as np
import cv2
import time
import rospy
from math import ceil
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from GUI.msg import cannonNumbers

uvc_img = Image()
bridge = CvBridge()
pub = rospy.Publisher('cannon_numbers', cannonNumbers, queue_size=10)
btn_down = False

#refrence values
reference4Radii = 13.0
reference4Length = 13.0

def talker():
    msg = cannonNumbers()
    msg.r1 = R1
    msg.r2 = R2
    msg.r3 = R3
    msg.l = L
    pub.publish(msg)

def set_window():
    window = cv2.namedWindow("cannon_mission", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("cannon_mission", 1920,1080)
    cv2.moveWindow("cannon_mission",100,100)

def calc_distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return round(sqrt((x1-x2)**2 + (y1-y2)**2))

def get_points(im):
    # Set up data to send to mouse handler
    flag = True
    data = {}
    data['im'] = im.copy()
    data['lines'] = []
    # Set the callback function for any mouse event
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    while(flag):
        key = cv2.waitKey(3)
        if key == ord('t'):
            flag = False
    cv2.destroyWindow("Image")
    return data['lines'], data['im']

def mouse_handler(event, x, y, flags, data):
    global btn_down
    if event == cv2.EVENT_LBUTTONUP and btn_down:
        #if you release the button, finish the line
        btn_down = False
        data['lines'][0].append((x, y)) #append the second point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255),5)
        cv2.line(data['im'], data['lines'][0][0], data['lines'][0][1], (0,0,255), 2)
        cv2.imshow("Image", data['im'])
    elif event == cv2.EVENT_MOUSEMOVE and btn_down:
        #thi is just for a line visualization
        image = data['im'].copy()
        cv2.line(image, data['lines'][0][0], (x, y), (0,0,0), 1)
        cv2.imshow("Image", image)
    elif event == cv2.EVENT_LBUTTONDOWN and len(data['lines']) < 2:
        btn_down = True
        data['lines'].insert(0,[(x, y)]) #prepend the point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 5, 16)
        cv2.imshow("Image", data['im'])

def main():
    global R1, R2, R3, L
    R1, R2, R3, L =0,0,0,0
    set_window()
    flag = 1
    while(flag and not rospy.is_shutdown()):
        if (R1 is not 0 and R2 is not 0 and R3 is not 0 and L is not 0):
            key = cv2.waitKey(1)
            if key == ord('c'):
                flag = 0
            else:
                if key == ord('1'):
                    cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                    im = cv2.imread("imageRetrievedCannon.jpg")
                    pts, final_image = get_points(im)
                    cv2.imshow('Image', final_image)
                    print ("point 1", (pts))
                    length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                    length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                    R1 = round(length2*reference4Radii*0.5/length1,1)
                    print("baleez")
                    print ("R1 is ", R1)
                    print ("points", pts[0][0][0], pts[0][0][1])
                    #print (pts)
                    #print("r1", (length2,length1,reference4Radii,R1))
                elif key == ord('2'):
                    cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                    im = cv2.imread("imageRetrievedCannon.jpg")
                    pts, final_image = get_points(im)
                    cv2.imshow('Image', final_image)
                    #print ("point 2", (pts))
                    length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                    length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                    R2 = round(length2*reference4Radii*0.5/length1,1)
                    print ("R2 is ", R2)
                    #print (length2,length1,R2)
                elif key == ord('3'):
                    cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                    im = cv2.imread("imageRetrievedCannon.jpg")
                    pts, final_image = get_points(im)
                    cv2.imshow('Image', final_image)
                    #print ("point 3", (pts))
                    length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                    length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                    R3 = round(length2*reference4Radii*0.5/length1,1)
                    print("R3 is ", R3)
                elif key == ord('l'):
                    cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                    im = cv2.imread("imageRetrievedCannon.jpg")
                    pts, final_image = get_points(im)
                    cv2.imshow('Image', final_image)
                    #print ("point 4", (pts))
                    length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                    length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                    L = round(length2*reference4Length/length1,1)
                    print ("Length is ", L)
                    #print (length2,length1,L)
        try:
            current_frame = bridge.imgmsg_to_cv2(uvc_img, "bgr8")
        except CvBridgeError, e:
            print(e)
        else:
            current_frame = cv2.flip(current_frame, 1)
            cv2.imshow('cannon_mission',current_frame)
            if cv2.waitKey(1) == ord('q'):
                flag = 0
                rospy.signal_shutdown('closing')
                cv2.destroyAllWindows()
                #listener()
            key = cv2.waitKey(1)
            if key == ord('1'):
                cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                im = cv2.imread("imageRetrievedCannon.jpg")
                pts, final_image = get_points(im)
                length1 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                length2 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                R1 = round(length2*reference4Radii*0.5/length1,1)
                print ("R1 is ", R1)
                print (pts)
            elif key == ord('2'):
                cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                im = cv2.imread("imageRetrievedCannon.jpg")
                pts, final_image = get_points(im)
                length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                R2 = round(length2*reference4Radii*0.5/length1,1)
                print ("R2 is ", R2)
            elif key == ord('3'):
                cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                im = cv2.imread("imageRetrievedCannon.jpg")
                pts, final_image = get_points(im)
                length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                R3 = round(length2*reference4Radii*0.5/length1,1)
                print ("R3 is ", R3)
            elif key == ord('l'):
                cv2.imwrite("imageRetrievedCannon.jpg", current_frame)
                im = cv2.imread("imageRetrievedCannon.jpg")
                pts, final_image = get_points(im)
                length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
                length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
                L = round(length2*reference4Length/length1,1)
                print ("Length is ", L)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    cv2.destroyAllWindows()
    rospy.signal_shutdown('done!')

def image_callback(msg):
    global uvc_img
    uvc_img = msg

def gui_flag_callback(msg):
    if(str(msg.data) == 'start_AF' or str(msg.data) == 'start_else'):
       pass

def listener():
     rospy.init_node('cannon_mission', anonymous=True)
     rospy.Subscriber("cannon_flag", String, gui_flag_callback)
     rospy.Subscriber('camera/image_raw', Image, image_callback)
     main()
     rospy.spin()

listener()