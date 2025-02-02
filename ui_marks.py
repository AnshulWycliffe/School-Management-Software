# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'markstmdkKK.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"/* Styling the Tab Widget */\n"
"QTabWidget {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"/* Styling the Tabs */\n"
"QTabBar::tab {\n"
"    background-color: #2196F3;  /* Tab background color */\n"
"    color: white;\n"
"    border: 1px solid #c0c0c0;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    min-width: 80px;\n"
"    min-height: 30px;\n"
"\n"
"	font: 14pt \"Segoe UI\";\n"
"}\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.formFrame = QFrame(self.tab)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setStyleSheet(u"*{\n"
"font: 14pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"/* Styling the QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #f4f4f4;  /* Light grey background */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 2px solid #c0c0c0;  /* Border color */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Focused state (when the QLineEdit is selected) */\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    background-color: #ffffff;  /* White background on focus */\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QLineEdit:disabled {\n"
"    background-color: #e0e0e0;  /* Grey background when disabled */\n"
"    color: #888888;  /* Light grey text when disabled */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Placeholder text style */\n"
"QLineEdit::placeholder {\n"
"    color: #888888;  /* Light grey color for placeholder text */\n"
"    font-style: italic;  /* Italicize the placeholder text */\n"
""
                        "}\n"
"\n"
"/* Styling the text cursor */\n"
"QLineEdit::cursor {\n"
"    color: #2196F3;  /* Change cursor color to blue */\n"
"}\n"
"")
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 0, 0, 0)
        self.label_14 = QLabel(self.formFrame)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.std_id_box = QLineEdit(self.formFrame)
        self.std_id_box.setObjectName(u"std_id_box")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.std_id_box)

        self.label = QLabel(self.formFrame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sub_name = QLineEdit(self.formFrame)
        self.sub_name.setObjectName(u"sub_name")

        self.horizontalLayout.addWidget(self.sub_name)

        self.sub_m1_box = QLineEdit(self.formFrame)
        self.sub_m1_box.setObjectName(u"sub_m1_box")

        self.horizontalLayout.addWidget(self.sub_m1_box)

        self.sub_m2_box = QLineEdit(self.formFrame)
        self.sub_m2_box.setObjectName(u"sub_m2_box")

        self.horizontalLayout.addWidget(self.sub_m2_box)

        self.sub_btn = QPushButton(self.formFrame)
        self.sub_btn.setObjectName(u"sub_btn")
        self.sub_btn.setStyleSheet(u"/* Styling the QPushButton */\n"
"QPushButton {\n"
"    background-color: #4CAF50;  /* Green background */\n"
"    color: white;  /* White text color */\n"
"    border: 2px solid #4CAF50;  /* Border color matches background */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 10px 20px;  /* Vertical and horizontal padding */\n"
"    \n"
"    font: 14pt \"Segoe UI\"; /* Font size */\n"
"    min-width: 100px;  /* Minimum width for the button */\n"
"}\n"
"\n"
"/* Hover effect when the mouse is over the button */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;  /* Darker green background */\n"
"    border-color: #45a049;  /* Darker green border */\n"
"}\n"
"\n"
"/* Pressed effect when the button is clicked */\n"
"QPushButton:pressed {\n"
"    background-color: #388e3c;  /* Even darker green */\n"
"    border-color: #388e3c;  /* Dark border */\n"
"    padding-top: 12px;  /* Slightly reduces padding to simulate a \"pressed\" effect */\n"
"    padding-left: 18px;  /* Shift the button to t"
                        "he left slightly */\n"
"}\n"
"\n"
"/* Focused state (when the button is focused) */\n"
"QPushButton:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    outline: none;  /* Removes the default outline */\n"
"}\n"
"\n"
"/* Disabled state for the QPushButton */\n"
"QPushButton:disabled {\n"
"    background-color: #e0e0e0;  /* Light grey background */\n"
"    color: #888888;  /* Light grey text */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Styling the text of the QPushButton */\n"
"QPushButton {\n"
"    font-weight: bold;  /* Make the text bold */\n"
"}\n"
"\n"
"/* Styling the QPushButton icon (if it has one) */\n"
"QPushButton::icon {\n"
"    padding-right: 10px;  /* Space between the icon and the text */\n"
"}\n"
"\n"
"/* Border effect when the button is in a focus or pressed state */\n"
"QPushButton:focus, QPushButton:pressed {\n"
"    border-style: inset;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.sub_btn)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.horizontalLayout_2.addWidget(self.formFrame, 0, Qt.AlignTop)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.sub_table = QTableWidget(self.tab)
        if (self.sub_table.columnCount() < 4):
            self.sub_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.sub_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sub_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.sub_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.sub_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.sub_table.rowCount() < 3):
            self.sub_table.setRowCount(3)
        self.sub_table.setObjectName(u"sub_table")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.sub_table.setFont(font)
        self.sub_table.setStyleSheet(u"QHeaderView::section {\n"
"background-color: rgb(0, 120, 212);\n"
"     /* Green background for headers */\n"
"    color: white;             /* White text color */\n"
"    font-weight: bold;        /* Bold font for header text */\n"
"    text-align: center;       /* Center-align text */\n"
"	\n"
"	font: 700 14pt \"Segoe UI\";\n"
"    border: 1px solid #ccc;   /* Light gray border around header sections */\n"
"    padding: 5px;             /* Padding inside header cells */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.sub_table)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.fetch_btn = QPushButton(self.tab)
        self.fetch_btn.setObjectName(u"fetch_btn")
        self.fetch_btn.setStyleSheet(u"/* Styling the QPushButton */\n"
"QPushButton {\n"
"    background-color: #4CAF50;  /* Green background */\n"
"    color: white;  /* White text color */\n"
"    border: 2px solid #4CAF50;  /* Border color matches background */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 10px 20px;  /* Vertical and horizontal padding */\n"
"    \n"
"    font: 14pt \"Segoe UI\"; /* Font size */\n"
"    min-width: 100px;  /* Minimum width for the button */\n"
"}\n"
"\n"
"/* Hover effect when the mouse is over the button */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;  /* Darker green background */\n"
"    border-color: #45a049;  /* Darker green border */\n"
"}\n"
"\n"
"/* Pressed effect when the button is clicked */\n"
"QPushButton:pressed {\n"
"    background-color: #388e3c;  /* Even darker green */\n"
"    border-color: #388e3c;  /* Dark border */\n"
"    padding-top: 12px;  /* Slightly reduces padding to simulate a \"pressed\" effect */\n"
"    padding-left: 18px;  /* Shift the button to t"
                        "he left slightly */\n"
"}\n"
"\n"
"/* Focused state (when the button is focused) */\n"
"QPushButton:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    outline: none;  /* Removes the default outline */\n"
"}\n"
"\n"
"/* Disabled state for the QPushButton */\n"
"QPushButton:disabled {\n"
"    background-color: #e0e0e0;  /* Light grey background */\n"
"    color: #888888;  /* Light grey text */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Styling the text of the QPushButton */\n"
"QPushButton {\n"
"    font-weight: bold;  /* Make the text bold */\n"
"}\n"
"\n"
"/* Styling the QPushButton icon (if it has one) */\n"
"QPushButton::icon {\n"
"    padding-right: 10px;  /* Space between the icon and the text */\n"
"}\n"
"\n"
"/* Border effect when the button is in a focus or pressed state */\n"
"QPushButton:focus, QPushButton:pressed {\n"
"    border-style: inset;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.fetch_btn)

        self.save_btn = QPushButton(self.tab)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setStyleSheet(u"/* Styling the QPushButton */\n"
"QPushButton {\n"
"    background-color: #4CAF50;  /* Green background */\n"
"    color: white;  /* White text color */\n"
"    border: 2px solid #4CAF50;  /* Border color matches background */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 10px 20px;  /* Vertical and horizontal padding */\n"
"    \n"
"    font: 14pt \"Segoe UI\"; /* Font size */\n"
"    min-width: 100px;  /* Minimum width for the button */\n"
"}\n"
"\n"
"/* Hover effect when the mouse is over the button */\n"
"QPushButton:hover {\n"
"    background-color: #45a049;  /* Darker green background */\n"
"    border-color: #45a049;  /* Darker green border */\n"
"}\n"
"\n"
"/* Pressed effect when the button is clicked */\n"
"QPushButton:pressed {\n"
"    background-color: #388e3c;  /* Even darker green */\n"
"    border-color: #388e3c;  /* Dark border */\n"
"    padding-top: 12px;  /* Slightly reduces padding to simulate a \"pressed\" effect */\n"
"    padding-left: 18px;  /* Shift the button to t"
                        "he left slightly */\n"
"}\n"
"\n"
"/* Focused state (when the button is focused) */\n"
"QPushButton:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    outline: none;  /* Removes the default outline */\n"
"}\n"
"\n"
"/* Disabled state for the QPushButton */\n"
"QPushButton:disabled {\n"
"    background-color: #e0e0e0;  /* Light grey background */\n"
"    color: #888888;  /* Light grey text */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Styling the text of the QPushButton */\n"
"QPushButton {\n"
"    font-weight: bold;  /* Make the text bold */\n"
"}\n"
"\n"
"/* Styling the QPushButton icon (if it has one) */\n"
"QPushButton::icon {\n"
"    padding-right: 10px;  /* Space between the icon and the text */\n"
"}\n"
"\n"
"/* Border effect when the button is in a focus or pressed state */\n"
"QPushButton:focus, QPushButton:pressed {\n"
"    border-style: inset;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Student ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Subject Details", None))
        self.sub_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sub name", None))
        self.sub_m1_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Theory Marks", None))
        self.sub_m2_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pract./Assign. Marks", None))
        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"Publish", None))
        ___qtablewidgetitem = self.sub_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Subject Name", None));
        ___qtablewidgetitem1 = self.sub_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Theory", None));
        ___qtablewidgetitem2 = self.sub_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Practical / Assignment", None));
        ___qtablewidgetitem3 = self.sub_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.fetch_btn.setText(QCoreApplication.translate("MainWindow", u"Fetch Details", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save && Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Marks Pages", None))
    # retranslateUi

