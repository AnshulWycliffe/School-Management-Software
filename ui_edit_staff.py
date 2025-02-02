# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_staffQFlpGQ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.label_2 = QLabel(self.formFrame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.formFrame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.staff_category_box = QComboBox(self.formFrame)
        self.staff_category_box.addItem("")
        self.staff_category_box.addItem("")
        self.staff_category_box.setObjectName(u"staff_category_box")
        self.staff_category_box.setStyleSheet(u"/* Styling the QComboBox */\n"
"QComboBox {\n"
"    background-color: #f4f4f4;  /* Light grey background */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 2px solid #c0c0c0;  /* Border color */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: 14pt \"Segoe UI\";\n"
"\n"
"    min-width: 150px;  /* Minimum width of the combo box */\n"
"}\n"
"\n"
"/* Styling the combo box when focused */\n"
"QComboBox:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    background-color: #ffffff;  /* White background on focus */\n"
"}\n"
"\n"
"/* Disabled state for the combo box */\n"
"QComboBox:disabled {\n"
"    background-color: #e0e0e0;  /* Grey background when disabled */\n"
"    color: #888888;  /* Light grey text when disabled */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Arrow button of the combo box */\n"
"\n"
"\n"
"/* Styling the dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color"
                        ": #ffffff;  /* White background for the dropdown list */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 1px solid #c0c0c0;  /* Border around the dropdown list */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"/* Hover effect on the dropdown list items */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #2196F3;  /* Blue background on hover */\n"
"    color: #ffffff;  /* White text on hover */\n"
"}\n"
"\n"
"/* Selected item in the dropdown list */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #64B5F6;  /* Light blue background when selected */\n"
"    color: #ffffff;  /* White text when selected */\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.staff_category_box)

        self.label = QLabel(self.formFrame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.staff_fname_box = QLineEdit(self.formFrame)
        self.staff_fname_box.setObjectName(u"staff_fname_box")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.staff_fname_box)

        self.label_3 = QLabel(self.formFrame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.staff_lname_box = QLineEdit(self.formFrame)
        self.staff_lname_box.setObjectName(u"staff_lname_box")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.staff_lname_box)

        self.label_6 = QLabel(self.formFrame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.staff_gen_box = QComboBox(self.formFrame)
        self.staff_gen_box.addItem("")
        self.staff_gen_box.addItem("")
        self.staff_gen_box.setObjectName(u"staff_gen_box")
        self.staff_gen_box.setStyleSheet(u"/* Styling the QComboBox */\n"
"QComboBox {\n"
"    background-color: #f4f4f4;  /* Light grey background */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 2px solid #c0c0c0;  /* Border color */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: 14pt \"Segoe UI\";\n"
"\n"
"    min-width: 150px;  /* Minimum width of the combo box */\n"
"}\n"
"\n"
"/* Styling the combo box when focused */\n"
"QComboBox:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    background-color: #ffffff;  /* White background on focus */\n"
"}\n"
"\n"
"/* Disabled state for the combo box */\n"
"QComboBox:disabled {\n"
"    background-color: #e0e0e0;  /* Grey background when disabled */\n"
"    color: #888888;  /* Light grey text when disabled */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Arrow button of the combo box */\n"
"\n"
"\n"
"/* Styling the dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color"
                        ": #ffffff;  /* White background for the dropdown list */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 1px solid #c0c0c0;  /* Border around the dropdown list */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"/* Hover effect on the dropdown list items */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #2196F3;  /* Blue background on hover */\n"
"    color: #ffffff;  /* White text on hover */\n"
"}\n"
"\n"
"/* Selected item in the dropdown list */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #64B5F6;  /* Light blue background when selected */\n"
"    color: #ffffff;  /* White text when selected */\n"
"}\n"
"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.staff_gen_box)

        self.label_7 = QLabel(self.formFrame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.staff_dob_box = QLineEdit(self.formFrame)
        self.staff_dob_box.setObjectName(u"staff_dob_box")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.staff_dob_box)

        self.lineEdit = QLineEdit(self.formFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)


        self.horizontalLayout_2.addWidget(self.formFrame, 0, Qt.AlignTop)

        self.formFrame_2 = QFrame(self.tab)
        self.formFrame_2.setObjectName(u"formFrame_2")
        self.formFrame_2.setStyleSheet(u"*{\n"
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
        self.formLayout_2 = QFormLayout(self.formFrame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.label_11 = QLabel(self.formFrame_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.formFrame_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.staff_contact_box = QLineEdit(self.formFrame_2)
        self.staff_contact_box.setObjectName(u"staff_contact_box")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.staff_contact_box)

        self.label_17 = QLabel(self.formFrame_2)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_17)

        self.staff_email_box = QLineEdit(self.formFrame_2)
        self.staff_email_box.setObjectName(u"staff_email_box")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.staff_email_box)

        self.label_13 = QLabel(self.formFrame_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.formFrame_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_14)

        self.staff_address_box = QPlainTextEdit(self.formFrame_2)
        self.staff_address_box.setObjectName(u"staff_address_box")
        self.staff_address_box.setMaximumSize(QSize(16777215, 80))
        self.staff_address_box.setStyleSheet(u"/* Styling the QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #f4f4f4;  /* Light grey background */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 2px solid #c0c0c0;  /* Border color */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 8px;\n"
"    font: 14pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"/* Focused state (when the QPlainTextEdit is selected) */\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    background-color: #ffffff;  /* White background on focus */\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QPlainTextEdit:disabled {\n"
"    background-color: #e0e0e0;  /* Grey background when disabled */\n"
"    color: #888888;  /* Light grey text when disabled */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Styling the text cursor */\n"
"QPlainTextEdit::cursor {\n"
"    color: #2196F3;  /* Change cursor color to blue */\n"
"}\n"
"\n"
"/* Styling the selected text */\n"
"QPlainTextEdit::"
                        "selection {\n"
"    background-color: #64B5F6;  /* Light blue background for selected text */\n"
"    color: #ffffff;  /* White text color for selected text */\n"
"}\n"
"\n"
"/* Styling the scroll bar */\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f4f4f4;\n"
"    width: 12px;\n"
"    margin: 0px, 0px, 0px, 0px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPlainTextEdit QScrollBar::handle:vertical {\n"
"    background: #2196F3;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPlainTextEdit QScrollBar::add-line:vertical, \n"
"QPlainTextEdit QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.staff_address_box)

        self.staff_dept_box = QComboBox(self.formFrame_2)
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.addItem("")
        self.staff_dept_box.setObjectName(u"staff_dept_box")
        self.staff_dept_box.setStyleSheet(u"/* Styling the QComboBox */\n"
"QComboBox {\n"
"    background-color: #f4f4f4;  /* Light grey background */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 2px solid #c0c0c0;  /* Border color */\n"
"    border-radius: 5px;  /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: 14pt \"Segoe UI\";\n"
"\n"
"    min-width: 150px;  /* Minimum width of the combo box */\n"
"}\n"
"\n"
"/* Styling the combo box when focused */\n"
"QComboBox:focus {\n"
"    border: 2px solid #2196F3;  /* Blue border when focused */\n"
"    background-color: #ffffff;  /* White background on focus */\n"
"}\n"
"\n"
"/* Disabled state for the combo box */\n"
"QComboBox:disabled {\n"
"    background-color: #e0e0e0;  /* Grey background when disabled */\n"
"    color: #888888;  /* Light grey text when disabled */\n"
"    border: 2px solid #cccccc;  /* Light grey border */\n"
"}\n"
"\n"
"/* Arrow button of the combo box */\n"
"\n"
"\n"
"/* Styling the dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    background-color"
                        ": #ffffff;  /* White background for the dropdown list */\n"
"    color: #333333;  /* Dark text color */\n"
"    border: 1px solid #c0c0c0;  /* Border around the dropdown list */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"/* Hover effect on the dropdown list items */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #2196F3;  /* Blue background on hover */\n"
"    color: #ffffff;  /* White text on hover */\n"
"}\n"
"\n"
"/* Selected item in the dropdown list */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #64B5F6;  /* Light blue background when selected */\n"
"    color: #ffffff;  /* White text when selected */\n"
"}\n"
"")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.staff_dept_box)

        self.staff_sal_box = QLineEdit(self.formFrame_2)
        self.staff_sal_box.setObjectName(u"staff_sal_box")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.staff_sal_box)


        self.horizontalLayout_2.addWidget(self.formFrame_2, 0, Qt.AlignTop)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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

        self.update_btn = QPushButton(self.tab)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setStyleSheet(u"/* Styling the QPushButton */\n"
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

        self.horizontalLayout_3.addWidget(self.update_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Staff ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.staff_category_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Teaching Staff", None))
        self.staff_category_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Non-Teaching Staff", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.staff_gen_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.staff_gen_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DOB", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Contact No.", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.staff_dept_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Primary - 1 to 5", None))
        self.staff_dept_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Middle High - 6 to 8", None))
        self.staff_dept_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Secondary - 9 to 10", None))
        self.staff_dept_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Science", None))
        self.staff_dept_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Commerce", None))
        self.staff_dept_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Humanities", None))
        self.staff_dept_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Utilities", None))
        self.staff_dept_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Lab Assistant", None))
        self.staff_dept_box.setItemText(8, QCoreApplication.translate("MainWindow", u"Finance", None))
        self.staff_dept_box.setItemText(9, QCoreApplication.translate("MainWindow", u"Office", None))

        self.fetch_btn.setText(QCoreApplication.translate("MainWindow", u"Fetch Data", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Edit Staff Details", None))
    # retranslateUi

