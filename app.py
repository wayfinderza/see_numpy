import os
import numpy as np
from flask import Flask, request, redirect, url_for, render_template, flash

# Create the Flask app
app = Flask(__name__)

# Set upload folder (adjust path as needed)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "supersecretkey"  # For flash messages

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("home"))

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("home"))

    if file and file.filename.endswith(".npz"):
        # Ensure the upload folder exists
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        
        # Define the full file path
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], "array.npz")  # Static file name to always overwrite
        
        try:
            # Save the uploaded file (overwrites if it already exists)
            file.save(file_path)

            # Load the file and process it
            data = np.load(file_path)
            array_keys = list(data.keys())  # Get all array keys (names) in the NPZ file
            dimensions = {key: data[key].shape for key in array_keys}  # Get dimensions

            flash(f"File uploaded successfully! Arrays: {array_keys}, Dimensions: {dimensions}")
        except Exception as e:
            flash(f"Error processing file: {e}")
            return redirect(url_for("home"))
    else:
        flash("Invalid file type. Please upload a valid .npz file.")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)