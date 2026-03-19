# 🚀 Smart Task Manager API

A **FastAPI-based backend project** that allows users to securely manage their tasks with authentication and intelligent priority detection.

---

## 🔐 Features

* 🔑 **JWT Authentication** (Signup & Login)
* 📋 **Task Management (CRUD)**

  * Create Task
  * View Tasks
  * Update Task
  * Delete Task
* 🤖 **Smart Priority Detection**

  * "urgent" → High
  * "important" → Medium
  * others → Low
* 👤 **User-specific Data Access**
* 🛠 **Admin APIs**

  * View all users
  * View all tasks
* ⚙️ **Middleware Logging**
* 🗄 **MySQL Database Integration**

---

## 🧠 Tech Stack

* ⚡ FastAPI
* 🐍 Python
* 🗄 MySQL
* 🔐 JWT (python-jose)
* 🔒 Passlib (bcrypt)
* 🌐 Uvicorn

---

## 📁 Project Structure

```
smart-task-api/
│
├── main.py
├── database.py
├── auth.py
├── models.py
├── utils.py
├── requirements.txt
├── README.md
│
├── routes/
│   ├── user.py
│   ├── task.py
│   ├── admin.py
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR-USERNAME/smart-task-api.git
cd smart-task-api
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create `.env` File

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
SECRET_KEY=your_secret_key
```

---

### 4️⃣ Run Server

```
uvicorn main:app --reload
```

---

### 5️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Testing Flow

1. Signup
2. Login → get token
3. Authorize using:

```
Bearer <your_token>
```

4. Use APIs:

   * `/tasks`
   * `/profile`
   * `/admin/*`

---

## 🔐 Security Note

* Sensitive data like passwords and secret keys are stored using **environment variables**
* `.env` file is excluded from GitHub using `.gitignore`

---

## 💼 Use Case

This project simulates a real-world backend system like:

* Todo Apps
* Task Managers
* Project Management Tools

---

## 🚀 Future Improvements

* Role-based authentication (Admin/User)
* Frontend integration (React)
* Docker support
* Deployment with cloud database

---

## 👨‍💻 Author

**Kanha Patidar**

---

## 🌟 If you like this project

Give it a ⭐ on GitHub and share it on LinkedIn 🚀
