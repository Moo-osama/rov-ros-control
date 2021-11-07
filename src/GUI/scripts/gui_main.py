#!/usr/bin/env python

#import for ros
import rospy
from std_msgs.msg import String
from GUI.msg import motors, Num, cannonNumbers
from distributor.msg import rov_msgs
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# subprocess launcher
from subprocess import Popen
import os

#import for qt
import cv2
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import sys
from simple_ui_form import Ui_Form

#port imports
import serial.tools.list_ports as port_list

#Flags Publishers 
species_flag_pub = rospy.Publisher('species_flag', String, queue_size=10)
line_follower_flag_pub = rospy.Publisher('line_follower_flag', String, queue_size=10)
cannon_flag_pub = rospy.Publisher('cannon_flag', String, queue_size=10)
judge_canon_pub = rospy.Publisher('cannon_numbers', cannonNumbers, queue_size=10)

#global variables
cannon_numbers = cannonNumbers()
species_count = Num()
joy_values = String()
rov_msg = rov_msgs()
uvc_img = Image()
crack_length = ''
cap = None
#Text Variables
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (0,0,255)
lineType               = 2

# Instantiate CvBridge, object
bridge = CvBridge()


#variables added before reigonals
ph_offset = 0
temp_offset = 0
ip_bool = False 
usb_bool = False
ph_temp_freez_flag = False
by_pass_mission = False


class main(QWidget, Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.update_values()
        self.Start_cannon.clicked.connect(self.flag_cannon)
        self.Species_start.clicked.connect(self.flag_species)
        self.Species_terminate.clicked.connect(self.kill_species)
        self.Track_line_push.clicked.connect(self.flag_line_follower)
        self.StopButton.clicked.connect(self.kill_line_follower)
        self.canon_judge.clicked.connect(self.calculate_canon_judge)
        self.cam_start_butt.clicked.connect(self.start_cam)
        self.cam_stop_butt.clicked.connect(self.stop_cam)
        self.rov_start_butt.clicked.connect(self.init_rov)
        self.rov_stop_butt.clicked.connect(self.terminate_rov)
        self.set_offset_butt.clicked.connect(self.set_ph_offset)
        self.measure_ph_temp.clicked.connect(self.freez_ph_temp)
        self.set_temp_offset_butt.clicked.connect(self.set_temp_offset)
        self.vid_cap()        
        self.show()

    def freez_ph_temp(self):
        global ph_temp_freez_flag
        ph_temp_freez_flag = True

    def set_ph_offset(self):
        global ph_temp_freez_flag
        ph_temp_freez_flag = False
        global ph_offset
        ph_offset = float(self.in_offset.text())
        print(ph_offset)

    def set_temp_offset(self):
        global ph_temp_freez_flag
        ph_temp_freez_flag = False
        global temp_offset
        temp_offset = float(self.in_temp_offset.text())
        print(temp_offset)

    def init_rov(self):
        global launch_rov
        com_port = str(self.in_com_port.text())
        joy_port = str(self.in_joy_port.text())
        if(len(com_port) > 0):
            com_port = 'port:=' + '/dev/tty' + com_port
        if(len(joy_port) > 0):
            joy_port = 'dev:=' + joy_port    
        launch_rov = Popen('exec ' + 'roslaunch motion_map read_and_write.launch ' + com_port + ' ' + joy_port, shell=True)
        
    def terminate_rov(self):
        global launch_rov
        launch_rov.terminate()

    

    def update_values(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_joy_values)
        self.timer.timeout.connect(self.show_sensor_messages)
        self.timer.timeout.connect(self.show_species_number)
        self.timer.timeout.connect(self.show_value_crack)
        self.timer.timeout.connect(self.show_cannon_values)
        self.timer.start(5)

    def show_value_crack(self):
        #c_l = int(crack_length)
        #if(c_l > 0):
        #   self.grid_2_1.setText(str(crack_length))
        self.crack_value.setText(str(crack_length))

    def show_cannon_values(self):
        self.Radius1Value.setText(str(cannon_numbers.r1))
        self.Radius2Value.setText(str(cannon_numbers.r2))
        self.Radius3Value.setText(str(cannon_numbers.r3))
        self.Cannon_length_value.setText(str(cannon_numbers.l))
        self.Cannon_volume_value.setText(str(cannon_numbers.vol))
        self.Canno_Weight_value.setText(str(cannon_numbers.weight))

    def flag_cannon(self):
        global open_cannon
        global ip_bool 
        global usb_bool
        message = 'error you should check the cannon type'
        open_calc = Popen('exec ' + 'rosrun GUI cannon_calculations.py', shell=True)
        if(self.AF_RB.isChecked()):
            #if(ip_bool is True):
            open_cannon = Popen('exec ' + 'rosrun GUI cannon_mission.py', shell=True)
            #elif(usb_bool is True):
                #open_cannon = Popen('exec ' + 'rosrun GUI cannon_mission_usb.py', shell=True)
            message = 'start_AF'
            cannon_flag_pub.publish(message)

        elif(self.Else_RB.isChecked()):
            #if(ip_bool is True):
            open_cannon = Popen('exec ' + 'rosrun GUI cannon_usb_screenshot_all_2.py', shell=True)
            #elif(usb_bool is True):
                #open_cannon = Popen('exec ' + 'rosrun GUI cannon_mission_usb.py', shell=True) 
            message = 'start_AF'
            cannon_flag_pub.publish(message)
        else:
            print(message)

    def calculate_canon_judge(self):
        cannon_numbers.r1 = float(self.in_rad_1.text())
        cannon_numbers.r2 = float(self.in_rad_2.text())
        cannon_numbers.r3 = float(self.in_rad_3.text())
        cannon_numbers.l = float(self.in_len.text())
        if(self.AF_RB.isChecked()):
            message = 'start_AF'
            cannon_flag_pub.publish(message)
        elif(self.Else_RB.isChecked()):
            message = 'start_else'
            cannon_flag_pub.publish(message)
        if(cannon_numbers.r1 != 0 and cannon_numbers.r2 != 0 and cannon_numbers.r3 != 0 and cannon_numbers.l != 0):
            judge_canon_pub.publish(cannon_numbers)
        else:
            print('All the values should be entered at once')

    def flag_species(self):
        global usb_bool
        global by_pass_mission
        global open_Camera
        #if(usb_bool is False):
            #by_pass_mission = True
            #self.start_cam()
        open_Camera = Popen('exec ' + 'rosrun GUI reigonal_species_ip.py', shell=True)
        #species_flag_pub.publish('start')

    def kill_species(self):
        global open_Camera
        open_Camera.terminate()

    def start_cam(self):
        message = 'error you should check the camera type'
        index = str(self.in_cam_index.text())
        self.stop_cam()
        global ip_bool 
        global usb_bool
        global by_pass_mission
        ip_bool = False
        usb_bool = False
        if(self.IP_RB.isChecked()):
            ip_bool = True
        elif(self.USB_RB.isChecked()):
            usb_bool = True
        else:
            print(message)
        if(by_pass_mission is False):
            if (ip_bool is True and usb_bool is False):
                response = os.system("ping -c 1 -w1 192.168.1.2")
                print(response)
                if(response == 0):
                    
                    print(index)
                    if(index != '1' and index != '2' and index != '3' and index != '4'):
                        index = '1'
                    cam_link = 'rtsp://admin:a1111111@192.168.1.2:554/Streaming/Channels/' + index + '01'
                    #print(cam_link)
                    global cap
                    cap=cv2.VideoCapture(cam_link)
                else:
                    print('Cameras Not Connected')
            elif(usb_bool is True and ip_bool is False):
                if(index != '0' and index != '1' and index != '2' and index != '3'):
                    index = '0'
                command = 'roslaunch video_stream_opencv camera.launch width:=640 height:=480' + ' video_stream_provider:=' + index
                print(command)
                global open_Camera
                open_Camera = Popen('exec ' + command, shell=True)
        else:
            command = 'roslaunch video_stream_opencv camera.launch width:=640 height:=480 video_stream_provider:=1'
            by_pass_mission = False



    def stop_cam(self):
        global cap
        global ip_bool 
        global usb_bool
        global open_Camera
        if(ip_bool is True): 
            if(cap is not None):
                if(cap.isOpened()):
                    cap.release()
            ip_bool = False
        elif(usb_bool is True):
            usb_bool = False
            open_Camera.terminate()

        

    def flag_line_follower(self):
        #global ip_bool 
        #global usb_bool
        global open_line_follower
        #if(usb_bool is True):
            #open_line_follower = Popen('exec ' + 'rosrun GUI line_process_usb_cam.py', shell=True)
            #line_follower_flag_pub.publish('start')
        #elif(ip_bool is True):
        open_line_follower = Popen('exec ' + 'rosrun  line_follower_node img_process.py', shell=True)
        line_follower_flag_pub.publish('start')
            

    def kill_line_follower(self):
        global open_line_follower
        open_line_follower.terminate()
        line_follower_flag_pub.publish('stop')

    def vid_cap(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        global ip_bool 
        global usb_bool

        if(ip_bool is True and usb_bool is False):
            if(cap is not None):
                global cap
                ret, frame = cap.read()
                if(ret != False):
                    #self.image = cv2.flip(frame, 1)
                    self.image = frame
                    cv2.putText(self.image,'Joy values:', (5,40), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,str(joy_values)[7:37], (180,40), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,'Yaw:', (5,80), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,str(rov_msg.yaw), (105,80), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,'Pitch:', (5,120), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,str(rov_msg.pitch), (105,120), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,'Roll:', (5,160), font, fontScale, fontColor, lineType)
                    cv2.putText(self.image,str(rov_msg.roll), (105,160), font, fontScale, fontColor, lineType)
                    self.display_image(self.image, 1)
        elif(usb_bool is True and ip_bool is False):
            try:
                # Convert your ROS Image message to OpenCV2
                cv2_img = bridge.imgmsg_to_cv2(uvc_img, "bgr8")
            except CvBridgeError, e:
                print(e)
            else:
                self.image = cv2.flip(cv2_img, 1)

                cv2.putText(self.image,'Joy values:', (5,40), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,str(joy_values)[7:37], (180,40), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,'Yaw:', (5,80), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,str(rov_msg.yaw), (105,80), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,'Pitch:', (5,120), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,str(rov_msg.pitch), (105,120), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,'Roll:', (5,160), font, fontScale, fontColor, lineType)
                cv2.putText(self.image,str(rov_msg.roll), (105,160), font, fontScale, fontColor, lineType)
                self.display_image(self.image, 1)

    def display_image(self, img, window =1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        out_image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        out_image = out_image.rgbSwapped()
        if window == 1:
            self.Video.setPixmap(QPixmap.fromImage(out_image))
            self.Video.setScaledContents(True)

    def vid_release(self):
        self.timer.stop()
#        self.capture.release()

    def show_species_number(self):
        self.triangle_no.setText(str(species_count.trianglesNo))
        self.circle_no.setText(str(species_count.circlesNo))
        self.square_no.setText(str(species_count.squaresNo))
        self.line_no.setText(str(species_count.linesNo))

    def show_joy_values(self):
        j_v = str(joy_values)
        #print(j_v)
        self.MotorValue1.setText(j_v[8:12])
        self.MotorValue2.setText(j_v[13:17])
        self.MotorValue3.setText(j_v[18:22])
        self.MotorValue4.setText(j_v[23:27])
        self.MotorValue5.setText(j_v[28:32])
        self.MotorValue6.setText(j_v[33:37])

    def show_sensor_messages(self):
        global ph_offset
        global ph_temp_freez_flag
        global temp_offset

        self.Yaw_value.setText(str(rov_msg.yaw))
        self.Pitch.setText(str(rov_msg.pitch))
        self.Magnet1.setText(str(rov_msg.mag1))

        if(ph_temp_freez_flag is False):
            ph_print_value = rov_msg.PH + ph_offset 
            temp_print_value = rov_msg.temp + temp_offset
        else:
            pass
        self.PHvalue.setText(str(ph_print_value))
        self.Temp_value.setText(str(temp_print_value))
        

def run():
    app = QApplication(sys.argv)
    window = main()
    QApplication.processEvents()
    app.exec_()

def retreive_joy_values(data):
     global joy_values
     joy_values = data
     #rospy.loginfo(joy_values)
     
     

def retreive_rov_msgs(data):
     global rov_msg
     rov_msg = data
     
def retreive_crack_length(data):
     global crack_length
     crack_length = data.data
     print('received crack: ', crack_length)

def image_callback(msg):
    global uvc_img
    uvc_img = msg
   
def species_callback(msg):
    global species_count
    species_count = msg

def cannon_callback(msg):
    global cannon_numbers
    cannon_numbers = msg


def listener():
     rospy.init_node('gui_main', anonymous=True)
     rospy.Subscriber("sensors_response_topic", rov_msgs, retreive_rov_msgs)
     rospy.Subscriber("motor_values", String, retreive_joy_values)
     rospy.Subscriber('camera/image_raw', Image, image_callback)
     rospy.Subscriber('crack', String, retreive_crack_length)
     rospy.Subscriber('species_No', Num, species_callback)
     rospy.Subscriber('calculated_cannon_numbers', cannonNumbers, cannon_callback)
     run()
     rospy.spin()
 

if __name__ == '__main__':
    listener()
