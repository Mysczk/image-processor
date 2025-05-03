from PIL import Image
import os

def load_image(image_path):
    """
    Loads an image from the specified file path.
    
    Args:
        image_path: Path to the image file.
    
    Returns:
        The loaded image object.
    
    Raises:
        FileNotFoundError: If the file does not exist at the given path.
        IOError: If an error occurs while opening the image file.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File {image_path} not found.")
    
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        raise IOError(f"Error while loading file: {e}")
