# Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- MySQL Server (XAMPP/WAMP recommended)
- pip (Python package manager)

## Step-by-Step Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup MySQL Database
1. Start MySQL server (via XAMPP/WAMP)
2. Open MySQL command line or phpMyAdmin
3. Create a new database:
   ```sql
   CREATE DATABASE real_estate_portal;
   ```

### 3. Configure Database Connection
The default configuration uses:
- Host: localhost
- User: root
- Password: 12345
- Database: real_estate_portal

Edit `config.py` if your MySQL credentials are different:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/real_estate_portal'
```

### 4. Initialize Database
```bash
python init_db.py
```
This will:
- Create all necessary tables
- Create a default admin user
  - Email: `admin@realestate.com`
  - Password: `admin123`

### 5. Run the Application
```bash
python app.py
```

### 6. Access the Portal
Open your browser and navigate to:
```
http://localhost:5000
```

## Default Admin Login
- **Email**: admin@realestate.com
- **Password**: admin123

## User Roles

### Admin
- Full system access
- Manage users and properties
- Approve/reject property listings
- View statistics and inquiries

### Agent
- Post property listings
- Manage own listings
- View inquiries on their properties

### User
- Browse and search properties
- Contact sellers
- Use chatbot for assistance

## Features to Test

1. **User Registration**: Register as a user or agent
2. **Property Posting**: Login as agent and post a property
3. **Property Search**: Use filters to find properties
4. **Chatbot**: Click the chat button and ask questions
5. **Admin Panel**: Login as admin to manage the system

## Troubleshooting

### Database Connection Error
- Ensure MySQL server is running
- Check database credentials in `config.py` (default: root/12345)
- Verify database `real_estate_portal` exists

### Port Already in Use
- Change port in `app.py`: `app.run(debug=True, port=5001)`

### Image Upload Issues
- Ensure `static/uploads/` directory exists and is writable
- Check file size limits in `config.py`

## Next Steps
- Add your own property images
- Customize the design in `static/css/style.css`
- Add more chatbot responses in `static/js/chatbot.js`
- Configure email notifications (optional)

