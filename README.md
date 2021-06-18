Homework for Zonar Middleware SDE role.

# Background
A delivery company hired you to help them build an application that will follow federal regulations in regards to how many hours a driver can work and operate behind a vehicle. You're hired as a backend developer to write some APIs that can be used with client applications. 
Below are some business rules that define (simplified version) how work hours and drive hours should be tracked to avoid driver's being in violation of federal laws.
The law tracks two types of work clocks: 
Working: tracks time between clock in and clock out, this can include loading packages, driving and unloading packages and delivering them to the building/house
Driving: tracks the time while driving the vehicle
each work clock has max allowed hours, and when those are exceeded the driver is violating the law.

# How to use this app:
- after clicking the 'code' dropdown, copy the github ssh link
- in your terminal enter git clone (the link you copied)
- pip or poetry install the dependancies

## If you are using docker:
- docker-compose up
- username: a_beaver, password: password123

## If you are using shell
- poetry shell
- python manage.py makemigrations homework_api
- python manage.py migrate
- python manage.py createsuperuser
- create your username and password
- *in the browser* navigate to: 127.0.0.1:8000/admin
- add your 'driver'
- navigate to 127.0.0.1:8000
- Here you will see your driver and can update their drive times.
