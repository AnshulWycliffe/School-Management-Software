# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainbphGdB.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1264, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.date_label.setFont(font2)

        self.horizontalLayout.addWidget(self.date_label, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"	background-image: url(:/assets/classroom.png);\n"
"    background-position: center;\n"
"\n"
"}\n"
"")
        self.main_pag = QWidget()
        self.main_pag.setObjectName(u"main_pag")
        self.verticalLayout_4 = QVBoxLayout(self.main_pag)
        self.verticalLayout_4.setSpacing(14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.main_pag)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setFamilies([u"Segoe Print"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_5.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.edit_staff_btn = QPushButton(self.main_pag)
        self.edit_staff_btn.setObjectName(u"edit_staff_btn")
        self.edit_staff_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 127);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets/staff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_staff_btn.setIcon(icon)
        self.edit_staff_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.edit_staff_btn, 1, 4, 1, 1)

        self.staff_attend_btn = QPushButton(self.main_pag)
        self.staff_attend_btn.setObjectName(u"staff_attend_btn")
        self.staff_attend_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/staff-attend.png", QSize(), QIcon.Normal, QIcon.Off)
        self.staff_attend_btn.setIcon(icon1)
        self.staff_attend_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.staff_attend_btn, 3, 2, 1, 1)

        self.edit_btn = QPushButton(self.main_pag)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 255);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/assets/edit_stud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_btn.setIcon(icon2)
        self.edit_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.edit_btn, 1, 2, 1, 1)

        self.teache_btn = QPushButton(self.main_pag)
        self.teache_btn.setObjectName(u"teache_btn")
        self.teache_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 0);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/assets/teaching.png", QSize(), QIcon.Normal, QIcon.Off)
        self.teache_btn.setIcon(icon3)
        self.teache_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.teache_btn, 1, 3, 1, 1)

        self.student_attend_btn = QPushButton(self.main_pag)
        self.student_attend_btn.setObjectName(u"student_attend_btn")
        self.student_attend_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 170, 255);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/attendance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.student_attend_btn.setIcon(icon4)
        self.student_attend_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.student_attend_btn, 3, 1, 1, 1)

        self.marksheet_btn = QPushButton(self.main_pag)
        self.marksheet_btn.setObjectName(u"marksheet_btn")
        self.marksheet_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/assets/result.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marksheet_btn.setIcon(icon5)
        self.marksheet_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.marksheet_btn, 3, 4, 1, 1)

        self.admission_btn = QPushButton(self.main_pag)
        self.admission_btn.setObjectName(u"admission_btn")
        self.admission_btn.setStyleSheet(u"QPushButton{\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";\n"
"	border-radius:5px;\n"
"	border: 1px solid black;\n"
"	background-color: rgb(85, 255, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/assets/admission_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.admission_btn.setIcon(icon6)
        self.admission_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.admission_btn, 1, 1, 1, 1)

        self.marks_btn = QPushButton(self.main_pag)
        self.marks_btn.setObjectName(u"marks_btn")
        self.marks_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 255);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/assets/marks.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marks_btn.setIcon(icon7)
        self.marks_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.marks_btn, 3, 3, 1, 1)

        self.std_rec_btn = QPushButton(self.main_pag)
        self.std_rec_btn.setObjectName(u"std_rec_btn")
        self.std_rec_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 127);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/assets/std_record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.std_rec_btn.setIcon(icon8)
        self.std_rec_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.std_rec_btn, 4, 1, 1, 1)

        self.staff_rec_btn = QPushButton(self.main_pag)
        self.staff_rec_btn.setObjectName(u"staff_rec_btn")
        self.staff_rec_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 85, 127);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/assets/staff_record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.staff_rec_btn.setIcon(icon9)
        self.staff_rec_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.staff_rec_btn, 4, 2, 1, 1)

        self.fees_btn = QPushButton(self.main_pag)
        self.fees_btn.setObjectName(u"fees_btn")
        self.fees_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	height:100px;\n"
"	width: 100px;\n"
"	font: 700 15pt \"Segoe UI\";border-radius:5px;\n"
"	border: 1px solid black;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/assets/fees.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fees_btn.setIcon(icon10)
        self.fees_btn.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.fees_btn, 4, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.logout_btn = QPushButton(self.main_pag)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid black;\n"
"	border-radius:5px;\n"
"	height:40px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/assets/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon11)
        self.logout_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.logout_btn)

        self.minimize_btn = QPushButton(self.main_pag)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid black;\n"
"	border-radius:5px;\n"
"	height:40px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/assets/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon12)
        self.minimize_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.exit_btn = QPushButton(self.main_pag)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid black;\n"
"	border-radius:5px;\n"
"	height:40px;\n"
"	font: 700 14pt \"Segoe UI\";\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/assets/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon13)
        self.exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.exit_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.main_pag)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.admission_btn, self.edit_btn)
        QWidget.setTabOrder(self.edit_btn, self.teache_btn)
        QWidget.setTabOrder(self.teache_btn, self.student_attend_btn)
        QWidget.setTabOrder(self.student_attend_btn, self.staff_attend_btn)
        QWidget.setTabOrder(self.staff_attend_btn, self.marksheet_btn)
        QWidget.setTabOrder(self.marksheet_btn, self.logout_btn)
        QWidget.setTabOrder(self.logout_btn, self.minimize_btn)
        QWidget.setTabOrder(self.minimize_btn, self.exit_btn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"School Management Software", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"School Management", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Software", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date: 12/12/2024 11:00:02 PM", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Admin Dashboard", None))
        self.edit_staff_btn.setText(QCoreApplication.translate("MainWindow", u"Edit Staff Details", None))
        self.staff_attend_btn.setText(QCoreApplication.translate("MainWindow", u"Staff Attendance", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit Student Details", None))
        self.teache_btn.setText(QCoreApplication.translate("MainWindow", u" Staff Details", None))
        self.student_attend_btn.setText(QCoreApplication.translate("MainWindow", u"Student Attendance", None))
        self.marksheet_btn.setText(QCoreApplication.translate("MainWindow", u"Marksheet", None))
        self.admission_btn.setText(QCoreApplication.translate("MainWindow", u"Student Admission", None))
        self.marks_btn.setText(QCoreApplication.translate("MainWindow", u"Marks", None))
        self.std_rec_btn.setText(QCoreApplication.translate("MainWindow", u"Student Record", None))
        self.staff_rec_btn.setText(QCoreApplication.translate("MainWindow", u"Staff Record", None))
        self.fees_btn.setText(QCoreApplication.translate("MainWindow", u"Fees Module", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.minimize_btn.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

