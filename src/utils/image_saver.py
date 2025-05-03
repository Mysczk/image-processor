import os

def save_image(image, output_path):
    """
    Saves an image object to the specified file path, creating directories as needed.
    
    Args:
        image: An image object with a `save` method (e.g., from PIL or similar libraries).
        output_path: The file path where the image will be saved.
    
    Raises:
        IOError: If an error occurs during directory creation or image saving.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        image.save(output_path)
        print(f"File saved: {output_path}")
    except Exception as e:
        raise IOError(f"Error while saving file: {e}")
