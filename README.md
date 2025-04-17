# Registration_and_Login_Form_Using_Django

A simple Django-based web application that provides user registration and login functionality. This project is ideal for beginners looking to understand user authentication workflows in Django.

**User Authentication Page :**

![Screenshot 2025-04-17 211925](https://github.com/user-attachments/assets/3709f161-e5af-4445-aeb3-086a58a76fe0)


## Features

- User registration with email and password.
- Secure login and logout functionality.
- Input validation with error messages.
- Password hashing for secure storage.
- Admin page access

**Register Page :**  

![Screenshot 2025-04-17 211943](https://github.com/user-attachments/assets/77510d12-33fc-450d-9c73-1f154eac7cd3)


  
**Login Page :**

![Screenshot 2025-04-17 212014](https://github.com/user-attachments/assets/1f0e48ae-4118-4c0f-bc4d-4b310af7e589)


  
**Home Page :**

![Screenshot 2025-04-17 212046](https://github.com/user-attachments/assets/a360ffe3-f458-4b3b-9317-722cbe9e96a0)


## Technologies Used

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** HTML5
- **Database:** SQLite (default Django database)
- **Others:** Django's built-in authentication framework


**D-jango Admin Page :**

![Screenshot 2025-04-17 212141](https://github.com/user-attachments/assets/21e86b3a-1700-48db-9542-409540f6c300)

  

## Prerequisites

Ensure you have the following installed on your system:

- Python (version 3.8 or later)
- Django (version 4.x or later)
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/anbuchelvanvk/Registration_and_Login_Form_Using_Django.git
   cd Registration_and_Login_Form_Using_Django

2. **Migrate the files after starting app**
   python manage.py makemigrations
   python manage.py migrate
   
4. **Run the development**
   python manage.py runserver

   **Access the Application through the browser**
   Link : http://127.0.0.1:8000/

Registration_and_Login_Form_Using_Django
│
├── website/                   # Django project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL configurations
│   └── ...
│
├── userreg/                   # Django app for user management
│   ├── templates/             # HTML templates
│   ├── forms.py               # Forms for user input
│   ├── models.py              # Database models
│   ├── views.py               # View functions and logic
│   └── ...
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script

