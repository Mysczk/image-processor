from PIL import Image
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File {image_path} not found.")
    
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        raise IOError(f"Error while loading file: {e}")
