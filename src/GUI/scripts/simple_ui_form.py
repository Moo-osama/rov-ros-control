# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_ui_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1149, 723)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Qtab = QtGui.QTabWidget(Form)
        self.Qtab.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(0, 0, 139);"))
        self.Qtab.setObjectName(_fromUtf8("Qtab"))
        self.MainTab = QtGui.QWidget()
        self.MainTab.setObjectName(_fromUtf8("MainTab"))
        self.splitter_8 = QtGui.QSplitter(self.MainTab)
        self.splitter_8.setGeometry(QtCore.QRect(243, 233, 875, 4))
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.splitter_9 = QtGui.QSplitter(self.splitter_8)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.splitter_11 = QtGui.QSplitter(self.splitter_8)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.Joy_values_label = QtGui.QLabel(self.MainTab)
        self.Joy_values_label.setGeometry(QtCore.QRect(720, 0, 201, 51))
        self.Joy_values_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Joy_values_label.setObjectName(_fromUtf8("Joy_values_label"))
        self.splitter_6 = QtGui.QSplitter(self.MainTab)
        self.splitter_6.setGeometry(QtCore.QRect(20, 500, 311, 101))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.Temp_sens_label_4 = QtGui.QLabel(self.splitter_6)
        self.Temp_sens_label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Temp_sens_label_4.setObjectName(_fromUtf8("Temp_sens_label_4"))
        self.Magnet1 = QtGui.QTextBrowser(self.splitter_6)
        self.Magnet1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Magnet1.setObjectName(_fromUtf8("Magnet1"))
        self.splitter_3 = QtGui.QSplitter(self.MainTab)
        self.splitter_3.setGeometry(QtCore.QRect(800, 460, 311, 191))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter_43 = QtGui.QSplitter(self.splitter_3)
        self.splitter_43.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_43.setObjectName(_fromUtf8("splitter_43"))
        self.rov_start_butt = QtGui.QPushButton(self.splitter_43)
        self.rov_start_butt.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.rov_start_butt.setObjectName(_fromUtf8("rov_start_butt"))
        self.rov_stop_butt = QtGui.QPushButton(self.splitter_43)
        self.rov_stop_butt.setStyleSheet(_fromUtf8("background-color: rgb(128, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.rov_stop_butt.setObjectName(_fromUtf8("rov_stop_butt"))
        self.splitter_46 = QtGui.QSplitter(self.splitter_3)
        self.splitter_46.setOrientation(QtCore.Qt.Vertical)
        self.splitter_46.setObjectName(_fromUtf8("splitter_46"))
        self.splitter_45 = QtGui.QSplitter(self.splitter_46)
        self.splitter_45.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_45.setObjectName(_fromUtf8("splitter_45"))
        self.Roll_label_3 = QtGui.QLabel(self.splitter_45)
        self.Roll_label_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Roll_label_3.setObjectName(_fromUtf8("Roll_label_3"))
        self.in_com_port = QtGui.QLineEdit(self.splitter_45)
        self.in_com_port.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_com_port.setObjectName(_fromUtf8("in_com_port"))
        self.splitter_44 = QtGui.QSplitter(self.splitter_46)
        self.splitter_44.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_44.setObjectName(_fromUtf8("splitter_44"))
        self.Roll_label_4 = QtGui.QLabel(self.splitter_44)
        self.Roll_label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Roll_label_4.setObjectName(_fromUtf8("Roll_label_4"))
        self.in_joy_port = QtGui.QLineEdit(self.splitter_44)
        self.in_joy_port.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_joy_port.setObjectName(_fromUtf8("in_joy_port"))
        self.splitter_23 = QtGui.QSplitter(self.MainTab)
        self.splitter_23.setGeometry(QtCore.QRect(390, 60, 731, 91))
        self.splitter_23.setOrientation(QtCore.Qt.Vertical)
        self.splitter_23.setObjectName(_fromUtf8("splitter_23"))
        self.splitter_13 = QtGui.QSplitter(self.splitter_23)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName(_fromUtf8("splitter_13"))
        self.Joy_values_label_14 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_14.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Joy_values_label_14.setObjectName(_fromUtf8("Joy_values_label_14"))
        self.Joy_values_label_15 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_15.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Joy_values_label_15.setObjectName(_fromUtf8("Joy_values_label_15"))
        self.Joy_values_label_16 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_16.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Joy_values_label_16.setObjectName(_fromUtf8("Joy_values_label_16"))
        self.Joy_values_label_17 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_17.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Joy_values_label_17.setObjectName(_fromUtf8("Joy_values_label_17"))
        self.Joy_values_label_18 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_18.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Joy_values_label_18.setObjectName(_fromUtf8("Joy_values_label_18"))
        self.Joy_values_label_19 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_19.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Joy_values_label_19.setObjectName(_fromUtf8("Joy_values_label_19"))
        self.splitter_12 = QtGui.QSplitter(self.splitter_23)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName(_fromUtf8("splitter_12"))
        self.MotorValue1 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.MotorValue1.setObjectName(_fromUtf8("MotorValue1"))
        self.MotorValue2 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue2.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);\n"
""))
        self.MotorValue2.setObjectName(_fromUtf8("MotorValue2"))
        self.MotorValue3 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue3.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.MotorValue3.setObjectName(_fromUtf8("MotorValue3"))
        self.MotorValue4 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue4.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.MotorValue4.setObjectName(_fromUtf8("MotorValue4"))
        self.MotorValue5 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue5.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.MotorValue5.setObjectName(_fromUtf8("MotorValue5"))
        self.MotorValue6 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue6.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.MotorValue6.setObjectName(_fromUtf8("MotorValue6"))
        self.splitter_32 = QtGui.QSplitter(self.MainTab)
        self.splitter_32.setGeometry(QtCore.QRect(650, 280, 451, 131))
        self.splitter_32.setOrientation(QtCore.Qt.Vertical)
        self.splitter_32.setObjectName(_fromUtf8("splitter_32"))
        self.measure_ph_temp = QtGui.QPushButton(self.splitter_32)
        self.measure_ph_temp.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.measure_ph_temp.setObjectName(_fromUtf8("measure_ph_temp"))
        self.splitter_31 = QtGui.QSplitter(self.splitter_32)
        self.splitter_31.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_31.setObjectName(_fromUtf8("splitter_31"))
        self.splitter = QtGui.QSplitter(self.splitter_31)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.PH_label = QtGui.QLabel(self.splitter)
        self.PH_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.PH_label.setObjectName(_fromUtf8("PH_label"))
        self.PHvalue = QtGui.QTextBrowser(self.splitter)
        self.PHvalue.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.PHvalue.setObjectName(_fromUtf8("PHvalue"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_31)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.Temp_sens_label = QtGui.QLabel(self.splitter_4)
        self.Temp_sens_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Temp_sens_label.setObjectName(_fromUtf8("Temp_sens_label"))
        self.Temp_value = QtGui.QTextBrowser(self.splitter_4)
        self.Temp_value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Temp_value.setObjectName(_fromUtf8("Temp_value"))
        self.unit_label_8 = QtGui.QLabel(self.splitter_4)
        self.unit_label_8.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.unit_label_8.setObjectName(_fromUtf8("unit_label_8"))
        self.splitter_47 = QtGui.QSplitter(self.MainTab)
        self.splitter_47.setGeometry(QtCore.QRect(390, 320, 251, 91))
        self.splitter_47.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_47.setObjectName(_fromUtf8("splitter_47"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_47)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.Yaw_label = QtGui.QLabel(self.splitter_2)
        self.Yaw_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Yaw_label.setObjectName(_fromUtf8("Yaw_label"))
        self.Pitch_label = QtGui.QLabel(self.splitter_2)
        self.Pitch_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Pitch_label.setObjectName(_fromUtf8("Pitch_label"))
        self.splitter_38 = QtGui.QSplitter(self.splitter_47)
        self.splitter_38.setOrientation(QtCore.Qt.Vertical)
        self.splitter_38.setObjectName(_fromUtf8("splitter_38"))
        self.Yaw_value = QtGui.QTextBrowser(self.splitter_38)
        self.Yaw_value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Yaw_value.setObjectName(_fromUtf8("Yaw_value"))
        self.Pitch = QtGui.QTextBrowser(self.splitter_38)
        self.Pitch.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Pitch.setObjectName(_fromUtf8("Pitch"))
        self.splitter_49 = QtGui.QSplitter(self.MainTab)
        self.splitter_49.setGeometry(QtCore.QRect(20, 30, 307, 355))
        self.splitter_49.setOrientation(QtCore.Qt.Vertical)
        self.splitter_49.setObjectName(_fromUtf8("splitter_49"))
        self.logo_label = QtGui.QLabel(self.splitter_49)
        self.logo_label.setText(_fromUtf8(""))
        self.logo_label.setPixmap(QtGui.QPixmap(_fromUtf8("../fuckin_ws/src/GUI/scripts/pixmaps/logo.jpg")))
        self.logo_label.setObjectName(_fromUtf8("logo_label"))
        self.Temp_sens_label_5 = QtGui.QLabel(self.splitter_49)
        self.Temp_sens_label_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Temp_sens_label_5.setObjectName(_fromUtf8("Temp_sens_label_5"))
        self.splitter_50 = QtGui.QSplitter(self.MainTab)
        self.splitter_50.setGeometry(QtCore.QRect(390, 460, 401, 191))
        self.splitter_50.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_50.setObjectName(_fromUtf8("splitter_50"))
        self.splitter_48 = QtGui.QSplitter(self.splitter_50)
        self.splitter_48.setOrientation(QtCore.Qt.Vertical)
        self.splitter_48.setObjectName(_fromUtf8("splitter_48"))
        self.IP_RB = QtGui.QRadioButton(self.splitter_48)
        self.IP_RB.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);"))
        self.IP_RB.setObjectName(_fromUtf8("IP_RB"))
        self.USB_RB = QtGui.QRadioButton(self.splitter_48)
        self.USB_RB.setStyleSheet(_fromUtf8("  color: white;\n"
"background-color: rgb(136, 138, 133);"))
        self.USB_RB.setObjectName(_fromUtf8("USB_RB"))
        self.splitter_42 = QtGui.QSplitter(self.splitter_50)
        self.splitter_42.setOrientation(QtCore.Qt.Vertical)
        self.splitter_42.setObjectName(_fromUtf8("splitter_42"))
        self.splitter_33 = QtGui.QSplitter(self.splitter_42)
        self.splitter_33.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_33.setObjectName(_fromUtf8("splitter_33"))
        self.cam_start_butt = QtGui.QPushButton(self.splitter_33)
        self.cam_start_butt.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.cam_start_butt.setObjectName(_fromUtf8("cam_start_butt"))
        self.cam_stop_butt = QtGui.QPushButton(self.splitter_33)
        self.cam_stop_butt.setStyleSheet(_fromUtf8("background-color: rgb(128, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.cam_stop_butt.setObjectName(_fromUtf8("cam_stop_butt"))
        self.splitter_41 = QtGui.QSplitter(self.splitter_42)
        self.splitter_41.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_41.setObjectName(_fromUtf8("splitter_41"))
        self.Roll_label_2 = QtGui.QLabel(self.splitter_41)
        self.Roll_label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Roll_label_2.setObjectName(_fromUtf8("Roll_label_2"))
        self.in_cam_index = QtGui.QLineEdit(self.splitter_41)
        self.in_cam_index.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_cam_index.setObjectName(_fromUtf8("in_cam_index"))
        self.splitter_53 = QtGui.QSplitter(self.MainTab)
        self.splitter_53.setGeometry(QtCore.QRect(649, 160, 471, 96))
        self.splitter_53.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_53.setObjectName(_fromUtf8("splitter_53"))
        self.splitter_104 = QtGui.QSplitter(self.splitter_53)
        self.splitter_104.setOrientation(QtCore.Qt.Vertical)
        self.splitter_104.setObjectName(_fromUtf8("splitter_104"))
        self.set_offset_butt = QtGui.QPushButton(self.splitter_104)
        self.set_offset_butt.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.set_offset_butt.setObjectName(_fromUtf8("set_offset_butt"))
        self.splitter_103 = QtGui.QSplitter(self.splitter_104)
        self.splitter_103.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_103.setObjectName(_fromUtf8("splitter_103"))
        self.Roll_label_8 = QtGui.QLabel(self.splitter_103)
        self.Roll_label_8.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Roll_label_8.setObjectName(_fromUtf8("Roll_label_8"))
        self.in_offset = QtGui.QLineEdit(self.splitter_103)
        self.in_offset.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_offset.setObjectName(_fromUtf8("in_offset"))
        self.splitter_52 = QtGui.QSplitter(self.splitter_53)
        self.splitter_52.setOrientation(QtCore.Qt.Vertical)
        self.splitter_52.setObjectName(_fromUtf8("splitter_52"))
        self.set_temp_offset_butt = QtGui.QPushButton(self.splitter_52)
        self.set_temp_offset_butt.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.set_temp_offset_butt.setObjectName(_fromUtf8("set_temp_offset_butt"))
        self.splitter_51 = QtGui.QSplitter(self.splitter_52)
        self.splitter_51.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_51.setObjectName(_fromUtf8("splitter_51"))
        self.Roll_label_9 = QtGui.QLabel(self.splitter_51)
        self.Roll_label_9.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
"\n"
""))
        self.Roll_label_9.setObjectName(_fromUtf8("Roll_label_9"))
        self.in_temp_offset = QtGui.QLineEdit(self.splitter_51)
        self.in_temp_offset.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_temp_offset.setObjectName(_fromUtf8("in_temp_offset"))
        self.Qtab.addTab(self.MainTab, _fromUtf8(""))
        self.CannonMission = QtGui.QWidget()
        self.CannonMission.setObjectName(_fromUtf8("CannonMission"))
        self.splitter_37 = QtGui.QSplitter(self.CannonMission)
        self.splitter_37.setGeometry(QtCore.QRect(9, 9, 667, 656))
        self.splitter_37.setOrientation(QtCore.Qt.Vertical)
        self.splitter_37.setObjectName(_fromUtf8("splitter_37"))
        self.splitter_36 = QtGui.QSplitter(self.splitter_37)
        self.splitter_36.setOrientation(QtCore.Qt.Vertical)
        self.splitter_36.setObjectName(_fromUtf8("splitter_36"))
        self.splitter_35 = QtGui.QSplitter(self.splitter_36)
        self.splitter_35.setOrientation(QtCore.Qt.Vertical)
        self.splitter_35.setObjectName(_fromUtf8("splitter_35"))
        self.splitter_34 = QtGui.QSplitter(self.splitter_35)
        self.splitter_34.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_34.setObjectName(_fromUtf8("splitter_34"))
        self.Canon_T_Label = QtGui.QLabel(self.splitter_34)
        self.Canon_T_Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Canon_T_Label.setObjectName(_fromUtf8("Canon_T_Label"))
        self.splitter_19 = QtGui.QSplitter(self.splitter_34)
        self.splitter_19.setOrientation(QtCore.Qt.Vertical)
        self.splitter_19.setObjectName(_fromUtf8("splitter_19"))
        self.AF_RB = QtGui.QRadioButton(self.splitter_19)
        self.AF_RB.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);\n"
"  color: white;"))
        self.AF_RB.setObjectName(_fromUtf8("AF_RB"))
        self.Else_RB = QtGui.QRadioButton(self.splitter_19)
        self.Else_RB.setStyleSheet(_fromUtf8("  color: white;\n"
"background-color: rgb(136, 138, 133);"))
        self.Else_RB.setObjectName(_fromUtf8("Else_RB"))
        self.Start_cannon = QtGui.QPushButton(self.splitter_35)
        self.Start_cannon.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Start_cannon.setObjectName(_fromUtf8("Start_cannon"))
        self.splitter_21 = QtGui.QSplitter(self.splitter_36)
        self.splitter_21.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_21.setObjectName(_fromUtf8("splitter_21"))
        self.splitter_17 = QtGui.QSplitter(self.splitter_21)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName(_fromUtf8("splitter_17"))
        self.Radius1_Label = QtGui.QLabel(self.splitter_17)
        self.Radius1_Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"\n"
""))
        self.Radius1_Label.setObjectName(_fromUtf8("Radius1_Label"))
        self.Radius2_Label = QtGui.QLabel(self.splitter_17)
        self.Radius2_Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
""))
        self.Radius2_Label.setObjectName(_fromUtf8("Radius2_Label"))
        self.Radius3_Label = QtGui.QLabel(self.splitter_17)
        self.Radius3_Label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Radius3_Label.setObjectName(_fromUtf8("Radius3_Label"))
        self.length_label = QtGui.QLabel(self.splitter_17)
        self.length_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
""))
        self.length_label.setObjectName(_fromUtf8("length_label"))
        self.Volume_label = QtGui.QLabel(self.splitter_17)
        self.Volume_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
""))
        self.Volume_label.setObjectName(_fromUtf8("Volume_label"))
        self.Weight_label = QtGui.QLabel(self.splitter_17)
        self.Weight_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Weight_label.setObjectName(_fromUtf8("Weight_label"))
        self.splitter_18 = QtGui.QSplitter(self.splitter_21)
        self.splitter_18.setOrientation(QtCore.Qt.Vertical)
        self.splitter_18.setObjectName(_fromUtf8("splitter_18"))
        self.Radius1Value = QtGui.QTextBrowser(self.splitter_18)
        self.Radius1Value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Radius1Value.setObjectName(_fromUtf8("Radius1Value"))
        self.Radius2Value = QtGui.QTextBrowser(self.splitter_18)
        self.Radius2Value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Radius2Value.setObjectName(_fromUtf8("Radius2Value"))
        self.Radius3Value = QtGui.QTextBrowser(self.splitter_18)
        self.Radius3Value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Radius3Value.setObjectName(_fromUtf8("Radius3Value"))
        self.Cannon_length_value = QtGui.QTextBrowser(self.splitter_18)
        self.Cannon_length_value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Cannon_length_value.setObjectName(_fromUtf8("Cannon_length_value"))
        self.Cannon_volume_value = QtGui.QTextBrowser(self.splitter_18)
        self.Cannon_volume_value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Cannon_volume_value.setObjectName(_fromUtf8("Cannon_volume_value"))
        self.Canno_Weight_value = QtGui.QTextBrowser(self.splitter_18)
        self.Canno_Weight_value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.Canno_Weight_value.setObjectName(_fromUtf8("Canno_Weight_value"))
        self.splitter_20 = QtGui.QSplitter(self.splitter_21)
        self.splitter_20.setOrientation(QtCore.Qt.Vertical)
        self.splitter_20.setObjectName(_fromUtf8("splitter_20"))
        self.unit_label_2 = QtGui.QLabel(self.splitter_20)
        self.unit_label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
""))
        self.unit_label_2.setObjectName(_fromUtf8("unit_label_2"))
        self.unit_label_3 = QtGui.QLabel(self.splitter_20)
        self.unit_label_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.unit_label_3.setObjectName(_fromUtf8("unit_label_3"))
        self.unit_label_4 = QtGui.QLabel(self.splitter_20)
        self.unit_label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.unit_label_4.setObjectName(_fromUtf8("unit_label_4"))
        self.unit_label_6 = QtGui.QLabel(self.splitter_20)
        self.unit_label_6.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.unit_label_6.setObjectName(_fromUtf8("unit_label_6"))
        self.unit_label_5 = QtGui.QLabel(self.splitter_20)
        self.unit_label_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.unit_label_5.setObjectName(_fromUtf8("unit_label_5"))
        self.unit_label_7 = QtGui.QLabel(self.splitter_20)
        self.unit_label_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.unit_label_7.setObjectName(_fromUtf8("unit_label_7"))
        self.Terminate_Cannon_button = QtGui.QPushButton(self.splitter_37)
        self.Terminate_Cannon_button.setStyleSheet(_fromUtf8("background-color: rgb(128, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Terminate_Cannon_button.setObjectName(_fromUtf8("Terminate_Cannon_button"))
        self.splitter_29 = QtGui.QSplitter(self.CannonMission)
        self.splitter_29.setGeometry(QtCore.QRect(682, 9, 431, 651))
        self.splitter_29.setOrientation(QtCore.Qt.Vertical)
        self.splitter_29.setObjectName(_fromUtf8("splitter_29"))
        self.splitter_27 = QtGui.QSplitter(self.splitter_29)
        self.splitter_27.setOrientation(QtCore.Qt.Vertical)
        self.splitter_27.setObjectName(_fromUtf8("splitter_27"))
        self.splitter_24 = QtGui.QSplitter(self.splitter_27)
        self.splitter_24.setOrientation(QtCore.Qt.Vertical)
        self.splitter_24.setObjectName(_fromUtf8("splitter_24"))
        self.splitter_15 = QtGui.QSplitter(self.splitter_24)
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName(_fromUtf8("splitter_15"))
        self.splitter_7 = QtGui.QSplitter(self.splitter_15)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.Canon_T_Label_6 = QtGui.QLabel(self.splitter_7)
        self.Canon_T_Label_6.setStyleSheet(_fromUtf8("background-color: rgb(128, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";\n"
"  color: white;"))
        self.Canon_T_Label_6.setObjectName(_fromUtf8("Canon_T_Label_6"))
        self.canon_judge = QtGui.QPushButton(self.splitter_7)
        self.canon_judge.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.canon_judge.setObjectName(_fromUtf8("canon_judge"))
        self.splitter_30 = QtGui.QSplitter(self.splitter_15)
        self.splitter_30.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_30.setObjectName(_fromUtf8("splitter_30"))
        self.Canon_T_Label_2 = QtGui.QLabel(self.splitter_30)
        self.Canon_T_Label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Canon_T_Label_2.setObjectName(_fromUtf8("Canon_T_Label_2"))
        self.in_rad_1 = QtGui.QLineEdit(self.splitter_30)
        self.in_rad_1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_rad_1.setObjectName(_fromUtf8("in_rad_1"))
        self.splitter_28 = QtGui.QSplitter(self.splitter_24)
        self.splitter_28.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_28.setObjectName(_fromUtf8("splitter_28"))
        self.Canon_T_Label_4 = QtGui.QLabel(self.splitter_28)
        self.Canon_T_Label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Canon_T_Label_4.setObjectName(_fromUtf8("Canon_T_Label_4"))
        self.in_rad_2 = QtGui.QLineEdit(self.splitter_28)
        self.in_rad_2.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_rad_2.setObjectName(_fromUtf8("in_rad_2"))
        self.splitter_26 = QtGui.QSplitter(self.splitter_27)
        self.splitter_26.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_26.setObjectName(_fromUtf8("splitter_26"))
        self.Canon_T_Label_3 = QtGui.QLabel(self.splitter_26)
        self.Canon_T_Label_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Canon_T_Label_3.setObjectName(_fromUtf8("Canon_T_Label_3"))
        self.in_rad_3 = QtGui.QLineEdit(self.splitter_26)
        self.in_rad_3.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_rad_3.setObjectName(_fromUtf8("in_rad_3"))
        self.splitter_14 = QtGui.QSplitter(self.splitter_29)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName(_fromUtf8("splitter_14"))
        self.Canon_T_Label_5 = QtGui.QLabel(self.splitter_14)
        self.Canon_T_Label_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Canon_T_Label_5.setObjectName(_fromUtf8("Canon_T_Label_5"))
        self.in_len = QtGui.QLineEdit(self.splitter_14)
        self.in_len.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.in_len.setObjectName(_fromUtf8("in_len"))
        self.Qtab.addTab(self.CannonMission, _fromUtf8(""))
        self.SpeceiesDetection = QtGui.QWidget()
        self.SpeceiesDetection.setObjectName(_fromUtf8("SpeceiesDetection"))
        self.splitter_25 = QtGui.QSplitter(self.SpeceiesDetection)
        self.splitter_25.setGeometry(QtCore.QRect(270, 140, 271, 421))
        self.splitter_25.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_25.setObjectName(_fromUtf8("splitter_25"))
        self.splitter_22 = QtGui.QSplitter(self.splitter_25)
        self.splitter_22.setOrientation(QtCore.Qt.Vertical)
        self.splitter_22.setObjectName(_fromUtf8("splitter_22"))
        self.circle_no = QtGui.QTextBrowser(self.splitter_22)
        self.circle_no.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.circle_no.setObjectName(_fromUtf8("circle_no"))
        self.triangle_no = QtGui.QTextBrowser(self.splitter_22)
        self.triangle_no.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.triangle_no.setObjectName(_fromUtf8("triangle_no"))
        self.line_no = QtGui.QTextBrowser(self.splitter_22)
        self.line_no.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.line_no.setObjectName(_fromUtf8("line_no"))
        self.square_no = QtGui.QTextBrowser(self.splitter_22)
        self.square_no.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.square_no.setObjectName(_fromUtf8("square_no"))
        self.label_4 = QtGui.QLabel(self.splitter_25)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/shapes.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.splitter_16 = QtGui.QSplitter(self.SpeceiesDetection)
        self.splitter_16.setGeometry(QtCore.QRect(280, 30, 434, 48))
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName(_fromUtf8("splitter_16"))
        self.Species_start = QtGui.QPushButton(self.splitter_16)
        self.Species_start.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Species_start.setObjectName(_fromUtf8("Species_start"))
        self.Species_terminate = QtGui.QPushButton(self.splitter_16)
        self.Species_terminate.setStyleSheet(_fromUtf8("background-color: rgb(128, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Species_terminate.setObjectName(_fromUtf8("Species_terminate"))
        self.shapes_image = QtGui.QLabel(self.SpeceiesDetection)
        self.shapes_image.setGeometry(QtCore.QRect(550, 140, 141, 421))
        self.shapes_image.setText(_fromUtf8(""))
        self.shapes_image.setPixmap(QtGui.QPixmap(_fromUtf8("../fuckin_ws/src/GUI/scripts/pixmaps/shapes.png")))
        self.shapes_image.setObjectName(_fromUtf8("shapes_image"))
        self.Qtab.addTab(self.SpeceiesDetection, _fromUtf8(""))
        self.LineFollowerMission = QtGui.QWidget()
        self.LineFollowerMission.setObjectName(_fromUtf8("LineFollowerMission"))
        self.gridLayout_8 = QtGui.QGridLayout(self.LineFollowerMission)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.splitter_83 = QtGui.QSplitter(self.LineFollowerMission)
        self.splitter_83.setOrientation(QtCore.Qt.Vertical)
        self.splitter_83.setObjectName(_fromUtf8("splitter_83"))
        self.splitter_5 = QtGui.QSplitter(self.splitter_83)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.splitter_10 = QtGui.QSplitter(self.splitter_5)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.Track_line_push = QtGui.QPushButton(self.splitter_5)
        self.Track_line_push.setStyleSheet(_fromUtf8("background-color: rgb(21, 88, 88);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Track_line_push.setObjectName(_fromUtf8("Track_line_push"))
        self.Cr_len_label_2 = QtGui.QLabel(self.splitter_5)
        self.Cr_len_label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
""))
        self.Cr_len_label_2.setObjectName(_fromUtf8("Cr_len_label_2"))
        self.crack_value = QtGui.QTextBrowser(self.splitter_5)
        self.crack_value.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.crack_value.setObjectName(_fromUtf8("crack_value"))
        self.unit_label = QtGui.QLabel(self.splitter_5)
        self.unit_label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.unit_label.setObjectName(_fromUtf8("unit_label"))
        self.StopButton = QtGui.QPushButton(self.splitter_5)
        self.StopButton.setStyleSheet(_fromUtf8("background-color: rgb(128, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.StopButton.setObjectName(_fromUtf8("StopButton"))
        self.splitter_82 = QtGui.QSplitter(self.splitter_83)
        self.splitter_82.setOrientation(QtCore.Qt.Vertical)
        self.splitter_82.setObjectName(_fromUtf8("splitter_82"))
        self.Cr_len_label_5 = QtGui.QLabel(self.splitter_82)
        self.Cr_len_label_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Cr_len_label_5.setObjectName(_fromUtf8("Cr_len_label_5"))
        self.splitter_81 = QtGui.QSplitter(self.splitter_82)
        self.splitter_81.setOrientation(QtCore.Qt.Vertical)
        self.splitter_81.setObjectName(_fromUtf8("splitter_81"))
        self.splitter_39 = QtGui.QSplitter(self.splitter_81)
        self.splitter_39.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_39.setObjectName(_fromUtf8("splitter_39"))
        self.grid_1_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_1_1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_1_1.setObjectName(_fromUtf8("grid_1_1"))
        self.grid_2_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_2_1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_2_1.setObjectName(_fromUtf8("grid_2_1"))
        self.grid_3_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_3_1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_3_1.setObjectName(_fromUtf8("grid_3_1"))
        self.grid_4_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_4_1.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_4_1.setObjectName(_fromUtf8("grid_4_1"))
        self.splitter_40 = QtGui.QSplitter(self.splitter_81)
        self.splitter_40.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_40.setObjectName(_fromUtf8("splitter_40"))
        self.grid_1_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_1_2.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_1_2.setObjectName(_fromUtf8("grid_1_2"))
        self.grid_2_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_2_2.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_2_2.setObjectName(_fromUtf8("grid_2_2"))
        self.grid_3_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_3_2.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_3_2.setObjectName(_fromUtf8("grid_3_2"))
        self.grid_4_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_4_2.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_4_2.setObjectName(_fromUtf8("grid_4_2"))
        self.splitter_80 = QtGui.QSplitter(self.splitter_81)
        self.splitter_80.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_80.setObjectName(_fromUtf8("splitter_80"))
        self.grid_1_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_1_3.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_1_3.setObjectName(_fromUtf8("grid_1_3"))
        self.grid_2_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_2_3.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_2_3.setObjectName(_fromUtf8("grid_2_3"))
        self.grid_3_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_3_3.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_3_3.setObjectName(_fromUtf8("grid_3_3"))
        self.grid_4_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_4_3.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);"))
        self.grid_4_3.setObjectName(_fromUtf8("grid_4_3"))
        self.gridLayout_8.addWidget(self.splitter_83, 0, 0, 1, 1)
        self.Qtab.addTab(self.LineFollowerMission, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Video = QtGui.QLabel(self.tab)
        self.Video.setFrameShape(QtGui.QFrame.Box)
        self.Video.setText(_fromUtf8(""))
        self.Video.setObjectName(_fromUtf8("Video"))
        self.gridLayout_2.addWidget(self.Video, 0, 0, 1, 1)
        self.Qtab.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.Qtab, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.Qtab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Joy_values_label.setText(_translate("Form", "JOY Values", None))
        self.Temp_sens_label_4.setText(_translate("Form", "MagnetoMeter", None))
        self.rov_start_butt.setText(_translate("Form", "Launch ROV", None))
        self.rov_stop_butt.setText(_translate("Form", "Stop ROV", None))
        self.Roll_label_3.setText(_translate("Form", "com port", None))
        self.Roll_label_4.setText(_translate("Form", "Joy port", None))
        self.Joy_values_label_14.setText(_translate("Form", "A", None))
        self.Joy_values_label_15.setText(_translate("Form", "B", None))
        self.Joy_values_label_16.setText(_translate("Form", "C", None))
        self.Joy_values_label_17.setText(_translate("Form", "D", None))
        self.Joy_values_label_18.setText(_translate("Form", "E", None))
        self.Joy_values_label_19.setText(_translate("Form", "F", None))
        self.MotorValue1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.measure_ph_temp.setText(_translate("Form", "Measure PH,Temp", None))
        self.PH_label.setText(_translate("Form", "PH ", None))
        self.Temp_sens_label.setText(_translate("Form", "Temp", None))
        self.unit_label_8.setText(_translate("Form", "°C", None))
        self.Yaw_label.setText(_translate("Form", "Yaw", None))
        self.Pitch_label.setText(_translate("Form", "Pitch", None))
        self.Yaw_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Temp_sens_label_5.setText(_translate("Form", "            WE DIVE DEEPER!", None))
        self.IP_RB.setText(_translate("Form", "IP", None))
        self.USB_RB.setText(_translate("Form", "USB", None))
        self.cam_start_butt.setText(_translate("Form", "Start Cam", None))
        self.cam_stop_butt.setText(_translate("Form", "Stop Cam", None))
        self.Roll_label_2.setText(_translate("Form", "Index", None))
        self.set_offset_butt.setText(_translate("Form", "set PH offset", None))
        self.Roll_label_8.setText(_translate("Form", "offset", None))
        self.set_temp_offset_butt.setText(_translate("Form", "set Temp offset", None))
        self.Roll_label_9.setText(_translate("Form", "offset", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.MainTab), _translate("Form", "Main Tab", None))
        self.Canon_T_Label.setText(_translate("Form", "Canon Type", None))
        self.AF_RB.setText(_translate("Form", "AF", None))
        self.Else_RB.setText(_translate("Form", "Else", None))
        self.Start_cannon.setText(_translate("Form", "Start Measuring", None))
        self.Radius1_Label.setText(_translate("Form", "Radius1", None))
        self.Radius2_Label.setText(_translate("Form", "Radius2", None))
        self.Radius3_Label.setText(_translate("Form", "Radius3", None))
        self.length_label.setText(_translate("Form", "Length", None))
        self.Volume_label.setText(_translate("Form", "Volume", None))
        self.Weight_label.setText(_translate("Form", "Weight", None))
        self.Radius1Value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Radius2Value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Radius3Value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Cannon_length_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Cannon_volume_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Canno_Weight_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.unit_label_2.setText(_translate("Form", "CM", None))
        self.unit_label_3.setText(_translate("Form", "CM", None))
        self.unit_label_4.setText(_translate("Form", "CM", None))
        self.unit_label_6.setText(_translate("Form", "CM", None))
        self.unit_label_5.setText(_translate("Form", "CM^3", None))
        self.unit_label_7.setText(_translate("Form", "Newton", None))
        self.Terminate_Cannon_button.setText(_translate("Form", "Terminate Process", None))
        self.Canon_T_Label_6.setText(_translate("Form", "Case_failed", None))
        self.canon_judge.setText(_translate("Form", "Judge call", None))
        self.Canon_T_Label_2.setText(_translate("Form", "In_Rad_1", None))
        self.Canon_T_Label_4.setText(_translate("Form", "In_Rad_2", None))
        self.Canon_T_Label_3.setText(_translate("Form", "In_Rad_3", None))
        self.Canon_T_Label_5.setText(_translate("Form", "In_Len_4", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.CannonMission), _translate("Form", "Cannon Mission", None))
        self.circle_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.triangle_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.line_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.square_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Species_start.setText(_translate("Form", "Start Species Mission", None))
        self.Species_terminate.setText(_translate("Form", "Terminate Mission", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.SpeceiesDetection), _translate("Form", "Species Detection", None))
        self.Track_line_push.setText(_translate("Form", "Start Line Track", None))
        self.Cr_len_label_2.setText(_translate("Form", " Crack Length:", None))
        self.crack_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.unit_label.setText(_translate("Form", "  cm", None))
        self.StopButton.setText(_translate("Form", "EMERGENCY STOP", None))
        self.Cr_len_label_5.setText(_translate("Form", "Grid_Mapping", None))
        self.grid_1_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_2_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_3_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_4_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_1_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_2_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_3_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_4_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_1_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_2_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_3_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_4_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.LineFollowerMission), _translate("Form", "Line Follower Mission", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.tab), _translate("Form", "Video Feed", None))

