# Python Developer Assignment – Fitness Studio Booking API


## Here is full guide to setup the project:
### 1. create a virtual environment
```bash
    - virtulenv env
```
### 2. Now activate virtual environment
```bash
    - .\env\Scripts\activate
```

### 3. install all the dependencies
```bash
    - pip install -r .\requirements.txt
```

### 4. Now run the server
```bash
    - py manage.py runserver
```


# API Endpoints:
## 1. GET  /api/classes
### - this end point shows all the upcomming classes .
### - gives data like class_name , instructor, class_date, created_at, available_slots
### - it also takes the tz=time/zone parameter to converts the time zone of class_date and created_at

## 2. POST /api/book
### - this end point is for creating a booking of class.
### - in this end point we have to pass the data like class_instance(class_id), client_name, client_email.
###   {
###   "class_instance": 1,
###   "client_name": "John Doe",
###   "client_email": "john@example.com"
###   }
### - this end point check the one client name should book a class only once.
### - this end point book a class only if slots are available


## 3. GET /api/bookings?email=client@email.com
### - this end point fetches all the booking of a perticular email address.

# Features

### - Built with Django & Django REST Framework

### - Timezone-aware datetime handling

### - Input validation & error responses

### - SQLite used for local storage (no external DB required)

### - Modular, clean code structure