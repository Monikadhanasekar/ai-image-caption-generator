AI Image Caption Generator

Developed By

Monika D

An AI-powered web application that generates image captions and relevant hashtags from uploaded images.

Features

- Upload JPG, JPEG, and PNG images
- Generate captions using AI
- Generate relevant hashtags automatically
- FastAPI backend
- React frontend
- User-friendly interface

Tech Stack

Frontend

- React.js
- CSS

Backend

- FastAPI
- Python

AI Model

- BLIP (Salesforce Image Captioning Model)
- Hugging Face Transformers

Project Workflow

1. User uploads an image.
2. React frontend sends the image to the FastAPI backend.
3. The BLIP model processes the image.
4. A caption is generated.
5. Relevant hashtags are created from caption keywords.
6. Results are displayed to the user.

Installation

Backend

pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend

cd frontend
npm install
npm start
