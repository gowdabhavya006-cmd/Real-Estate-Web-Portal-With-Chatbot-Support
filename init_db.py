"""Database initialization script"""
from app import app, db
from models import User, Property, Contact
from werkzeug.security import generate_password_hash

def init_database():
    """Initialize database with default admin user"""
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin user exists
        admin = User.query.filter_by(email='admin@realestate.com').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@realestate.com',
                full_name='Administrator',
                role='admin',
                is_active=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✓ Admin user created successfully!")
            print("  Email: admin@realestate.com")
            print("  Password: admin123")
        else:
            print("✓ Admin user already exists")
        
        print("\n✓ Database initialized successfully!")
        print("✓ You can now run the application with: python app.py")

if __name__ == '__main__':
    init_database()

