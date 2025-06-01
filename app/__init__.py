# Core Setup for Flask Application
from flask import Flask

def create_app(): # application factory pattern
    """Create and configure the Flask application."""
    app = Flask(__name__)

    from .routes import main # relative import
    app.register_blueprint(main)
    
    return app