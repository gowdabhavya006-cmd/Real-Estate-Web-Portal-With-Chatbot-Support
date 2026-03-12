"""Check image paths in database"""
from app import app, db
from models import Property
import json

def check_images():
    """Check a few properties to see their image paths"""
    with app.app_context():
        properties = Property.query.filter(Property.images.isnot(None)).limit(5).all()
        
        print("Sample properties with images:\n")
        for prop in properties:
            images = json.loads(prop.images) if prop.images else []
            print(f"Property ID: {prop.id}")
            print(f"Title: {prop.title}")
            print(f"Type: {prop.property_type}")
            print(f"Images ({len(images)}):")
            for img in images:
                print(f"  - {img}")
            print("-" * 50)

if __name__ == '__main__':
    check_images()

