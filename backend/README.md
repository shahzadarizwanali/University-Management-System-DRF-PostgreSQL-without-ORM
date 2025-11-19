# 🎓 University Management System (Django + DRF + Raw SQL + PostgreSQL)

This project is a **University Management System** built using **Django REST Framework**, **PostgreSQL**, and **Raw SQL queries only (NO ORM)**.

It includes complete CRUD operations for:

- University
- Department
- Faculty
- Student
- Classroom

All CRUD APIs are written using **psycopg2** and **manual SQL queries**, following real-world backend engineering practices.

---

## 🚀 Features

### ✔ No Django ORM Used

All database operations are performed using **raw SQL queries** via `psycopg2`.

### ✔ PostgreSQL Integration

A complete `schema.sql` file is provided to generate all required tables.

### ✔ Modular Code Structure

- `views.py` → All CRUD APIs
- `db.py` → PostgreSQL connection
- `urls.py` → Route definitions
- `schema.sql` → Database structure

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/university-management-rawsql.git
cd university-management-rawsql
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create PostgreSQL database

Create a database:

```sql
CREATE DATABASE university_db;
```

### 4️⃣ Import schema

Inside pgAdmin or terminal:

```sql
\i schema.sql
```

### 5️⃣ Configure `.env` (or update settings.py)

Update your PostgreSQL credentials:

```
NAME = "university_db"
USER = "postgres"
PASSWORD = "your_password"
HOST = "localhost"
PORT = "5432"
```

### 6️⃣ Run Django server

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

| Model      | GET               | POST              | PUT                   | DELETE                |
| ---------- | ----------------- | ----------------- | --------------------- | --------------------- |
| University | /api/university/  | /api/university/  | /api/university/<id>  | /api/university/<id>  |
| Department | /api/departments/ | /api/departments/ | /api/departments/<id> | /api/departments/<id> |
| Faculty    | /api/faculty/     | /api/faculty/     | /api/faculty/<id>     | /api/faculty/<id>     |
| Student    | /api/students/    | /api/students/    | /api/students/<id>    | /api/students/<id>    |
| Classroom  | /api/classrooms/  | /api/classrooms/  | /api/classrooms/<id>  | /api/classrooms/<id>  |

---

## 🗄 Database Schema (PostgreSQL)

See file: `schema.sql`

---

## 🧑‍💻 Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- PostgreSQL
- psycopg2 (Raw SQL)

---

## 📁 Project Structure

```
backend/
│── api/
│   ├── views.py
│   ├── urls.py
│   ├── db.py
│── schema.sql
│── requirements.txt
│── README.md
│── manage.py
```

---

## 👨‍🎓 Author

**Shahzada Rizwan Ali**  
📧 [shahzadarizwanali01@gmail.com](mailto:shahzadarizwanali01@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/shahzadarizwanali)

University Management System (DRF + Raw SQL)

---

## ⭐ Contribution

Feel free to fork the repo and submit PRs.

---

## 📄 License

MIT License
