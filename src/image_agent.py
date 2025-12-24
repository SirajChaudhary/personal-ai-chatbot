import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Vision model
vision_model = genai.GenerativeModel("gemini-2.0-flash")


def upload_images(images):
    """
    Converts Streamlit UploadedFile objects to Gemini image format.
    Supports single or multiple images.
    """
    if not images:
        raise ValueError("No images uploaded")

    # Normalize to list
    if not isinstance(images, list):
        images = [images]

    image_payloads = []

    for image in images:
        image_payloads.append({
            "mime_type": image.type,
            "data": image.getvalue(),
        })

    return image_payloads


def query_image(prompt, image_data):
    """
    Sends prompt with one or more images to Gemini Vision.
    """
    if not image_data:
        raise ValueError("Image data is empty")

    # Gemini expects: [prompt, image1, image2, ...]
    contents = [prompt] + image_data

    response = vision_model.generate_content(contents=contents)

    return response.text if hasattr(response, "text") else "No response from model"
