"""Seed database with sample property data"""
from app import app, db
from models import User, Property
import json
from decimal import Decimal

def seed_properties():
    """Add sample properties for each city and category"""
    with app.app_context():
        # Get or create admin user
        admin = User.query.filter_by(email='admin@realestate.com').first()
        if not admin:
            print("Admin user not found. Please run init_db.py first.")
            return
        
        cities = ['Bengaluru', 'Mysore', 'Shivamogga', 'Hubli', 'Hassan']
        categories = {
            'flat': {
                'name': 'Flat',
                'bedrooms': [1, 2, 3, 4],
                'bathrooms': [1, 2, 3],
                'area_range': (600, 2000),
                'price_range_sale': (3000000, 15000000),
                'price_range_rent': (15000, 60000)
            },
            'house': {
                'name': 'House',
                'bedrooms': [2, 3, 4, 5],
                'bathrooms': [2, 3, 4],
                'area_range': (1200, 4000),
                'price_range_sale': (5000000, 25000000),
                'price_range_rent': (25000, 100000)
            },
            'shop': {
                'name': 'Shop',
                'bedrooms': [0],
                'bathrooms': [1, 2],
                'area_range': (200, 1500),
                'price_range_sale': (2000000, 12000000),
                'price_range_rent': (10000, 80000)
            },
            'office': {
                'name': 'Office',
                'bedrooms': [0],
                'bathrooms': [1, 2, 3],
                'area_range': (500, 3000),
                'price_range_sale': (4000000, 20000000),
                'price_range_rent': (20000, 120000)
            }
        }
        
        locations = {
            'Bengaluru': [
                'Koramangala', 'Indiranagar', 'Whitefield', 'Marathahalli', 'HSR Layout',
                'BTM Layout', 'Jayanagar', 'Rajajinagar', 'Malleshwaram', 'Yelahanka'
            ],
            'Mysore': [
                'Vijayanagar', 'Gokulam', 'Kuvempunagar', 'Nazarbad', 'Saraswathipuram',
                'T K Layout', 'Bogadi', 'Hootagalli', 'Hunsur Road', 'Ring Road'
            ],
            'Shivamogga': [
                'Gandhi Nagar', 'Bhadravathi Road', 'Kuvempu Nagar', 'Sagar Road',
                'Tunga Nagar', 'Vidyanagar', 'New Extension', 'Old Town', 'MG Road', 'Station Road'
            ],
            'Hubli': [
                'Dharwad Road', 'Gokul Road', 'Deshpande Nagar', 'Vidyanagar',
                'Unkal', 'Old Hubli', 'New Hubli', 'Keshwapur', 'Rayapur', 'Navalgund Road'
            ],
            'Hassan': [
                'MG Road', 'Belur Road', 'Sakleshpur Road', 'New Extension',
                'Old Town', 'Industrial Area', 'Railway Station Road', 'Bus Stand Road',
                'Kuvempu Nagar', 'Vidyanagar'
            ]
        }
        
        property_count = 0
        
        for city in cities:
            city_locations = locations[city]
            
            for category_key, category_info in categories.items():
                # Create 10 properties for each category in each city
                for i in range(10):
                    import random
                    
                    # Determine listing type (70% sale, 30% rent)
                    listing_type = 'sale' if random.random() < 0.7 else 'rent'
                    
                    # Set price based on listing type
                    if listing_type == 'sale':
                        price = random.randint(*category_info['price_range_sale'])
                    else:
                        price = random.randint(*category_info['price_range_rent'])
                    
                    # Set bedrooms and bathrooms
                    bedrooms = random.choice(category_info['bedrooms'])
                    bathrooms = random.choice(category_info['bathrooms']) if bedrooms > 0 else random.choice([1, 2])
                    
                    # Set area
                    area = random.randint(*category_info['area_range'])
                    
                    # Select location
                    location = random.choice(city_locations)
                    
                    # Generate property title
                    if category_key in ['shop', 'office']:
                        title = f"{area} sq ft {category_info['name']} Space in {location}"
                    else:
                        title = f"{bedrooms} BHK {category_info['name']} in {location}"
                    
                    # Generate description
                    descriptions = {
                        'flat': f"Beautiful {bedrooms} BHK flat in prime location of {location}, {city}. Well-maintained property with modern amenities. Close to schools, hospitals, and shopping centers. Perfect for families.",
                        'house': f"Spacious {bedrooms} BHK independent house in {location}, {city}. Built with quality materials, featuring a garden and parking space. Ideal for large families seeking comfort and privacy.",
                        'shop': f"Prime commercial {category_info['name'].lower()} space in {location}, {city}. High footfall area, perfect for retail business. Good visibility and accessibility. Ready to move in.",
                        'office': f"Modern {category_info['name'].lower()} space in {location}, {city}. Fully furnished with all amenities. Suitable for corporate offices, startups, or professional services. Great connectivity."
                    }
                    
                    description = descriptions[category_key]
                    
                    # Create property
                    property_obj = Property(
                        title=title,
                        description=description,
                        property_type=category_key,
                        price=Decimal(str(price)),
                        location=f"{location}, {city}",
                        city=city,
                        state='Karnataka',
                        pincode=str(random.randint(560000, 580000)),
                        bedrooms=bedrooms,
                        bathrooms=bathrooms,
                        area_sqft=Decimal(str(area)),
                        listing_type=listing_type,
                        status='available',
                        images=None,  # User will add images later
                        user_id=admin.id,
                        is_approved=True,
                        is_featured=(i < 2)  # First 2 properties in each category are featured
                    )
                    
                    db.session.add(property_obj)
                    property_count += 1
        
        try:
            db.session.commit()
            print(f"\n✓ Successfully added {property_count} properties!")
            print(f"✓ Properties added for cities: {', '.join(cities)}")
            print(f"✓ Categories: {', '.join([c['name'] for c in categories.values()])}")
            print(f"✓ 10 properties per category per city")
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")

if __name__ == '__main__':
    seed_properties()

