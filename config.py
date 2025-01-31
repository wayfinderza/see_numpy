# config.py
import os

class Config:
    SECRET_KEY = "supersecretkey"
    UPLOAD_FOLDER = "uploads"
    SAMPLES_FOLDER_SUBPATH = "static/samples"

    @staticmethod
    def init_app(app):
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        app.config["SAMPLES_FOLDER"] = os.path.join(
            app.root_path,
            app.config["SAMPLES_FOLDER_SUBPATH"]
        )
