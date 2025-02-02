
# 🎓 School Management System

A comprehensive Qt-based desktop application for managing school operations including student admission, staff management, attendance tracking, marks management, and fee collection.

## 📋 Features

### 🧑‍🎓 Student Management
- New student admission with automatic ID generation 🎟️
- Student information editing ✏️
- Student records viewing and filtering 🔍
- Student attendance tracking 📅
- Academic performance management 📊

### 👩‍🏫 Staff Management
- Staff registration with automatic ID generation 🆔
- Staff information editing ✏️
- Staff records viewing and filtering 🔍
- Staff attendance tracking 📅
- Department-wise staff organization 🏢

### 📚 Academic Management
- Mark entry and management 📝
- Report card generation 🏅
- Academic performance tracking 📈
- Student attendance records 📊
- Class and section management 🏫

### 💰 Financial Management
- Fee collection and tracking 💵
- Fee records management 🧾
- Payment history 🗓️

## ⚙️ Technical Requirements

### Prerequisites
- Python 3.x 🐍
- Pyside6 📦
- SQLite3 💾
- docxtpl (for report generation) 📄

### Dependencies
```bash
pip install pyside6 sqlite3 docxtpl random string subprocess
```

## 🗃️ Database Structure

The system uses SQLite3 for data management with the following main tables:

1. **students** - Stores student information
   - `id` (Primary Key)
   - `first_name`
   - `last_name`
   - `fname` (Father's Name)
   - `mname` (Mother's Name)
   - `gender`
   - `dob` (Date of Birth)
   - `address`
   - `contact`
   - `email`
   - `standard`
   - `division`

2. **staff** - Stores staff information
   - `staff_id` (Primary Key)
   - `category`
   - `first_name`
   - `last_name`
   - `gender`
   - `dob` (Date of Birth)
   - `address`
   - `contact`
   - `email`
   - `department`
   - `salary`

3. **marks** - Stores student academic performance
   - `std_id` (Foreign Key)
   - `subject_name`
   - `theory_marks`
   - `assignment_marks`

4. **fees** - Stores fee collection records
   - `std_id` (Foreign Key)
   - `amount`
   - `fee_date`

5. **attendance** - Stores student attendance
   - `std_id` (Foreign Key)
   - `date`
   - `status`
   - `standard`
   - `division`

6. **staff_attendance** - Stores staff attendance
   - `staff_id` (Foreign Key)
   - `date`
   - `status`
   - `department`

## 🛠️ Key Classes

1. **AdmissionWindow** 🏫
   - Handles new student admissions
   - Generates unique student IDs
   - Manages student database operations

2. **StaffWindow** 👩‍🏫
   - Manages staff registration
   - Handles staff categorization (Teaching/Non-Teaching)
   - Maintains staff records

3. **MarksheetWindow** 📝
   - Manages student academic records
   - Generates report cards
   - Calculates grades and percentages

4. **FeesWindow** 💸
   - Handles fee collection
   - Maintains payment records
   - Generates fee reports

5. **AttendanceWindow** 📅
   - Manages both student and staff attendance
   - Provides attendance tracking and reporting
   - Supports multiple attendance status options

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/anshulwycliffe/school-management-system.git
```

2. Install required dependencies
```bash
pip install pyside6 docxtpl
```


3. Run the application
```bash
python main.py
```

## 🚀 Usage

### 🧑‍🎓 Student Management
1. Use the **Admission Window** for new student registration
2. Student ID is automatically generated with 'S-' prefix 🎟️
3. All mandatory fields must be filled ✏️
4. Student records can be viewed and filtered in the **Records Window** 🔍

### 👩‍🏫 Staff Management
1. Use the **Staff Window** for new staff registration
2. Staff ID is automatically generated with 'T-' or 'NT-' prefix based on category 🆔
3. Department and salary information must be provided 💼
4. Staff records can be filtered by department 🏢

### 📅 Attendance
1. Select date and class/department 📅
2. Mark attendance as Present/Absent/Late/Excused ✅❌
3. Save attendance records 💾
4. View attendance history 📊

### 📚 Academic Records
1. Enter marks by subject 📝
2. Generate report cards 🏅
3. Calculate grades automatically 📈
4. View academic performance history 📊

## 🤝 Contributing

1. Fork the repository 🍴
2. Create a feature branch 🧑‍💻
3. Commit your changes 💾
4. Push to the branch 🚀
5. Create a Pull Request ✨

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
