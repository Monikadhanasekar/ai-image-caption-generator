# AI Image Caption Generator

An AI-powered backend application built using FastAPI and Hugging Face Transformers that generates captions and hashtags from uploaded images.

---

## Features

- Upload image API
- AI-generated image captions
- Automatic hashtag generation
- File validation
- Exception handling
- Swagger API documentation
- Modular backend architecture

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Hugging Face Transformers
- BLIP Image Captioning Model
- Pillow

---

## Project Structure

app/
│
├── routes/
├── services/
├── utils/
├── main.py

uploads/

---

## API Endpoint

### Upload Image

POST /upload-image

Accepts:
- JPG
- JPEG
- PNG

Returns:
- Caption
- Hashtags
- File details

---

## Example Response

json
{
    "message": "Image uploaded successfully",
    "file_path": "uploads/image.jpg",
    "filename": "image.jpg",
    "caption": "a dog running in the grass",
    "hashtags": [
        "#dog",
        "#running",
        "#grass"
    ]
}


---

## Future Improvements

- Object detection
- Multi-language captions
- Cloud deployment
- Frontend integration

---

## Author

Monika