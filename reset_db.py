"""Reset database - Drops all tables and recreates them"""
from app import app, db
from models import User, Property, Contact
from werkzeug.security import generate_password_hash

def reset_database():
    """Drop all tables and recreate them with default admin user"""
    with app.app_context():
        print("⚠️  WARNING: This will delete all existing data!")
        print("Dropping all tables...")
        
        # Disable foreign key checks to allow dropping tables with constraints
        db.session.execute(db.text("SET FOREIGN_KEY_CHECKS = 0"))
        
        # Drop all tables manually to handle any orphaned tables
        try:
            db.session.execute(db.text("DROP TABLE IF EXISTS contacts"))
            db.session.execute(db.text("DROP TABLE IF EXISTS properties"))
            db.session.execute(db.text("DROP TABLE IF EXISTS messages"))  # Drop orphaned table
            db.session.execute(db.text("DROP TABLE IF EXISTS users"))
            db.session.commit()
        except Exception as e:
            print(f"Note: {e}")
            db.session.rollback()
        
        # Also try SQLAlchemy's drop_all
        try:
            db.drop_all()
        except Exception as e:
            print(f"Note: {e}")
        
        # Re-enable foreign key checks
        db.session.execute(db.text("SET FOREIGN_KEY_CHECKS = 1"))
        db.session.commit()
        
        print("Creating all tables...")
        # Create all tables
        db.create_all()
        
        # Create default admin user
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
        
        print("\n✓ Database reset successfully!")
        print("✓ All tables recreated with correct schema")
        print("✓ Admin user created:")
        print("  Email: admin@realestate.com")
        print("  Password: admin123")
        print("\n✓ You can now run the application with: python app.py")

if __name__ == '__main__':
    reset_database()

