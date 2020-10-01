# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerqBmAAq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 85, 127);\n"
"	border-radius: 12px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(40, -1, -1, -1)
        self.label_City = QLabel(self.frame_2)
        self.label_City.setObjectName(u"label_City")
        self.label_City.setStyleSheet(u"color: rgb(85, 170, 255)")

        self.verticalLayout_3.addWidget(self.label_City)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 100, -1)
        self.label_temp = QLabel(self.frame_3)
        self.label_temp.setObjectName(u"label_temp")
        self.label_temp.setStyleSheet(u"color: rgb(85, 170, 255)")
        self.label_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_temp, 0, 0, 2, 1)

        self.label_feels_like = QLabel(self.frame_3)
        self.label_feels_like.setObjectName(u"label_feels_like")
        self.label_feels_like.setStyleSheet(u"color: rgb(85, 170, 255)")

        self.gridLayout.addWidget(self.label_feels_like, 0, 1, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 100, -1)
        self.label_wind_speed = QLabel(self.frame_4)
        self.label_wind_speed.setObjectName(u"label_wind_speed")
        self.label_wind_speed.setStyleSheet(u"color: rgb(85, 170, 255)")

        self.horizontalLayout.addWidget(self.label_wind_speed)

        self.label_pressure_mm = QLabel(self.frame_4)
        self.label_pressure_mm.setObjectName(u"label_pressure_mm")
        self.label_pressure_mm.setStyleSheet(u"color: rgb(85, 170, 255)")

        self.horizontalLayout.addWidget(self.label_pressure_mm)

        self.label_humidity = QLabel(self.frame_4)
        self.label_humidity.setObjectName(u"label_humidity")
        self.label_humidity.setStyleSheet(u"color: rgb(85, 170, 255)")

        self.horizontalLayout.addWidget(self.label_humidity)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 30, 88, 34))

        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_City.setText("")
        self.label_temp.setText("")
        self.label_feels_like.setText("")
        self.label_wind_speed.setText("")
        self.label_pressure_mm.setText("")
        self.label_humidity.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

