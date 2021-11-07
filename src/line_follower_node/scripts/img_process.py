#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import cv2
import numpy as np 
import time 
import sys
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os

#camera subscribtion variables
uvc_img = Image()

# Instantiate CvBridge, object
bridge = CvBridge()

# Publisher Information
direction_pub = rospy.Publisher('direction', String, queue_size=10)
crack_pub = rospy.Publisher('crack', String, queue_size=10)

#Golal variables
Directions = []

for i in range(1000):
   Directions.append('i')

INITIATE_flag = 0
flag = 1
prev_len = 0
Max_len = 0
counter = 0
clock1 = time.time()

def camera_input(cap):
    # take first frame of the video
    ret,frame = cap.read()
    return ret, frame

def set_window():
    window = cv2.namedWindow("Image_processing", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image_processing", 1920,1080)
    cv2.moveWindow("Image_processing",100,100)

def Reigons_of_interest(frame):
    H = frame.shape[1]
    V = frame.shape[0]
    u_i = frame[0:V/3, H/3:2*H/3]
    l_i = frame[V/3:2*V/3, 0:H/3]
    m_i = frame[V/3:2*V/3, H/3:2*H/3]
    r_i = frame[V/3:2*V/3, 2*H/3:H]
    d_i = frame[2*V/3:V, H/3:2*H/3]
    return u_i, l_i, m_i, r_i, d_i

def Identify_red(frame):
    Flag = False
    #converting from RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#hsv ranges of colors
    red_lower = np.array([0,87,90],np.uint8)
    red_upper = np.array([5,255,255],np.uint8)
    #finding ranges of colors in the image
    red = cv2.inRange(hsv, red_lower, red_upper)

    #morphological operation - dilation
    kernel = np.ones((5,5), np.uint8)
    red = cv2.dilate(red, kernel)
    resRed = cv2.bitwise_and(frame,frame,mask = red)
    
    #tracking colors
    (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 3000):
            Flag = True
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)
            cv2.putText(frame, "RED", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (25,150,150))
    return Flag

def Identify_blue(frame, prev_len, Max_len):
    Flag = False
    #converting from RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	 #hsv ranges of colors
    blue_lower = np.array([61,81,60],np.uint8)
    blue_upper = np.array([130,255,255],np.uint8)
    #finding ranges of colors in the image
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    
    #morphological operation - dilation
    kernel = np.ones((5,5), np.uint8)
    blue = cv2.dilate(blue, kernel)
    #blue = cv2.erode(blue, kernel)
    resBlue = cv2.bitwise_and(frame,frame,mask = blue)
    

    #cv2.imshow("blue", resBlue)
    #tracking colors
    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 2000):
            prev_len, Max_len = Get_crack_len(resBlue, prev_len, Max_len)
            Flag = True
            p = cv2.arcLength(contour, True)
            v = cv2.approxPolyDP(contour, 0.04*p, True)
            (x, y), (w, h), theta = cv2.minAreaRect(v)
            cv2.drawContours(frame, [v], 0, (0), 5)
            M = cv2.moments(contour)
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
            cv2.putText(frame, "BLUE", (cX,cY), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
            #frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
    return Flag, prev_len, Max_len

def Get_crack_len(frame, prevlen,  Max_len):
   error = 0.83
   scale = 2.3
   length = 0
   gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   edges = cv2.Canny(gray,50,150)
   _, contours, _ = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   for c in contours:
      peri = cv2.arcLength(c, True)
      vertices = cv2.approxPolyDP(c, 0.04 * peri, True)
      if(len(vertices) < 6):
         (x,y),(w,h),theta = cv2.minAreaRect(vertices)
         if(h*w > 120):
            if(w>h and (h/w < 0.4)):
               length = scale*w/h      
            elif((w/h < 0.4)):
               length = scale*h/w
            length = length * error
         
   if(length > Max_len):
      Max_len = length 
      #print(Max_len)
      return length, Max_len
   else:
      return prev_len, Max_len


def directions_2(ROI_arr):
     u_i, l_i, m_i, r_i, d_i = 0,0,0,0,0
     if (Identify_red(ROI_arr[0])):
        u_i = 1
     if (Identify_red(ROI_arr[1])):
        l_i = 1
     if (Identify_red(ROI_arr[2])):
        m_i = 1
     if (Identify_red(ROI_arr[3])):
        r_i = 1
     if (Identify_red(ROI_arr[4])):
        d_i = 1
     return u_i, l_i, m_i, r_i, d_i

def get_direction(ROI_arr, Directions, frame, counter):
     u_i, l_i, m_i, r_i, d_i = directions_2(ROI_arr)
     direction = 'null'
     
     Flag = False
     if(counter >= 1): 
        prev_direction = Directions[counter - 1]
     else:
        prev_direction = 'i'
      
     if(Directions[0] != 'i'):
         if((prev_direction == 'down' or prev_direction == 'up' or prev_direction == 'i')):
            if(l_i == 1  and prev_direction != 'left'):
               direction = 'right'
            elif(r_i == 1 and prev_direction != 'right'):
               direction = 'left'
         if((prev_direction == 'left' or prev_direction == 'right' or prev_direction == 'i')):
            if(d_i == 1  and prev_direction != 'up'):
               direction = 'down'
            elif(u_i == 1 and prev_direction != 'down'):
               direction = 'up'
         if(direction != prev_direction and direction != 'null'):
            Directions[counter] = direction
            counter += 1
            Flag = True 

     if(Directions[0] == 'i'):
         if(d_i == 1 and m_i == 1):
            Directions[counter] = 'down'
            counter += 1
            Flag = True
         elif(u_i == 1 and m_i == 1):
            Directions[counter] = 'up'
            counter += 1
            Flag = True
         elif(l_i == 1 and m_i == 1):
            Directions[counter] = 'left'
            counter += 1
            Flag = True
         elif(r_i == 1 and m_i == 1):
            Directions[counter] = 'right'
            counter += 1
            Flag = True

     return Directions, counter, Flag


def main():
      
      global Directions
      global INITIATE_flag
      global flag
      global prev_len 
      global Max_len
      global counter
      global clock1 
      set_window()
      response = os.system("ping -c 1 -w1 192.168.1.2")
      print(response)
      if(response == 0):
         cam_link = 'rtsp://admin:a1111111@192.168.1.2:554/Streaming/Channels/101'
         cap=cv2.VideoCapture(cam_link)
         flag = 1
      else:
         print('Cameras Not Connected')
         flag =0 
      while(flag and not rospy.is_shutdown()):
         ret, current_frame = cap.read()
         current_frame = cv2.flip(current_frame, 1)
         INITIATE = cv2.waitKey(5) & 0xff
         if INITIATE == 32:
            INITIATE_flag = 1
         
         if(INITIATE_flag):
            
            flag2, prev_len, Max_len = Identify_blue(current_frame, prev_len, Max_len) 
            if(flag2):
                  print("Crack length: ", Max_len)
                  var = "Crack detected with length: " + str(Max_len) 
                  crack_pub.publish(var)
            
            if((time.time()-clock1) >= 2):
                  ROI_arr = Reigons_of_interest(current_frame)
                  #Identfying red in each reigon
                  Directions, counter, flag_print = get_direction(ROI_arr, Directions, current_frame, counter)
                  if(flag_print and not rospy.is_shutdown()):
                     clock1 = time.time()
                     print(Directions[counter - 1])
                     #rospy.loginfo(Directions[counter - 1])
                     direction_pub.publish(Directions[counter - 1])
         
         cv2.imshow("Image_processing", current_frame)
         k = cv2.waitKey(1) & 0xff
         if k == ord('q'):
            flag = 0
            rospy.signal_shutdown('process done')
         elif(k == 32):
            INITIATE_flag = 1
      cv2.destroyAllWindows()

def image_callback(msg):
    global uvc_img
    uvc_img = msg
   
def gui_flag_callback(msg):
    if(str(msg.data) == 'start'):
       pass

def listener():
     rospy.init_node('line_follower_color', anonymous=True)
     rospy.Subscriber("line_follower_flag", String, gui_flag_callback)
     #rospy.Subscriber('camera/image_raw', Image, image_callback)
     main()
     rospy.spin()
     
 

if __name__ == '__main__':    
    listener()

