from PIL import Image

def apply_grayscale(image):
    """
    Graysecale filter application on an image.
    """
    return image.convert("L")
