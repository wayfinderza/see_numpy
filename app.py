import os
import numpy as np
from flask import Flask, request, redirect, url_for, render_template, flash
from utils.file_processing import load_npz_file, validate_npz_file
from config import Config  # Import the config class

app = Flask(__name__)
app.config.from_object(Config)  # Load config from our Config class
Config.init_app(app) 

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
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], "array.npz")
        try:
            file.save(file_path)

            # Validate
            is_valid, error_message = validate_npz_file(file_path)
            if not is_valid:
                flash(error_message)
                return redirect(url_for("home"))

            # Parse
            arrays = load_npz_file(file_path)

            flash("File uploaded successfully!")
            return render_template("index.html", arrays=arrays)

        except Exception as e:
            flash(f"Error processing file: {e}")
            return redirect(url_for("home"))
    else:
        flash("Invalid file type. Please upload a valid .npz file.")
    return redirect(url_for("home"))

@app.route("/load_sample/<sample_id>", methods=["GET"])
def load_sample(sample_id):
    """
    Loads a sample NPZ file and processes it just like an uploaded file.
    """
    sample_file = f"sample{sample_id}.npz"
    sample_path = os.path.join(SAMPLES_FOLDER, sample_file)

    if not os.path.exists(sample_path):
        flash("Sample file not found.")
        return redirect(url_for("home"))

    upload_path = os.path.join(app.config["UPLOAD_FOLDER"], "array.npz")
    try:
        # Copy sample file to uploads directory
        with open(sample_path, "rb") as src, open(upload_path, "wb") as dst:
            dst.write(src.read())

        # Validate the copied sample file
        is_valid, error_message = validate_npz_file(upload_path)
        if not is_valid:
            flash(error_message)
            return redirect(url_for("home"))

        # Parse the arrays using existing logic
        arrays = load_npz_file(upload_path)

        flash(f"Sample {sample_id} loaded successfully!")
        return render_template("index.html", arrays=arrays)

    except Exception as e:
        flash(f"Error loading sample: {e}")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
