"""Test if image URLs are correct"""
from app import app

with app.app_context():
    from flask import url_for
    
    # Test image path
    test_path = "uploads/flat/pexels-medhat-ayad-122846-439227.jpg"
    url = url_for('static', filename=test_path)
    print(f"Image path: {test_path}")
    print(f"Generated URL: {url}")
    print(f"\nFull URL would be: http://localhost:5000{url}")

