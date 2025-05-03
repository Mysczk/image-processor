from PIL import ImageOps

def apply_invert(image):
    """
    Inverzion of image.
    """
    return ImageOps.invert(image)
