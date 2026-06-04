import os
from fastapi import UploadFile

from app.config import UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

async def save_uploaded_file(file: UploadFile):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return file_path