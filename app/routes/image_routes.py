from fastapi import APIRouter, UploadFile, File
from app.utils.file_handler import save_uploaded_file
from app.services.caption_service import generate_caption
from app.models.response_models import ImageUploadResponse
from app.utils.logger import logger

router = APIRouter()

@router.post(
    "/upload-image",
    response_model=ImageUploadResponse
)

async def upload_image(file: UploadFile = File(...)):

    if file.content_type not in [
        "image/jpeg",
        "image/jpg",
        "image/png"
    ]:
        return {
            "error": "Only JPG, JPEG, and PNG files are allowed"
        }

    try:

        file_path = await save_uploaded_file(file)
        logger.info("Image uploaded successfully")
        result = generate_caption(file_path)
        logger.info("Caption and hashtags generated successfully")

    except Exception as e:
        
        logger.error(f"Error processing image: {str(e)}")

        return {
            "error": f"Unable to process image: {str(e)}"
        }

    return {
        "message": "Image uploaded successfully",
        "file_path": file_path,
        "filename": file.filename,
        "caption": result["caption"],
        "hashtags": result["hashtags"]
    }