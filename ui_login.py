# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginjJVydE.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 399)
        MainWindow.setMaximumSize(QSize(484, 399))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setItalic(False)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #4CAF50; /* Green border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    margin-top: 10px; /* Space between the title and the border */\n"
"    background-color: #FFFFFF; /* Light gray background */\n"
"    font: bold 17pt \"Arial\"; /* Font style for the title */\n"
"    color: #333333; /* Dark gray title text color */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; /* Place the title outside the border */\n"
"    subcontrol-position: top center; /* Center the title at the top */\n"
"    padding: 0 5px; /* Padding around the title text */\n"
"    background-color: #FFFFFF; /* White background behind the title */\n"
"    color: #4CAF50; /* Green title text color */\n"
"    font: bold 20pt \"Arial\"; /* Font style for the title */\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 40, 1, 1)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(30, 30, 30, 30)
        self.password_box = QLineEdit(self.frame)
        self.password_box.setObjectName(u"password_box")
        self.password_box.setMinimumSize(QSize(200, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.password_box.setFont(font3)
        self.password_box.setStyleSheet(u"QLineEdit{\n"
"	height:30px;\n"
"	font: 12pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.password_box.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_box)

        self.username_box = QLineEdit(self.frame)
        self.username_box.setObjectName(u"username_box")
        self.username_box.setMinimumSize(QSize(200, 0))
        self.username_box.setFont(font3)
        self.username_box.setStyleSheet(u"QLineEdit{\n"
"	height:30px;\n"
"	font: 12pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_box)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(True)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.login_btn = QPushButton(self.frame)
        self.login_btn.setObjectName(u"login_btn")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        self.login_btn.setFont(font5)
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(76, 175, 80);\n"
"	border-radius:5px;\n"
"	border: 1px solid black;\n"
"	height:30px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.login_btn)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.groupBox, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.username_box, self.password_box)
        QWidget.setTabOrder(self.password_box, self.login_btn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login Window", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"School Management", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Software", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Login Credentials", None))
        self.password_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"pass$word", None))
        self.username_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"user@name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Developed By: Purva Gajpal - BCA Final Year", None))
    # retranslateUi

