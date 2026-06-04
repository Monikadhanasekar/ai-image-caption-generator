from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "Salesforce/blip-image-captioning-base"
)