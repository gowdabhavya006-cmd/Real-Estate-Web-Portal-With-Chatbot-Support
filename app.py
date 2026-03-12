from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager
import os
import json

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# Create upload directory
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Jinja2 filters
@app.template_filter('from_json')
def from_json_filter(value):
    """Parse JSON string to Python object"""
    if not value:
        return []
    try:
        return json.loads(value)
    except:
        return []

# Import models for login manager
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
from routes.auth import auth_bp
from routes.properties import properties_bp
from routes.admin import admin_bp
from routes.api import api_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(properties_bp, url_prefix='/properties')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(api_bp, url_prefix='/api')

# Main routes
@app.route('/')
def index():
    """Home page"""
    from flask import render_template
    from models import Property
    # Get featured and recent properties
    featured_properties = Property.query.filter_by(is_approved=True, is_featured=True).limit(6).all()
    recent_properties = Property.query.filter_by(is_approved=True).order_by(Property.created_at.desc()).limit(6).all()
    return render_template('index.html', 
                         featured_properties=featured_properties,
                         recent_properties=recent_properties)

@app.route('/about')
def about():
    """About page"""
    from flask import render_template
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    """Contact page"""
    from flask import render_template
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)

