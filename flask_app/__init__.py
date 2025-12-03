from flask import Flask

def create_application():
    """
    Initializes and configures the Flask application instance.
    Serves as the entry points used by 'flask run'
    """
    application = Flask(__name__)
    
    # Register Blueprints (Modules)
    from .routes import main_blueprint, auth_blueprint
    application.register_blueprint(main_blueprint)
    application.register_blueprint(auth_blueprint)
    
    return application