"""Remove all plot properties from database"""
from app import app, db
from models import Property

def remove_plots():
    """Delete all plot properties"""
    with app.app_context():
        plot_properties = Property.query.filter_by(property_type='plot').all()
        count = len(plot_properties)
        
        if count > 0:
            for prop in plot_properties:
                db.session.delete(prop)
            
            try:
                db.session.commit()
                print(f"✓ Successfully removed {count} plot properties from database")
            except Exception as e:
                db.session.rollback()
                print(f"Error: {e}")
        else:
            print("No plot properties found in database")

if __name__ == '__main__':
    remove_plots()

