"""Assign images from folders to properties"""
from app import app, db
from models import Property
import json
import os
import random
from pathlib import Path

def assign_images_to_properties():
    """Assign images from category folders to properties"""
    with app.app_context():
        # Define image folders
        base_path = Path('static/uploads')
        categories = ['flat', 'house', 'office', 'shop']
        
        # Get all images for each category
        category_images = {}
        total_images = 0
        for category in categories:
            category_path = base_path / category
            if category_path.exists():
                images = []
                # Check for images with various extensions
                for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.webp', '*.JPG', '*.JPEG', '*.PNG', '*.GIF', '*.WEBP']:
                    images.extend(category_path.glob(ext))
                
                # Convert to relative paths
                image_paths = [f"uploads/{category}/{img.name}" for img in images]
                category_images[category] = image_paths
                total_images += len(image_paths)
                print(f"✓ Found {len(image_paths)} images for {category}")
            else:
                print(f"⚠ Warning: Folder {category_path} does not exist - please create it and add images")
                category_images[category] = []
        
        if total_images == 0:
            print("\n⚠ No images found! Please add images to the following folders:")
            for category in categories:
                print(f"   - static/uploads/{category}/")
            print("\nSupported formats: .jpg, .jpeg, .png, .gif, .webp")
            return
        
        # Get all properties
        properties = Property.query.filter(Property.property_type.in_(categories)).all()
        print(f"\nFound {len(properties)} properties to assign images to")
        
        updated_count = 0
        for property_obj in properties:
            category = property_obj.property_type
            if category in category_images and category_images[category]:
                # Select random images (1-5 images per property, repeating if needed)
                num_images = random.randint(1, min(5, len(category_images[category])))
                # Allow repetition by using random.choices instead of random.sample
                selected_images = random.choices(category_images[category], k=num_images)
                
                # Update property with images
                property_obj.images = json.dumps(selected_images)
                updated_count += 1
        
        try:
            db.session.commit()
            print(f"\n✓ Successfully assigned images to {updated_count} properties!")
            print(f"✓ Images are randomly assigned and repeated across different properties")
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")

if __name__ == '__main__':
    assign_images_to_properties()

