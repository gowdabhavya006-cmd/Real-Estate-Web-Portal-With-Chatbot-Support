# Real Estate Web Portal with Chatbot Support

A comprehensive real estate web portal that enables users to search, view, and post properties for sale or rent, with integrated 24/7 chatbot support.

## Features

- **User Authentication**: Registration, login, and profile management for users, agents, and admins
- **Property Listings**: Post, view, edit, and manage property listings with images
- **Advanced Search & Filters**: Search by location, price, property type, and features
- **AI Chatbot**: 24/7 virtual assistant to answer common queries
- **Admin Panel**: Manage users, approve listings, and view statistics
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Chatbot**: JavaScript-based intelligent bot

## Installation

1. **Prerequisites**:
   - Python 3.8 or higher
   - MySQL Server (XAMPP/WAMP)
   - pip (Python package manager)

2. **Setup Database**:
   - Start MySQL server (via XAMPP/WAMP)
   - Create a database named `real_estate_portal`
   - Update database credentials in `config.py` if needed (default: root/12345)

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**:
   ```bash
   python init_db.py
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Portal**:
   - Open your browser and navigate to `http://localhost:5000`

## Default Admin Credentials

- **Email**: admin@realestate.com
- **Password**: admin123

## User Roles

- **Admin**: Full system access, manages users and listings
- **Agent/Property Owner**: Can post and manage property listings
- **Buyer/User**: Can browse, search, and contact sellers

## Project Structure

```
real-estate-project/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── init_db.py            # Database initialization
├── requirements.txt      # Python dependencies
├── models.py             # Database models
├── routes/               # Route handlers
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   ├── properties.py    # Property routes
│   ├── admin.py         # Admin routes
│   └── api.py           # API endpoints
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── auth/
│   ├── properties/
│   └── admin/
├── static/               # Static files
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
└── utils/                # Utility functions
    ├── __init__.py
    └── helpers.py
```

## Features in Detail

### 1. User Authentication
- Secure registration and login
- Password hashing
- Session management
- Profile editing

### 2. Property Management
- Upload property details and images
- Edit and delete listings
- View property details
- Contact seller functionality

### 3. Search & Filters
- Search by city/location
- Filter by price range
- Filter by property type (flat, house, shop, etc.)
- Filter by features (bedrooms, bathrooms, etc.)

### 4. Chatbot
- Answers common FAQs
- Assists with navigation
- Provides property search help
- 24/7 availability

### 5. Admin Panel
- User management
- Property approval/rejection
- System statistics
- Report handling

## License

This project is created for educational purposes.

