# Application Form Filling Project

## Project Overview

The **Application Form Filling Project** is a web-based application developed to collect, store, and manage user application details efficiently. It provides a user-friendly interface for filling out forms and a secure backend for processing and storing data.

This project is built using the **Django framework** and follows a structured MVC/MVT architecture to ensure scalability, security, and maintainability.

---

## Technologies / Techniques Used

### Backend

* **Python** – Core programming language
* **Django** – Web framework for backend logic and routing
* **MySQL** – Relational database for storing application data

### Frontend

* **HTML** – Structure of web pages
* **CSS** – Styling and layout
* **JavaScript** – Client-side validation and interactivity

---

## Key Features

* User-friendly application form
* Form validation (client-side and server-side)
* Secure data storage using MySQL
* Dynamic rendering using Django templates
* Clean and responsive UI

---

## Project Structure (Basic)

```
Application_form/
│── app/
│── templates/
│── static/
│── db.sqlite3 / MySQL
│── manage.py
```

---

## Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/charangoud-creator/Application_form.git
```

2. Navigate to the project directory

```bash
cd Application_form
```

3. Install dependencies

```bash
pip install django mysqlclient
```

4. Configure MySQL database in `settings.py`

5. Run migrations

```bash
python manage.py migrate
```

6. Start the development server

```bash
python manage.py runserver
```

---

## Future Enhancements

* Authentication system (Login/Signup)
* Admin dashboard
* File upload support
* Email notifications

---

## Developed By

**Charan Goud**

---

## License

This project is for educational purposes.
