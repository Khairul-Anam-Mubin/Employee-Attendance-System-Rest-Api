# Employee Attendance System

## Installation Guide

### Backend (Language - python, FrameWork - Django Rest API)

1. Activate Virtual Environment : VENV\Scripts\activate
2. Install the requirements.txt
3. Connect the mongodb database
4. Create a mongodb database on local host and named "EmployeeAttendanceSystemDB"
5. Run "python manage.py makemigrations" for making the database migrations
6. Run "python manage.py migrate" for migrate
7. Run "python manage.py runserver" and it will run in localhost

## Aplication Programming Interface

### API Endpoints

* /createAccount        -> [POST] request will create new employee account details
* /showEmployee         -> [GET] request will show all the employee account details
* /ShowEmployee/<id>    -> [GET] request will show specific employee account details
* /createAttendance     -> [POST] request will create the attendance if data is validated
* /monthlyReport        -> [GET] request will show current monthly reports
* /monthlyReport        -> [POST] request with "startDate" and "endDate" json request will return the employee status in this date range

#### For any invalid json request it will response with null

## Project Architecture Design

### EmployeeAttendanceSystem
* Projects main settings and path routing are defined here.

### Account Application
* models.py file contains the employee details fields
* serializers.py file used to serialize the complex data into simple data according to models
* views.py contains the request mapping functions
* service.py contains CreateAccountService class which takes the json parsed data 
and check validation. Also Used to insert data into database. Another class ShowEmployeeService return the employees data according to GET and GET by id request.

### TimeTracking
* models.py file contains the attendane details according to there current status.
* service.py 

### Frondend with Angular
1. /employee page will show all the employee records
2. There is Add Member button which will pop up modal to create new employee
3. /attendance will show the current monthly report and there are filter options for monthly time tracking reports based on month and year.
4. Add Attendance button will pop up modal and create attendances.