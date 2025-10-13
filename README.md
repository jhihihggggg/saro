# SmartGardenHub - Student Management System

A comprehensive Flask-based student management system for educational institutions.

## 🌟 Features

- **Multi-Role Authentication**: Support for Students, Teachers, and Super Users
- **Student Management**: CRUD operations for student records
- **Batch Management**: Organize students into batches/classes
- **Attendance Tracking**: Mark and monitor student attendance
- **Online Exams**: Create and manage online assessments
- **Monthly Exams**: Track regular monthly examinations
- **SMS Integration**: Send notifications to parents/students
- **Dashboard Analytics**: Real-time statistics and insights

## 🚀 Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL / SQLite
- **Authentication**: Flask-Session with secure password hashing
- **Frontend**: HTML, CSS, JavaScript
- **SMS**: Custom SMS integration

## 📋 Prerequisites

- Python 3.8+
- MySQL Server (or SQLite for development)
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/8ytgggygt/saro.git
   cd saro
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DATABASE=smartgardenhub
   SECRET_KEY=your_secret_key_here
   ```

5. **Initialize database**
   ```bash
   python init_db.py
   python create_default_users.py
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

   Server will start at `http://127.0.0.1:5000`

## 👥 Default Login Credentials

After running `create_default_users.py`:

**Admin Account:**
- Phone: `01712345678`
- Password: `admin123`

**Teacher Account:**
- Phone: `01812345678`
- Password: `teacher123`

**Student Account:**
- Phone: `01912345678`
- Password: `student123`

## 📁 Project Structure

```
saro/
├── app.py                 # Main application entry point
├── config.py              # Configuration settings
├── models.py              # Database models
├── auth.py                # Authentication routes
├── routes/                # API routes
│   ├── students.py
│   ├── batches.py
│   ├── attendance.py
│   ├── exams.py
│   └── ...
├── utils/                 # Utility functions
│   ├── auth.py
│   ├── response.py
│   └── password_manager.py
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── requirements.txt       # Python dependencies
└── README.md
```

## 🔐 Security Features

- Secure password hashing using Werkzeug
- Role-based access control (RBAC)
- Session management
- Local password storage for students
- SQL injection protection via SQLAlchemy ORM

## 📝 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user

### Students
- `GET /api/students` - List all students
- `POST /api/students` - Create new student
- `GET /api/students/{id}` - Get student details
- `PUT /api/students/{id}` - Update student
- `DELETE /api/students/{id}` - Delete student
- `GET /api/students/passwords` - Get student passwords (Teacher only)

### Batches
- `GET /api/batches` - List all batches
- `POST /api/batches` - Create new batch
- `GET /api/batches/{id}` - Get batch details
- `PUT /api/batches/{id}` - Update batch
- `DELETE /api/batches/{id}` - Delete batch

### Attendance
- `POST /api/attendance` - Mark attendance
- `GET /api/attendance` - Get attendance records

### Exams
- `GET /api/exams` - List all exams
- `POST /api/exams` - Create new exam
- `GET /api/exams/{id}/results` - Get exam results

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Golam Sarowar Sir**

## 🆘 Support

For support, email support@smartgardenhub.com or open an issue in the repository.

## 📱 Contact

- Website: [smartgardenhub.com](http://smartgardenhub.com)
- Email: contact@smartgardenhub.com

---

**Built with ❤️ for educational institutions**
