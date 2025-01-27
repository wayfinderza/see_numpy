from flask import Flask
import os

# Initialize the Flask app
def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Set the folder to save uploaded files
    UPLOAD_FOLDER = 'uploads'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Import and register the blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
