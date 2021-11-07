#!/usr/bin/env python
## R2 < R1 < R3 < Length
import array as arr
import math
from math import sqrt
import numpy as np
import cv2
import time
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from GUI.msg import cannonNumbers
import os 

uvc_img = Image()
bridge = CvBridge()
pub = rospy.Publisher('cannon_numbers', cannonNumbers, queue_size=10)
btn_down = False
empty = []
reference4Radii = 22.8
reference4Length = 11.0
msg = cannonNumbers()
'''
def talker():
    msg = cannonNumbers()
    msg.r1 = R1
    msg.r2 = R2
    msg.r3 = R3
    msg.l = L
    pub.publish(msg)
'''
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
    data = {}
    data['im'] = im.copy()
    data['lines'] = []
    # Set the callback function for any mouse event
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)
    cv2.destroyWindow("Image")
    return data['lines'], data['im']

    # Convert array to np.array in shape n,2,2
    # points = np.uint16(data['lines'])

def mouse_handler(event, x, y, flags, data):
    global btn_down

    if event == cv2.EVENT_LBUTTONUP and btn_down:
        #if you release the button, finish the line
        btn_down = False
        data['lines'][0].append((x, y)) #append the seconf point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255),2)
        cv2.line(data['im'], data['lines'][0][0], data['lines'][0][1], (0,0,255), 1)
        cv2.imshow("Image", data['im'])

    elif event == cv2.EVENT_MOUSEMOVE and btn_down:
        #thi is just for a ine visualization
        image = data['im'].copy()
        cv2.line(image, data['lines'][0][0], (x, y), (0,0,0), 1)
        cv2.imshow("Image", image)

    elif event == cv2.EVENT_LBUTTONDOWN and len(data['lines']) < 2:
        btn_down = True
        data['lines'].insert(0,[(x, y)]) #prepend the point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 1, 16)
        cv2.imshow("Image", data['im'])

def get_points_new(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['lines'] = []
    # Set the callback function for any mouse event
    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler_new, data)
    cv2.waitKey(0)
    cv2.destroyWindow("Image")
    return data['lines'], data['im']

    # Convert array to np.array in shape n,2,2
    #points = np.uint16(data['lines'])

def mouse_handler_new(event, x, y, flags, data):
    global btn_down
    if event == cv2.EVENT_LBUTTONUP and btn_down:
        #if you release the button, finish the line
        btn_down = False
        data['lines'][0].append((x, y)) #append the seconf point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255),2)
        cv2.line(data['im'], data['lines'][0][0], data['lines'][0][1], (0,0,255), 1)
        cv2.imshow("Image", data['im'])
    elif event == cv2.EVENT_MOUSEMOVE and btn_down:
        #thi is just for a ine visualization
        image = data['im'].copy()
        cv2.line(image, data['lines'][0][0], (x, y), (0,0,0), 1)
        cv2.imshow("Image", image)
    elif event == cv2.EVENT_LBUTTONDOWN and len(data['lines']) < 3:
        btn_down = True
        data['lines'].insert(0,[(x, y)]) #prepend the point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 1, 16)
        cv2.imshow("Image", data['im'])

def start():
    key = cv2.waitKey(1)
    if key == ord('1'):
        calculate1()
    elif key == ord('2'):
        calculate3()
    elif key == ord('l'):
        calculateL()

def calculate1():
    im = cv2.imread("/home/mahfouz/Pictures/r1_2.png")
    pts, final_image = get_points_new(im)
    if pts != empty:
        length1 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
        length2 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
        length3 = calc_distance((pts[2][0][0],pts[2][0][1]),(pts[2][1][0],pts[2][1][1])) #check this
        R1 = length2*reference4Radii*0.5/length1 ###CHECK THISSSS
        R2 = length3*reference4Radii*0.5/length1 ###CHECK THISSSS
        if R2 > R1:
            R1, R2 = R2, R1 #swapping
        msg.r1 = R1
        msg.r2 = R2
        '''print ("length 3:")
        print (length3)
        print ("length 2:")
        print (length2)
        print ("length 1:")
        print (length1)
        print ("R1")
        print (R1)
        print ("R2")
        print (R2)'''
        #cv2.waitKey(0)
        #cv2.destroyWindow('imageR1')
        cv2.waitKey(0)
        calculate3()
    else:
        calculate1()

def calculate3():
    im = cv2.imread("/home/mahfouz/Pictures/r3.png")
    pts, final_image = get_points(im)
    #cv2.imshow('ImageR3', final_image)
    #print (pts)
    if pts != empty:
        length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
        length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
        R3 = length2*reference4Radii*0.5/length1
        msg.r3 = R3
        #print ("R3:")
        #print (length2,length1,R3)
        #cv2.waitKey(0)
        #cv2.destroyWindow('imageR3')
        cv2.waitKey(0)
        calculateL()
    else:
        calculate3()

def calculateL():
    im = cv2.imread("/home/mahfouz/Pictures/len.png")
    pts, final_image = get_points(im)
    if pts != empty:
        length2 = calc_distance((pts[0][0][0],pts[0][0][1]),(pts[0][1][0],pts[0][1][1]))
        length1 = calc_distance((pts[1][0][0],pts[1][0][1]),(pts[1][1][0],pts[1][1][1]))
        L = length2*reference4Length/length1
        msg.l = L
        #print ("length:")
        #print (length2,length1,L)
        pub.publish(msg)
        cv2.destroyAllWindows() ##
    else:
        calculateL()

def newMain():
    global R1, R2, R3, L, flag
    R1, R2, R3, L =0,0,0,0    
    #set_window()
    flag = 1
    '''response = os.system("ping -c 1 -w1 192.168.1.2")
    print(response)
    response = 0
    if(response == 0):
        cam_link = 'rtsp://admin:a1111111@192.168.1.2:554/Streaming/Channels/101'
        cap=cv2.VideoCapture(cam_link)
        flag = 1
    else:
        print('Cameras Not Connected')
        flag =0''' 



        #writeImage(current_frame)
        #ret, current_frame = cap.read()
        #current_frame = cv2.flip(current_frame, 1)
        #cv2.imshow('cannon_mission',current_frame)
    '''if cv2.waitKey(1) == ord('q'):
        flag = 0
        rospy.signal_shutdown('closing')
        cv2.destroyAllWindows()'''
    calculate1()
    print ("reached here - flag = 0")
    #talker()
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
     #rospy.Subscriber('camera/image_raw', Image, image_callback)
     newMain()
     rospy.spin()

listener()
