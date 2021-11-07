#!/usr/bin/env python
## 1- Press 'a' to capture current frame from the video
## 2- Select with the lines that define your region of interest - select as many as you want. Press 't' when you finish
## 3- Press 'a' to detect and count the shapes

#import imutils
import rospy
import math
import numpy as np
import cv2
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from GUI.msg import Num
import os

# Calibration Variables
ratio_w_h_shape_0 = 0.65
ratio_w_h_shape_1 = 1.35
Lower_black_115_117 = 117


uvc_img = Image()
bridge = CvBridge()
pub = rospy.Publisher('species_No', Num, queue_size=10)
#variables
c,C,T,L,S,w,h=0,-1,0,0,0,0,0
btn_down = False
points = []

def camera_input(cap):
    # take first frame of the video
    ret,frame = cap.read()
    return ret, frame

def talker():
    msg = Num()
    msg.circlesNo = C
    msg.trianglesNo = T
    msg.linesNo = L
    msg.squaresNo = S
    pub.publish(msg)

def color_seg(choice):
    if choice == 'black':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([1,255,255])
    return lower_hue, upper_hue

def detectShape(cnt):
    global ratio_w_h_shape_0
    global ratio_w_h_shape_1
    shape = 'unknown'
    peri = cv2.arcLength(c, True)
    vertices = cv2.approxPolyDP(c, 0.04 * peri, True)
    #if len(vertices) == 2:
        #shape = 'line'
    if len(vertices) == 3:
        shape = 'triangle'
    elif len(vertices) == 4:
        if ((float(w)/h) > ratio_w_h_shape_0 and (float(w)/h) < ratio_w_h_shape_1):
            shape = "square"
        else:
            shape = "line"
    elif len(vertices) > 5:
        shape = 'circle'
    return shape

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
        data['lines'][0].append((x, y)) #append the seconf point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255),2)
        point1 = []
        point1.append(x)
        point1.append(y)
        points.append(point1)
        #print (point1)
        print ("points are: ")
        print (points)
        cv2.line(data['im'], data['lines'][0][0], data['lines'][0][1], (0,0,255), 2)
        cv2.imshow("Image", data['im'])
    elif event == cv2.EVENT_MOUSEMOVE and btn_down:
        #thi is just for a ine visualization
        image = data['im'].copy()
        cv2.line(image, data['lines'][0][0], (x, y), (0,0,0), 1)
        cv2.imshow("Image", image)
    elif event == cv2.EVENT_LBUTTONDOWN and cv2.waitKey(1) is not ord('t'):
        btn_down = True
        data['lines'].insert(0,[(x, y)]) #prepend the point
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 2, 16)
        cv2.imshow("Image", data['im'])

def set_window():
    window = cv2.namedWindow("SpeciesDetectionVideo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("SpeciesDetectionVideo", 1920,1080)
    cv2.moveWindow("SpeciesDetectionVideo",100,100)

def main():
    global c, C, T, L, S, w, h 
    global Lower_black_115_117 
    #set_window()
    INITIATE_flag = 0
    flag = 1
    font = cv2.FONT_HERSHEY_COMPLEX

    '''response = os.system("ping -c 1 -w1 192.168.1.2")
    print(response)
    response = 0
    if(response == 0):
        cam_link = 'rtsp://admin:a1111111@192.168.1.2:554/Streaming/Channels/201'
        cap=cv2.VideoCapture(cam_link)
        flag = 1
    else:
        print('Cameras Not Connected')
        flag =0''' 


    #while(flag and not rospy.is_shutdown()):
    '''ret, current_frame = cap.read()
    counter = 0
    current_frame = cv2.flip(current_frame, 1)
    cv2.imshow('SpeciesDetectionVideo',current_frame)
    if cv2.waitKey(33) == ord('q'):
        flag = 0
        rospy.signal_shutdown('closing')
        cv2.destroyAllWindows()
    if cv2.waitKey(33) == ord('a'):
        cv2.imwrite("imageRetrieved.jpg", current_frame)'''
    im = cv2.imread("/home/mahfouz/Pictures/r.png")
    grayscaleImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    overlayImage=np.copy(grayscaleImage)
    pts, final_image = get_points(im)
    print (pts)
    
    mask = np.ones(im.shape, dtype=np.uint8)
    mask.fill(255)
    roi_corners = np.array(points, dtype=np.int32)
    cv2.fillConvexPoly(mask, roi_corners, 0)
    cv2.imwrite('image_masked.png', mask)
    out = cv2.bitwise_or(im, mask)
    cv2.imshow('image_masked.png', out)
    cv2.waitKey(0)
    
    #for i in range(0,255):
        #for j in range(0, 255):
            #out[np.where((out == [i][j]))] = [255]
    #cv2.imwrite('new_masked_image.png', out)
    #cv2.imshow('NEWEST_image_masked.png', out)
    #cv2.waitKey(0)

    ##
    for i in range(Lower_black_115_117,255):
        out[np.where(out == [i])] = [255]
    cv2.imwrite('new_masked_image.png', out)                
    cv2.imshow('NEWEST_image_masked.png', out)
    cv2.waitKey(0)
    ##

    gray = cv2.cvtColor(out,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150)
    cv2.imshow('edges', edges)
    cv2.waitKey(0)
    _, contours, _ = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    L,T,S,C=0,0,0,0
    for c in contours:
        M = cv2.moments(c)
        if M['m00'] == 0:
            cX, cY = 0, 0
        else:
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
        p = cv2.arcLength(c,True)
        v = cv2.approxPolyDP(c,0.04*p,True)
        (x,y),(w,h),theta = cv2.minAreaRect(v)
        cv2.drawContours(out, [v], 0, (0), 5) #1
        x = v.ravel()[0] #2
        y = v.ravel()[1] #3
        shape = detectShape(c)
        if w >= h:
            if w > 30 and w < 400:
                if shape == 'line':
                    L += 1
                elif shape == 'triangle':
                    T += 1
                elif shape == 'square':
                    S += 1
                elif shape == 'circle':
                    C+= 1
        else:
            if h > 30 and h < 400:
                if shape == 'line':
                    L += 1
                elif shape == 'triangle':
                    T += 1
                elif shape == 'square':
                    S += 1
                elif shape == 'circle':
                    C+= 1
        #flag = 0
    cv2.imshow("finished", out)
    key = cv2.waitKey(0)
    if key == ord('r'):
        pass
    print('Number of lines is ', L)
    print('Number of triangles is ', T)
    print('Number of squares is ', S)
    print('Number of circles is ', C)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    cv2.destroyAllWindows()

def image_callback(msg):
    global uvc_img
    uvc_img = msg
   
def gui_flag_callback(msg):
    if(str(msg.data) == 'start'):
       pass
    
def listener():
     rospy.init_node('shapes_detection', anonymous=True)
     rospy.Subscriber("species_flag", String, gui_flag_callback)
     rospy.Subscriber('camera/image_raw', Image, image_callback)
     main()
     rospy.spin()

listener()
