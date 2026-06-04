from pydantic import BaseModel
from typing import List


class ImageUploadResponse(BaseModel):

    message: str
    file_path: str
    filename: str
    caption: str
    hashtags: List[str]