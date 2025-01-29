import os
import numpy as np
from flask import Flask, request, redirect, url_for, render_template, flash
from utils.file_processing import load_npz_file, validate_npz_file

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
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], "array.npz")  # Static file name

        try:
            file.save(file_path)

            # **NEW: Validate the file before loading**
            is_valid, error_message = validate_npz_file(file_path)
            if not is_valid:
                flash(error_message)
                return redirect(url_for("home"))

            # Load the file only if validation passes
            arrays = load_npz_file(file_path)

            flash("File uploaded successfully!")
            return render_template("index.html", arrays=arrays)

        except Exception as e:
            flash(f"Error processing file: {e}")
            return redirect(url_for("home"))
    else:
        flash("Invalid file type. Please upload a valid .npz file.")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
