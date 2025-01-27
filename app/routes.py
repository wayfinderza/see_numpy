import os
import numpy as np
from flask import Blueprint, request, render_template, flash, current_app

# Create a blueprint
main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return render_template('index.html')
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return render_template('index.html')
    
    if file and file.filename.endswith('.npz'):
        # Save the file to the server
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        try:
            file.save(file_path)  # Save the uploaded file
            
            # Load the file and process it
            data = np.load(file_path)
            array_keys = list(data.keys())  # Get all array keys (names) in the NPZ file
            
            # Example: Get dimensions of each array
            dimensions = {key: data[key].shape for key in array_keys}
            
            flash(f"File uploaded successfully! Arrays found: {array_keys}, Dimensions: {dimensions}")
        except Exception as e:
            flash(f"Error processing file: {e}")
            return render_template('index.html')
    else:
        flash('Invalid file type. Please upload a valid .npz file.')
    
    return render_template('index.html')
