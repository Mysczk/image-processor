import os

def save_image(image, output_path):
    """
    Save an image object to the specified output path.
    
    Args:
        image: PIL Image object to save
        output_path: String path where the image should be saved
    
    Raises:
        IOError: If an error occurs during saving
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        image.save(output_path)
        print(f"File saved: {output_path}")
    except Exception as e:
        raise IOError(f"Error while saving file: {e}") from e
