# Payroll Management System

A web-based Payroll Management System developed using Django to manage employee information, attendance, leave requests, payroll records, salary calculations, salary slips, and payroll reports.

## Features

- Employee Management
  - Add, update, view, and delete employees
  - Employee search
  - Department filtering
  - Employee details/profile

- Attendance Management
  - Record employee attendance
  - Present, Absent, and Leave status
  - Add remarks
  - Edit and delete attendance records

- Leave Management
  - Add leave records
  - View leave requests
  - Leave status display

- Payroll Management
  - Create and manage payroll records
  - Automatic net salary calculation
  - Attendance-based salary calculation
  - Salary slips

- Payroll Reports
  - Employee-wise payroll reports
  - Month-wise filtering
  - Printable payroll reports

- Dashboard
  - Total Employees
  - Payroll Records
  - Attendance Records
  - Leave Requests
  - Total Payroll Amount

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Django ORM
- Git & GitHub

## MVT Architecture

This project follows Django's Model-View-Template (MVT) architecture.

- **Model:** Handles database structure and data.
- **View:** Handles application logic and requests.
- **Template:** Displays the user interface.

## Project Structure

```text
PayrollManagementSystem/
│
├── accounts/
├── employees/
├── attendance/
├── payroll/
├── config/
├── templates/
├── static/
├── manage.py
├── .gitignore
└── README.md
