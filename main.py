from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer,QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget, QMessageBox,QHeaderView, QTableWidgetItem,QComboBox)


from ui_login import Ui_MainWindow as login
from ui_main import Ui_MainWindow as main
from ui_admission import Ui_MainWindow as admission
from ui_edit_stud import Ui_MainWindow as editstud
from ui_stud_attend import Ui_MainWindow as std_attend
from ui_marksheet import Ui_MainWindow as marksheet
from ui_staff_attend import Ui_MainWindow as staff_attend

from ui_marks import Ui_MainWindow as marks
from ui_staff import Ui_MainWindow as staff
from ui_edit_staff import Ui_MainWindow as editstaff
from ui_stud_fees import Ui_MainWindow as fees

from ui_std_records import Ui_MainWindow as stud_rec
from ui_staff_rec import Ui_MainWindow as staff_rec

import sys
import string
import random
import subprocess
import os
import sqlite3
from docxtpl import DocxTemplate

class AdmissionWindow(QMainWindow):
    def __init__(self):
        super(AdmissionWindow,self).__init__()
        self.ui = admission()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.admission_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.std_id_label.setText("S-"+self.generate_random_string())

        self.ui.save_btn.clicked.connect(self.save_data)
        self.load_data_into_table()
    def generate_random_string(self):
        characters = string.ascii_letters + string.digits  # Include letters and numbers
        return ''.join(random.choice(characters) for _ in range(5)).upper()
    
    def save_data(self):
        # Retrieve data from UI elements
        std_id = self.ui.std_id_label.text()
        first_name = self.ui.std_firstname_box.text()
        last_name = self.ui.std_lastname_box.text()
        fname = self.ui.std_fname_box.text()
        mname = self.ui.std_mname_box.text()
        gender = self.ui.std_gender_box.currentText()
        dob = self.ui.std_dob_box.text()
        address = self.ui.std_address_box.toPlainText()
        contact = self.ui.std_contact_box.text()
        email = self.ui.std_email_box.text()
        standard = self.ui.std_class_box.currentText()
        div = self.ui.std_section_box.currentText()

        # Validate input fields (basic example)
        if not first_name or not last_name or not email or not contact:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")
            return

        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Insert or update the data in the database
            cursor.execute("""
            INSERT INTO students (id, first_name, last_name, fname, mname, gender, dob, address, contact, email, standard, division)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                first_name=excluded.first_name,
                last_name=excluded.last_name,
                fname=excluded.fname,
                mname=excluded.mname,
                gender=excluded.gender,
                dob=excluded.dob,
                address=excluded.address,
                contact=excluded.contact,
                email=excluded.email,
                standard=excluded.standard,
                division=excluded.division
            """, (std_id, first_name, last_name, fname, mname, gender, dob, address, contact, email, standard, div))

            # Commit changes and close the database
            db.commit()
            db.close()

            # Notify the user
            QMessageBox.information(self, "Success", "Student data saved successfully!")
            self.load_data_into_table()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            db.rollback()
            db.close()

    def load_data_into_table(self):
        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to fetch all data from the students table
            cursor.execute("SELECT * FROM students")
            data = cursor.fetchall()  # Fetch all rows

            # Get the column names
            custom_headers = [
            "Student ID", "First Name", "Last Name", "Father's Name",
            "Mother's Name", "Gender", "Date of Birth", "Address",
            "Contact Number", "Email", "Class", "Section"
            ]

            # Set the row and column counts for the QTableWidget
            self.ui.admission_table.setRowCount(len(data))  # Number of rows
            self.ui.admission_table.setColumnCount(len(custom_headers))  # Number of columns
            self.ui.admission_table.setHorizontalHeaderLabels(custom_headers)  # Set custom headers

            # Populate the table with data
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    # Convert data to string and add it to the table widget
                    self.ui.admission_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
 

class EditStudentWindow(QMainWindow):
    def __init__(self):
        super(EditStudentWindow,self).__init__()
        self.ui = editstud()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.std_age_box.setVisible(False)
        self.ui.label_8.setVisible(False)
        self.ui.save_btn.clicked.connect(self.update_data)
        self.ui.fetch_btn.clicked.connect(self.fetch_data)

    def fetch_data(self):
        # Retrieve the Student ID entered by the user (e.g., in a text box)
        std_id = self.ui.std_id_box.text()

        # Validate if Student ID is provided
        if not std_id:
            QMessageBox.warning(self, "Input Error", "Please enter a valid Student ID.")
            return

        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to fetch data from the students table based on the Student ID
            cursor.execute("SELECT * FROM students WHERE id = ?", (std_id,))
            student_data = cursor.fetchone()  # Fetch the first matching row

            # If no record is found, show a message
            if not student_data:
                QMessageBox.warning(self, "No Data", f"No student found with ID {std_id}.")
                db.close()
                return

            # Populate the text fields with the fetched data
            self.ui.std_firstname_box.setText(student_data[1])  # first_name
            self.ui.std_lastname_box.setText(student_data[2])   # last_name
            self.ui.std_fname_box.setText(student_data[3])      # fname
            self.ui.std_mname_box.setText(student_data[4])      # mname
            self.ui.std_gender_box.setCurrentText(student_data[5])  # gender
            self.ui.std_dob_box.setText(student_data[6])        # dob
            self.ui.std_address_box.setPlainText(student_data[7])  # address
            self.ui.std_contact_box.setText(student_data[8])    # contact
            self.ui.std_email_box.setText(student_data[9])      # email
            self.ui.std_class_box.setCurrentText(student_data[10])  # standard
            self.ui.std_section_box.setCurrentText(student_data[11])  # division

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")

    def update_data(self):
        # Retrieve data from UI elements
        std_id = self.ui.std_id_box.text()  # Primary key to identify the record
        first_name = self.ui.std_firstname_box.text()
        last_name = self.ui.std_lastname_box.text()
        fname = self.ui.std_fname_box.text()
        mname = self.ui.std_mname_box.text()
        gender = self.ui.std_gender_box.currentText()
        dob = self.ui.std_dob_box.text()
        address = self.ui.std_address_box.toPlainText()
        contact = self.ui.std_contact_box.text()
        email = self.ui.std_email_box.text()
        standard = self.ui.std_class_box.currentText()
        div = self.ui.std_section_box.currentText()

        # Validate input fields
        if not std_id or not first_name or not last_name:
            QMessageBox.warning(self, "Input Error", "Student ID, First Name, and Last Name are required.")
            return

        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # SQL query to update the data
            cursor.execute("""
            UPDATE students
            SET first_name = ?, last_name = ?, fname = ?, mname = ?, gender = ?, dob = ?, 
                address = ?, contact = ?, email = ?, standard = ?, division = ?
            WHERE id = ?
            """, (first_name, last_name, fname, mname, gender, dob, address, contact, email, standard, div, std_id))

            # Check if any row was updated
            if cursor.rowcount == 0:
                QMessageBox.warning(self, "Update Failed", f"No record found with Student ID {std_id}.")
            else:
                # Commit changes and provide feedback
                db.commit()
                QMessageBox.information(self, "Success", "Student data updated successfully.")

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            db.rollback()
            db.close()

class EditStaffWindow(QMainWindow):
    def __init__(self):
        super(EditStaffWindow,self).__init__()
        self.ui = editstaff()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.fetch_btn.clicked.connect(self.fetch_staff_details)
        self.ui.update_btn.clicked.connect(self.update_staff_details)
    def fetch_staff_details(self):
        # Retrieve the staff ID entered by the user (for example, in a text box)
        staff_id = self.ui.lineEdit.text()


        # Validate if staff ID is provided
        if not staff_id:
            QMessageBox.warning(self, "Input Error", "Please enter a valid Staff ID.")
            return

        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to fetch data from the staff table based on the Staff ID
            cursor.execute("SELECT * FROM staff WHERE staff_id = ?", (staff_id,))
            staff_data = cursor.fetchone()  # Fetch the first matching row

            # If no record is found, show a message
            if not staff_data:
                QMessageBox.warning(self, "No Data", f"No staff found with ID {staff_id}.")
                db.close()
                return

            # Populate the text fields with the fetched data
            self.ui.staff_fname_box.setText(staff_data[2])  # first_name
            self.ui.staff_lname_box.setText(staff_data[3])   # last_name
            self.ui.staff_category_box.setCurrentText(staff_data[1])  # category
            self.ui.staff_gen_box.setCurrentText(staff_data[4])  # gender
            self.ui.staff_dob_box.setText(staff_data[5])        # dob
            self.ui.staff_address_box.setPlainText(staff_data[6])  # address
            self.ui.staff_contact_box.setText(staff_data[7])    # contact
            self.ui.staff_email_box.setText(staff_data[8])      # email
            self.ui.staff_dept_box.setCurrentText(staff_data[9])  # department
            self.ui.staff_sal_box.setText(str(staff_data[10]))  # salary

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")

    def update_staff_details(self):
        # Retrieve data from the UI elements
        staff_id = self.ui.lineEdit.text()  # Staff ID (primary key)
        category = self.ui.staff_category_box.currentText()  # Staff Category
        first_name = self.ui.staff_fname_box.text()  # First Name
        last_name = self.ui.staff_lname_box.text()  # Last Name
        gender = self.ui.staff_gen_box.currentText()  # Gender
        dob = self.ui.staff_dob_box.text()  # Date of Birth
        address = self.ui.staff_address_box.toPlainText()  # Address
        contact = self.ui.staff_contact_box.text()  # Contact Number
        email = self.ui.staff_email_box.text()  # Email
        dept = self.ui.staff_dept_box.currentText()  # Department
        salary = self.ui.staff_sal_box.text()  # Salary

        # Validate required fields
        if not staff_id or not first_name or not last_name or not contact or not email:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")
            return

        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # SQL query to update the staff details in the staff table
            cursor.execute("""
            UPDATE staff
            SET category = ?, first_name = ?, last_name = ?, gender = ?, dob = ?, 
                address = ?, contact = ?, email = ?, department = ?, salary = ?
            WHERE staff_id = ?
            """, (category, first_name, last_name, gender, dob, address, contact, email, dept, salary, staff_id))

            # Check if any row was updated
            if cursor.rowcount == 0:
                QMessageBox.warning(self, "Update Failed", f"No record found with Staff ID {staff_id}.")
            else:
                # Commit the changes and provide feedback
                db.commit()
                QMessageBox.information(self, "Success", "Staff details updated successfully.")

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            db.rollback()
            db.close()


class FeesWindow(QMainWindow):
    def __init__(self):
        super(FeesWindow,self).__init__()
        self.ui = fees()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.fees_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.entry_btn.setVisible(False)
        self.load_fees_data()
        self.ui.save_btn.clicked.connect(self.save_fees)
        self.ui.fetch_btn.clicked.connect(self.fetch_fees_data)


    def fetch_fees_data(self):
        try:
            # Retrieve the student ID entered by the user
            std_id = self.ui.fees_id_box.text()

            # Validate the student ID input
            if not std_id:
                QMessageBox.warning(self, "Input Error", "Please enter a Student ID to fetch fees.")
                return

            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to fetch fee records for the given student ID
            cursor.execute("""
                SELECT f.std_id, s.id AS std_id, s.first_name, s.last_name, f.amount, f.fee_date
                FROM fees f
                JOIN students s ON f.std_id = s.id
                WHERE f.std_id = ?
            """, (std_id,))
            
            data = cursor.fetchall()  # Fetch all rows

            # Check if data is returned
            if not data:
                QMessageBox.warning(self, "No Data", f"No fee records found for Student ID {std_id}.")
                db.close()
                return

            # Define custom column headers
            custom_headers = [
                "Fee ID", "Student ID", "First Name", "Last Name", "Amount", "Fee Date"
            ]

            # Set the row and column counts for the QTableWidget
            self.ui.fees_table.setRowCount(len(data))  # Number of rows
            self.ui.fees_table.setColumnCount(len(custom_headers))  # Number of columns
            self.ui.fees_table.setHorizontalHeaderLabels(custom_headers)  # Set custom headers

            # Populate the table with fee data
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    # Convert data to string and add it to the table widget
                    self.ui.fees_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            # Handle any database errors
            print(f"Database error: {e}")
            QMessageBox.critical(self, "Database Error", f"An error occurred while fetching fee data: {e}")


    def save_fees(self):
        try:
            # Retrieve the inputs
            std_id = self.ui.fees_id_box.text()
            amt = self.ui.lineEdit.text()
            date = QDate.currentDate().toString("dd-MM-yyyy")  # Current date in the format "dd-MM-yyyy"
            
            # Validate inputs
            if not std_id or not amt or not date:
                QMessageBox.warning(self, "Input Error", "Please fill in all the fields.")
                return
            
            if not amt.isdigit():
                QMessageBox.warning(self, "Input Error", "Please enter a valid fee amount.")
                return

            # Connect to the database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to check if the student ID exists
            cursor.execute("SELECT * FROM students WHERE id=?", (std_id,))
            student = cursor.fetchone()

            if not student:
                QMessageBox.warning(self, "Invalid Student", f"No student found with ID {std_id}.")
                db.close()
                return

            # Insert the fee data into the fees table
            cursor.execute("""
                INSERT INTO fees (std_id, amount, fee_date)
                VALUES (?, ?, ?)
            """, (std_id, amt, date))

            # Commit the changes to the database
            db.commit()

            # Show a success message
            QMessageBox.information(self, "Success", "Fee record saved successfully.")

            # Clear the input fields after saving the data
            self.ui.fees_id_box.clear()
            self.ui.lineEdit.clear()

            # Close the database connection
            db.close()
            self.load_fees_data()

        except sqlite3.Error as e:
            # Handle any database errors
            print(f"Database error: {e}")
            QMessageBox.critical(self, "Database Error", f"An error occurred while saving the fee: {e}")

    def load_fees_data(self):
        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to fetch all fee records
            cursor.execute("SELECT f.std_id, s.id AS std_id, s.first_name, s.last_name, f.amount, f.fee_date "
                        "FROM fees f "
                        "JOIN students s ON f.std_id = s.id")
            data = cursor.fetchall()  # Fetch all rows

            # Check if data is returned
            if not data:
                QMessageBox.warning(self, "No Data", "No fee records found.")
                db.close()
                return

            # Define custom column headers
            custom_headers = [
                "Fee ID", "Student ID", "First Name", "Last Name", "Amount", "Fee Date"
            ]

            # Set the row and column counts for the QTableWidget
            self.ui.fees_table.setRowCount(len(data))  # Number of rows
            self.ui.fees_table.setColumnCount(len(custom_headers))  # Number of columns
            self.ui.fees_table.setHorizontalHeaderLabels(custom_headers)  # Set custom headers

            # Populate the table with fee data
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    # Convert data to string and add it to the table widget
                    self.ui.fees_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            # Handle any database errors
            print(f"Database error: {e}")
            QMessageBox.critical(self, "Database Error", f"An error occurred while fetching fee data: {e}")

class StudentRecWindow(QMainWindow):
    def __init__(self):
        super(StudentRecWindow,self).__init__()
        self.ui = stud_rec()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.std_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.fetch_btn.clicked.connect(self.load_data_into_table)
        self.load_data_into_table()
        
        
    def load_data_into_table(self):
        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()
            
            # Get values entered by the user
            std_id = self.ui.std_id_box.text()
            std_class = self.ui.std_class_box.currentText()
            std_div = self.ui.std_section_box.currentText()

            # Handle the case when no filters are provided
            if not std_id :
                std_id = 'None'
            
            # Construct the WHERE clause dynamically based on the available filters
            
            cursor.execute('SELECT * FROM students WHERE id=? OR standard=? AND division=?', (std_id,std_class,std_div) )
            data = cursor.fetchall()  # Fetch all rows

            # Check if any data was returned
            if not data:
                QMessageBox.warning(self, "No Data", "No student found matching the given criteria.")
                db.close()
                return

            # Define custom column headers
            custom_headers = [
                "Student ID", "First Name", "Last Name", "Father's Name",
                "Mother's Name", "Gender", "Date of Birth", "Address",
                "Contact Number", "Email", "Class", "Section"
                ]

            # Set the row and column counts for the QTableWidget
            self.ui.std_table.setRowCount(len(data))  # Number of rows
            self.ui.std_table.setColumnCount(len(custom_headers))  # Number of columns
            self.ui.std_table.setHorizontalHeaderLabels(custom_headers)  # Set custom headers

            # Populate the table with data
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    # Convert data to string and add it to the table widget
                    self.ui.std_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            # Handle any database errors
            print(f"Database error: {e}")
            QMessageBox.critical(self, "Database Error", f"An error occurred while fetching data: {e}")

class StaffRecWindow(QMainWindow):
    def __init__(self):
        super(StaffRecWindow,self).__init__()
        self.ui = staff_rec()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.staff_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.load_data_into_table()
        self.ui.fetch_btn.clicked.connect(self.load_data_into_table)
    def load_data_into_table(self):
        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()
            
            # Get the values entered by the user
            staff_id = self.ui.staff_id_box.text()
            staff_dept = self.ui.staff_dept_box.currentText()

            # Handle case where both filters are empty
            if not staff_id:
                staff_id='None'
            
            # If staff_id is provided, filter by staff_id, otherwise filter by department
            cursor.execute("SELECT * FROM staff WHERE (staff_id = ? OR department = ?) ", (staff_id, staff_dept))
            

            data = cursor.fetchall()  # Fetch all rows from the query

            # If no data is returned, show a message
            if not data:
                QMessageBox.warning(self, "No Data", "No staff found matching the given criteria.")
                db.close()
                return

            # Get the column names for header
            headers = ["Staff ID", "Category", "First Name", "Last Name", "Gender", "DOB", 
                    "Address", "Contact", "Email", "Department", "Salary"]

            # Set the row and column counts for the QTableWidget
            self.ui.staff_table.setRowCount(len(data))  # Number of rows
            self.ui.staff_table.setColumnCount(len(headers))  # Number of columns
            self.ui.staff_table.setHorizontalHeaderLabels(headers)  # Set custom headers

            # Populate the table with the data
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    # Convert data to string and add it to the table widget
                    self.ui.staff_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Resize the columns to fit the content

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while fetching data: {e}")

class MarksheetWindow(QMainWindow):
    def __init__(self):
        super(MarksheetWindow, self).__init__()

        self.ui = marksheet()  # Assuming marksheet is the UI class generated by pyuic
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.ui.std_marks_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.details = {}
        # Connect fetch button to function
        self.ui.fetch_btn.clicked.connect(self.fetch_marks)
        self.ui.print_btn.clicked.connect(self.print_marksheet)
        
    def fetch_marks(self):
        """Fetch marks for a student and populate the list view with student details and the table with marks."""
        try:
            std_id = self.ui.std_id_box.text()  # Get student ID from input field or combo box
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()

            # Fetch student details
            cursor.execute('''
                SELECT first_name || ' ' || last_name, standard, division,dob,fname,mname
                FROM students
                WHERE id = ?
            ''', (std_id,))
            student_details = cursor.fetchone()

            if student_details:
                # Extract details from fetched data
                student_name, student_class, student_section, dob, fname, mname = student_details
                student_info = [
                    f"Student ID: {std_id}",
                    f"Student Name: {student_name}",
                    f"Class: {student_class}",
                    f"Section: {student_section}"
                ]

                # Assuming `std_details_box` is a QListWidget
                self.ui.std_details_box.clear()  # Clear the list widget first
                self.ui.std_details_box.addItems(student_info)  # Add student details to the list widget

                # Fetch marks for the student
                cursor.execute('''
                    SELECT subject_name, theory_marks, assignment_marks
                    FROM marks
                    WHERE std_id = ?
                ''', (std_id,))
                records = cursor.fetchall()
                
                # Clear the previous data from the table
                self.ui.std_marks_table.setRowCount(0)

                # Populate the table with fetched data
                self.ui.std_marks_table.setRowCount(len(records))
                self.ui.std_marks_table.setColumnCount(3)  # 4 columns: Subject, Theory Marks, Assignment Marks
                self.ui.std_marks_table.setHorizontalHeaderLabels(["Subject", "Theory Marks", "Assignment Marks"])
                marks = []
                # Populate table with data
                for row, record in enumerate(records):
                    self.ui.std_marks_table.setItem(row, 0, QTableWidgetItem(record[0]))  # Subject Name
                    self.ui.std_marks_table.setItem(row, 1, QTableWidgetItem(str(record[1])))  # Theory Marks
                    self.ui.std_marks_table.setItem(row, 2, QTableWidgetItem(str(record[2])))  # Assignment Marks
                    
                                
                total_marks_obtained = 0  # Total obtained marks across all subjects
                total_max_marks = 0       # Total maximum marks across all subjects
                marks = []                # List to store individual subject marks and grades

                for record in records:
                    subject_name = record[0]
                    theory_marks = record[1]
                    theory_max = 70
                    assignment_marks = record[2]
                    assignment_max = 30
                    total_subject_marks = theory_marks + assignment_marks
                    max_subject_marks = theory_max + assignment_max

                    # Add to cumulative totals
                    total_marks_obtained += total_subject_marks
                    total_max_marks += max_subject_marks

                    # Append subject-specific details with grade
                    marks.append([
                        subject_name,                     # Subject Name
                        theory_marks,                     # Theory Marks
                        theory_max,                       # Total Theory Marks
                        assignment_marks,                 # Assignment Marks
                        assignment_max,                   # Total Assignment Marks
                        total_subject_marks,              # Total Obtained Marks (Theory + Assignment)
                        self.assign_grade(total_subject_marks)  # Grade for the subject
                    ])

                # Calculate overall percentage and grade
                percentage = round((total_marks_obtained / total_max_marks) * 100,2)
                final_grade = self.assign_grade(total_marks_obtained / len(records))  # Average grade
                result = "Pass" if percentage >= 35 else "Fail"
                self.details = {"name":student_name,
                                "fname":fname,
                                "mname":mname,
                                "id":std_id,
                                "class":student_class,
                                "sec":student_section,
                                "dob":dob,
                                "marks":marks,
                                "total": total_marks_obtained,
                                "per":percentage,
                                "grade":final_grade,
                                "result":result
                                }

                return self.details
            else:
                QMessageBox.warning(self, "No Student Found", "Student ID not found!")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")
            
    def assign_grade(self, total_marks):
        """Assign a grade based on total obtained marks."""
        if total_marks >= 90:
            return 'A+'
        elif 80 <= total_marks < 90:
            return 'A'
        elif 70 <= total_marks < 80:
            return 'B'
        elif 60 <= total_marks < 70:
            return 'C'
        elif 50 <= total_marks < 60:
            return 'D'
        elif 35 <= total_marks < 50:
            return 'E'
        else:
            return 'Fail'

    def generate_marksheet(self):
        """Generate a marksheet using docxtpl and save it."""
        try:
            # Load the Word template
            doc = DocxTemplate("report.docx")

            # Prepare context (data to fill in the template)
            context = {
                'name': self.details['name'],
                'fname': self.details['fname'],
                'mname': self.details['mname'],
                'std_id': self.details['id'],
                'std': self.details['class'],
                'div': self.details['sec'],
                'marks': self.details['marks'],
                'per':self.details['per'],
                'result':self.details['result'] + " " + self.details['grade'] ,
                'total':self.details['total']
                
            }

            # Render the template with the student data
            doc.render(context)

            # Save the generated marksheet
            file_name = f"report_card/marksheet_{self.details['id']}.docx"
            doc.save(file_name)

            return file_name

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating marksheet: {e}")
    
    def print_marksheet(self):
        """Print the marksheet for the selected student."""
        student_id = self.ui.std_id_box.text()  # Assume the student ID is entered in a text box

        if not student_id:
            QMessageBox.warning(self, "Input Error", "Please enter a valid student ID.")
            return

        # Fetch student data
        student_data = self.fetch_marks()
        if not student_data:
            return  # Student not found

        # Generate the marksheet
        file_name = self.generate_marksheet()

        if file_name:
            QMessageBox.information(self, "Success", f"Marksheets have been generated and saved as {file_name}")
            try:
                subprocess.Popen(['start', file_name], shell=True)
            except Exception as e:
                print(f"Error: {e}")
            except FileNotFoundError:
                print("The specified application or file was not found.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred: {e}")
        else:
            QMessageBox.critical(self, "Error", "Error generating the marksheet.")

class MarksWindow(QMainWindow):
    def __init__(self):
        super(MarksWindow, self).__init__()
        self.ui = marks()  # Assuming marks() is your form's UI class
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.sub_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.sub_table.setRowCount(0)
        custom_headers = ["Subject","Theory","Practical"]

        # Set the row and column counts for the QTableWidget
        self.ui.sub_table.setColumnCount(len(custom_headers))  # Number of columns
        self.ui.sub_table.setHorizontalHeaderLabels(custom_headers)  # Set custom headers

        # Connect buttons to functions
        self.ui.sub_btn.clicked.connect(self.publish_marks)
        self.ui.save_btn.clicked.connect(self.save_marks)
        self.ui.fetch_btn.clicked.connect(self.fetch_marks)

    def publish_marks(self):
        """Publish entered subject marks to the table widget."""
        try:
            # Get input values from UI elements
            std_id = self.ui.std_id_box.text()  # Student ID input field
            subject_name = self.ui.sub_name.text()  # Subject Name combo box
            theory_marks = self.ui.sub_m1_box.text()  # Theory Marks spinner
            assignment_marks = self.ui.sub_m2_box.text()  # Assignment Marks spinner

            # Add the entered details into the table widget
            row_position = self.ui.sub_table.rowCount()
            self.ui.sub_table.insertRow(row_position)

            # Set the values into the table cells
            self.ui.sub_table.setItem(row_position, 0, QTableWidgetItem(subject_name))  # Subject Name
            self.ui.sub_table.setItem(row_position, 1, QTableWidgetItem(str(theory_marks)))  # Theory Marks
            self.ui.sub_table.setItem(row_position, 2, QTableWidgetItem(str(assignment_marks)))  # Assignment Marks

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while publishing marks: {e}")

    def save_marks(self):
        """Save or update marks for a student."""
        try:
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()

            std_id = self.ui.std_id_box.text()  # Get the student ID from input field

            # Loop through each row in the table and update or insert marks
            for row in range(self.ui.sub_table.rowCount()):
                subject_name = self.ui.sub_table.item(row, 0).text()  # Subject
                theory_marks = self.ui.sub_table.item(row, 1).text()  # Theory Marks
                assignment_marks = self.ui.sub_table.item(row, 2).text()  # Assignment Marks

                # Check if the record already exists in the database
                cursor.execute('''
                    SELECT COUNT(*) FROM marks
                    WHERE std_id = ? AND subject_name = ?
                ''', (std_id, subject_name))
                exists = cursor.fetchone()[0]

                if exists > 0:
                    # If the record exists, update the marks
                    cursor.execute('''
                        UPDATE marks
                        SET theory_marks = ?, assignment_marks = ?
                        WHERE std_id = ? AND subject_name = ?
                    ''', (theory_marks, assignment_marks, std_id, subject_name))
                else:
                    # If the record does not exist, insert a new record
                    cursor.execute('''
                        INSERT INTO marks (std_id, subject_name, theory_marks, assignment_marks)
                        VALUES (?, ?, ?, ?)
                    ''', (std_id, subject_name, theory_marks, assignment_marks))

            db.commit()  # Commit the changes to the database
            QMessageBox.information(self, "Success", "Marks saved successfully!")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def fetch_marks(self):
        """Fetch marks for a student and populate the table."""
        try:
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()

            std_id = self.ui.std_id_box.text()  # Get the student ID from input field
            cursor.execute('''
                SELECT std_id, subject_name, theory_marks, assignment_marks
                FROM marks
                WHERE std_id = ?
            ''', (std_id,))
            records = cursor.fetchall()

            # Populate the table widget with fetched data
            self.ui.sub_table.setRowCount(len(records))
            for row, record in enumerate(records):
                self.ui.sub_table.setItem(row, 0, QTableWidgetItem(str(record[1])))  # Subject
                self.ui.sub_table.setItem(row, 1, QTableWidgetItem(str(record[2])))  # Theory Marks
                self.ui.sub_table.setItem(row, 2, QTableWidgetItem(str(record[3])))  # Assignment Marks

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

class StudentAttendanceWindow(QMainWindow):
    def __init__(self):
        super(StudentAttendanceWindow, self).__init__()
        self.ui = std_attend()  # Assuming std_attend() is your form's class
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.std_attend_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Connect buttons to functions
        self.ui.fetch_btn.clicked.connect(self.load_students_for_attendance)
        self.ui.save_btn.clicked.connect(self.save_attendance)
        
        self.ui.std_attend_table.setColumnCount(4)  # Columns: Student ID, Name, Class, Status
        self.ui.std_attend_table.setHorizontalHeaderLabels(["Student ID", "Name", "Class", "Status"])

    def check_attendance_exists(self, selected_date, standard, division):
        # Check if attendance exists for the selected date, class, and division
        cursor = sqlite3.connect('database/school.db').cursor()
        cursor.execute(''' 
            SELECT COUNT(*) FROM attendance
            WHERE date = ? AND standard = ? AND division = ? 
        ''', (selected_date, standard, division))
        result = cursor.fetchone()
        return result[0] > 0  # Returns True if attendance data exists, False otherwise

    def load_students_for_attendance(self):
        try:
            selected_date = self.ui.std_calender_box.selectedDate().toString("yyyy-MM-dd")
            standard = self.ui.std_class_box.currentText()
            division = self.ui.std_section_box.currentText()

            # Check if attendance exists
            if not self.check_attendance_exists(selected_date, standard, division):
                # Fetch students for the given class and division
                db = sqlite3.connect('database/school.db')
                cursor = db.cursor()
                cursor.execute('''
                    SELECT id, first_name || ' ' || last_name, standard, division
                    FROM students
                    WHERE standard = ? AND division = ?
                ''', (standard, division))
                students = cursor.fetchall()

                # Populate TableWidget with student details and default status
                self.populate_attendance_table_with_default_status(students, selected_date, standard, division)
            else:
                # Fetch and display the existing attendance
                self.fetch_attendance()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def populate_attendance_table_with_default_status(self, students, selected_date, standard, division):
        # Populate the attendance table with the students' information
        self.ui.std_attend_table.setRowCount(len(students))
        self.ui.std_attend_table.setColumnCount(4)  # Student ID, Name, Class, Status
        self.ui.std_attend_table.setHorizontalHeaderLabels(["Student ID", "Name", "Class", "Status"])

        for row, student in enumerate(students):
            self.ui.std_attend_table.setItem(row, 0, QTableWidgetItem(student[0]))  # Student ID
            self.ui.std_attend_table.setItem(row, 1, QTableWidgetItem(student[1]))  # Name
            self.ui.std_attend_table.setItem(row, 2, QTableWidgetItem(f"{student[2]} - {student[3]}"))  # Class - Division

            # Default attendance status is "Absent"
            combo = QComboBox()
            combo.addItems(["Present", "Absent", "Late", "Excused"])
            combo.setCurrentText("Absent")  # Default status
            self.ui.std_attend_table.setCellWidget(row, 3, combo)

        # Add default attendance entries to the database
        self.save_default_attendance(selected_date, students, standard, division)

    def save_default_attendance(self, selected_date, students, standard, division):
        try:
            # Save default attendance status for each student
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()
            for student in students:
                std_id = student[0]  # Student ID
                status = "Absent"  # Default status

                cursor.execute('''
                    INSERT INTO attendance (std_id, date, status, standard, division)
                    VALUES (?, ?, ?, ?, ?)
                ''', (std_id, selected_date, status, standard, division))

            db.commit()  # Commit the changes
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def fetch_attendance(self):
        try:
            selected_date = self.ui.std_calender_box.selectedDate().toString("yyyy-MM-dd")
            standard = self.ui.std_class_box.currentText()
            division = self.ui.std_section_box.currentText()
            
            # Connect to the database
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()

            # Fetch attendance data from the database
            cursor.execute('''
                SELECT a.std_id, s.first_name || ' ' || s.last_name AS full_name, 
                    a.standard, a.division, a.status
                FROM attendance a
                JOIN students s ON a.std_id = s.id
                WHERE a.date = ? AND a.standard = ? AND a.division = ?
            ''', (selected_date, standard, division))

            records = cursor.fetchall()

            # Set up the table widget: setting rows and columns dynamically based on the fetched data
            self.ui.std_attend_table.setRowCount(len(records))
            self.ui.std_attend_table.setColumnCount(4)  # Columns: Student ID, Name, Class, Status
            self.ui.std_attend_table.setHorizontalHeaderLabels(["Student ID", "Name", "Class", "Status"])

            # Loop through the fetched records and populate the table
            for row, record in enumerate(records):
                # Add student data to the first three columns
                self.set_student_data(row, record)

                # Add a combo box for the attendance status in the last column
                self.set_attendance_status(row, record[4])

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")


    def set_student_data(self, row, record):
        """
        Set student information (ID, Name, Class) in the table.
        """
        # Student ID
        self.ui.std_attend_table.setItem(row, 0, QTableWidgetItem(str(record[0])))

        # Student Name
        self.ui.std_attend_table.setItem(row, 1, QTableWidgetItem(str(record[1])))

        # Class and Division (Standard and Division)
        self.ui.std_attend_table.setItem(row, 2, QTableWidgetItem(f"{record[2]} - {record[3]}"))


    def set_attendance_status(self, row, status):
        """
        Set attendance status using a combo box.
        """
        # Create combo box for attendance status
        combo = QComboBox()
        combo.addItems(["Present", "Absent", "Late", "Excused"])

        # Set the current status from the database
        combo.setCurrentText(status)  # Set the current status based on the fetched record

        # Add the combo box to the last column (Status column)
        self.ui.std_attend_table.setCellWidget(row, 3, combo)


    def save_attendance(self):
        try:
            selected_date = self.ui.std_calender_box.selectedDate().toString("yyyy-MM-dd")
            standard = self.ui.std_class_box.currentText()
            division = self.ui.std_section_box.currentText()
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()

            for row in range(self.ui.std_attend_table.rowCount()):
                std_id = self.ui.std_attend_table.item(row, 0).text()  # Student ID
                status = self.ui.std_attend_table.cellWidget(row, 3).currentText()  # Attendance Status
                
                # Check if attendance for this student and date already exists in the DB
                cursor.execute('''
                    SELECT COUNT(*) FROM attendance
                    WHERE std_id = ? AND date = ? AND standard = ? AND division = ?
                ''', (std_id, selected_date, standard, division))
                exists = cursor.fetchone()[0]

                if exists:
                    # If attendance exists, update it
                    cursor.execute('''
                        UPDATE attendance
                        SET status = ?
                        WHERE std_id = ? AND date = ? AND standard = ? AND division = ?
                    ''', (status, std_id, selected_date, standard, division))
                else:
                    # If attendance doesn't exist, insert a new record
                    cursor.execute('''
                        INSERT INTO attendance (std_id, date, status, standard, division)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (std_id, selected_date, status, standard, division))

            db.commit()  # Commit the changes
            QMessageBox.information(self, "Success", "Attendance saved successfully!")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")
            
class StaffWindow(QMainWindow):
    def __init__(self):
        super(StaffWindow,self).__init__()
        self.ui = staff()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.staff_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.staff_id_label.setText("T-"+self.generate_random_string())
        self.ui.staff_category_box.currentIndexChanged.connect(self.ToggleFunc)

        self.ui.save_btn.clicked.connect(self.save_details)
        self.load_data_into_table()

    def ToggleFunc(self,x):
        if x == 0:
            self.ui.staff_id_label.setText("T-"+self.generate_random_string())
        else:
            self.ui.staff_id_label.setText("NT-"+self.generate_random_string())
        

    def generate_random_string(self):
        characters = string.ascii_letters + string.digits  # Include letters and numbers
        return ''.join(random.choice(characters) for _ in range(5)).upper()
    
    def save_details(self):
        # Retrieve data from the UI elements
        staff_id = self.ui.staff_id_label.text()  # Staff ID
        category = self.ui.staff_category_box.currentText()  # Staff Category
        first_name = self.ui.staff_fname_box.text()  # First Name
        last_name = self.ui.staff_lname_box.text()  # Last Name
        gender = self.ui.staff_gen_box.currentText()  # Gender
        dob = self.ui.staff_dob_box.text()  # Date of Birth
        address = self.ui.staff_address_box.toPlainText()  # Address
        contact = self.ui.staff_contact_box.text()  # Contact Number
        email = self.ui.staff_email_box.text()  # Email
        dept = self.ui.staff_dept_box.currentText()  # Department
        salary = self.ui.staff_sal_box.text()  # Salary

        # Validate required fields
        if not staff_id or not first_name or not last_name or not contact or not email:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")
            return

        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # SQL query to insert the staff details into the staff table
            cursor.execute("""
            INSERT INTO staff (staff_id, category, first_name, last_name, gender, dob, 
                            address, contact, email, department, salary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (staff_id, category, first_name, last_name, gender, dob, address, contact, email, dept, salary))

            # Commit the changes
            db.commit()

            # Provide feedback to the user
            QMessageBox.information(self, "Success", "Staff details saved successfully.")

            # Close the database connection
            db.close()
            self.load_data_into_table()

        except sqlite3.Error as e:
            # Handle any database errors
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")

    def load_data_into_table(self):
        try:
            # Connect to the SQLite database
            db = sqlite3.connect("database/school.db")
            cursor = db.cursor()

            # Query to fetch all data from the students table
            cursor.execute("SELECT * FROM staff")
            data = cursor.fetchall()  # Fetch all rows

            # Get the column names
            headers = ["Staff ID", "Category", "First Name", "Last Name", "Gender", "DOB", 
               "Address", "Contact", "Email", "Department", "Salary"]

            # Set the row and column counts for the QTableWidget
            self.ui.staff_table.setRowCount(len(data))  # Number of rows
            self.ui.staff_table.setColumnCount(len(headers))  # Number of columns
            self.ui.staff_table.setHorizontalHeaderLabels(headers)  # Set custom headers

            # Populate the table with data
            for row_index, row_data in enumerate(data):
                for col_index, col_data in enumerate(row_data):
                    # Convert data to string and add it to the table widget
                    self.ui.staff_table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

            # Close the database connection
            db.close()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
 

class StaffAttendanceWindow(QMainWindow):
    def __init__(self):
        super(StaffAttendanceWindow, self).__init__()
        self.ui = staff_attend()  # Assuming staff_attend() is your form's class
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ui.staff_attend_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Connect buttons to functions
        self.ui.fetch_btn.clicked.connect(self.load_staff_for_attendance)
        self.ui.save_btn.clicked.connect(self.save_attendance)

    def check_staff_attendance_exists(self, selected_date, department):
        # Check if staff attendance exists for the selected date and department
        cursor = sqlite3.connect('database/school.db').cursor()
        cursor.execute('''
            SELECT COUNT(*) FROM staff_attendance
            WHERE date = ? AND department = ?
        ''', (selected_date, department))
        result = cursor.fetchone()
        return result[0] > 0  # Returns True if attendance data exists, False otherwise

    def load_staff_for_attendance(self):
        try:
            selected_date = self.ui.staff_calender_box.selectedDate().toString("yyyy-MM-dd")
            department = self.ui.staff_dept_box.currentText()

            # Check if attendance exists for the selected date and department
            if not self.check_staff_attendance_exists(selected_date, department):
                # Fetch staff members from the selected department
                db = sqlite3.connect('database/school.db')
                cursor = db.cursor()
                cursor.execute('''
                    SELECT staff_id, first_name || ' ' || last_name, department
                    FROM staff
                    WHERE department = ?
                ''', (department,))
                staff_members = cursor.fetchall()

                # Populate TableWidget with staff details and default status
                self.populate_staff_attendance_table_with_default_status(staff_members, selected_date, department)
            else:
                # Fetch and display the existing staff attendance
                self.fetch_staff_attendance()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def populate_staff_attendance_table_with_default_status(self, staff_members, selected_date, department):
        # Populate the attendance table with the staff members' information
        self.ui.staff_attend_table.setRowCount(len(staff_members))
        self.ui.staff_attend_table.setColumnCount(4)  # Staff ID, Name, Department, Status
        self.ui.staff_attend_table.setHorizontalHeaderLabels(["Staff ID", "Name", "Department", "Status"])

        for row, staff in enumerate(staff_members):
            self.ui.staff_attend_table.setItem(row, 0, QTableWidgetItem(str(staff[0])))  # Staff ID
            self.ui.staff_attend_table.setItem(row, 1, QTableWidgetItem(staff[1]))  # Name
            self.ui.staff_attend_table.setItem(row, 2, QTableWidgetItem(staff[2]))  # Department

            # Default attendance status is "Absent"
            combo = QComboBox()
            combo.addItems(["Present", "Absent", "Late", "Excused"])
            combo.setCurrentText("Absent")  # Default status
            self.ui.staff_attend_table.setCellWidget(row, 3, combo)

        # Add default attendance entries to the database
        self.save_default_staff_attendance(selected_date, staff_members, department)

    def save_default_staff_attendance(self, selected_date, staff_members, department):
        try:
            # Save default attendance status for each staff member
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()
            for staff in staff_members:
                staff_id = staff[0]  # Staff ID
                status = "Absent"  # Default status

                cursor.execute('''
                    INSERT INTO staff_attendance (staff_id, date, status, department)
                    VALUES (?, ?, ?, ?)
                ''', (staff_id, selected_date, status, department))

            db.commit()  # Commit the changes
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def fetch_staff_attendance(self):
        try:
            selected_date = self.ui.staff_calender_box.selectedDate().toString("yyyy-MM-dd")
            department = self.ui.staff_dept_box.currentText()
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()
            cursor.execute('''
                SELECT sa.staff_id, s.first_name || ' ' || s.last_name AS full_name, 
                       sa.department, sa.status
                FROM staff_attendance sa
                JOIN staff s ON sa.staff_id = s.staff_id
                WHERE sa.date = ? AND sa.department = ?
            ''', (selected_date, department))
            records = cursor.fetchall()

            # Populate TableWidget with staff attendance data
            self.ui.staff_attend_table.setRowCount(len(records))
            for row, record in enumerate(records):
                for col, data in enumerate(record):
                    if col != 3:  # Attendance status (column 3) will have a combo box
                        self.ui.staff_attend_table.setItem(row, col, QTableWidgetItem(str(data)))
                    else:
                        # Add combo box for attendance status
                        combo = QComboBox()
                        combo.addItems(["Present", "Absent", "Late", "Excused"])
                        combo.setCurrentText(data)  # Set the current status from the DB
                        self.ui.staff_attend_table.setCellWidget(row, col, combo)

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def save_attendance(self):
        try:
            selected_date = self.ui.staff_calender_box.selectedDate().toString("yyyy-MM-dd")
            department = self.ui.staff_dept_box.currentText()
            db = sqlite3.connect('database/school.db')
            cursor = db.cursor()
            for row in range(self.ui.staff_attend_table.rowCount()):
                staff_id = self.ui.staff_attend_table.item(row, 0).text()  # Staff ID
                status = self.ui.staff_attend_table.cellWidget(row, 3).currentText()  # Attendance Status

                # Update attendance status in the database
                cursor.execute('''
                    UPDATE staff_attendance
                    SET status = ?
                    WHERE staff_id = ? AND date = ? AND department = ?
                ''', (status, staff_id, selected_date, department))

            db.commit()  # Commit the changes
            QMessageBox.information(self, "Success", "Attendance saved successfully!")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.ui = login()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.show()
        self.ui.username_box.returnPressed.connect(self.ui.password_box.setFocus)
        self.ui.password_box.returnPressed.connect(self.loginFunction)


        self.conn = sqlite3.connect("database/school.db")
        self.cursor = self.conn.cursor()

        self.ui.login_btn.clicked.connect(self.loginFunction)

    def loginFunction(self):
        username = self.ui.username_box.text()
        password = self.ui.password_box.text()

        self.cursor.execute("""
                SELECT password FROM users WHERE username = ?
                    """, (username,))
        result = self.cursor.fetchone()

        if result:
            password_g = result[0]
            # Verify the entered password against the stored hash
            if password_g == password:
                QMessageBox.information(self, "Login Successful", "Welcome!")
                self.ui.username_box.clear()
                self.ui.password_box.clear()
                self.close()
                self.conn.close()
                mainApp.showFullScreen()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
        else:
            QMessageBox.warning(self, "Login Failed", "No Username Found")
        

    def mousePressEvent(self, event: QMouseEvent):
        """Store the position when the mouse is pressed."""
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition()

    def mouseMoveEvent(self, event: QMouseEvent):
        """Enable dragging the frameless window."""
        if self.old_pos is not None:
            delta = event.globalPosition() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition()

    def mouseReleaseEvent(self, event: QMouseEvent):
        """Reset the position after releasing the mouse."""
        if event.button() == Qt.LeftButton:
            self.old_pos = None


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = main()
        self.ui.setupUi(self)
        self.windows = {}
        self.ui.logout_btn.clicked.connect(lambda : (mainApp.close(),loginApp.show()))
        self.ui.minimize_btn.clicked.connect(lambda : mainApp.showMinimized())
        self.ui.exit_btn.clicked.connect(lambda : mainApp.close())
        

        
        self.ui.admission_btn.clicked.connect(lambda: self.show_window("admission", AdmissionWindow))
        self.ui.edit_btn.clicked.connect(lambda: self.show_window("edit_student", EditStudentWindow))
        self.ui.marksheet_btn.clicked.connect(lambda: self.show_window("marksheet", MarksheetWindow))
        self.ui.marks_btn.clicked.connect(lambda: self.show_window("marks", MarksWindow))
        self.ui.student_attend_btn.clicked.connect(lambda: self.show_window("student_attendance", StudentAttendanceWindow))
        self.ui.staff_attend_btn.clicked.connect(lambda: self.show_window("staff_attendance", StaffAttendanceWindow))
        self.ui.teache_btn.clicked.connect(lambda: self.show_window("staff", StaffWindow))
        self.ui.edit_staff_btn.clicked.connect(lambda: self.show_window("edit_staff", EditStaffWindow))
        self.ui.fees_btn.clicked.connect(lambda: self.show_window("fees",FeesWindow))
        self.ui.std_rec_btn.clicked.connect(lambda: self.show_window("stud_rec",StudentRecWindow))
        self.ui.staff_rec_btn.clicked.connect(lambda: self.show_window("staff_rec",StaffRecWindow))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time_date)
        self.timer.start(1000)  # Update every 1000ms (1 second)

        # Initialize the display
        self.update_time_date()
        

    def update_time_date(self):
        # Get the current time and date
        current_time = QDateTime.currentDateTime()

        # Format time and date
        time_text = current_time.toString("hh:mm:ss AP")  # 12-hour format with AM/PM
        date_text = current_time.toString("dd/MM/yyyy")  # Full date format

        # Update the labels
        self.ui.date_label.setText("Date: "+ date_text+"  \nTime: "+time_text+"")

    def close_window(self, window_name):
        """Close the existing window if it exists."""
        if window_name in self.windows:
            self.windows[window_name].deleteLater()
            del self.windows[window_name]

    def show_window(self, window_name, window_class):
        """General method to close and show a fresh window."""
        self.close_window(window_name)
        self.windows[window_name] = window_class()  # Create and store the window
        self.windows[window_name].showMaximized()    



if __name__ == "__main__":
    app = QApplication([])
    loginApp = LoginWindow()
    mainApp = MainWindow()
    loginApp.show()
    sys.exit(app.exec())