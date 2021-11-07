import cv2
import numpy as np

# choose which camera to capture from. 0 is for the webcam
cap = cv2.VideoCapture(0) 


def camera_input(cap):
    # take first frame of the video
    ret,frame = cap.read()
    return ret, frame

ret, frame = camera_input(cap)
window = cv2.namedWindow("Solved Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Solved Image", 1080,720)
cv2.moveWindow("Solved Image",100,100)
cv2.imshow("Solved Image",frame)
k = cv2.waitKey(0) & 0xff
if k == 27:
    flag = 0
elif(k == 32):
    INITIATE_flag = 1