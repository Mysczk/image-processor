import numpy as np
from PIL import Image
import cv2

def equalize_histogram(image):
    """
    Provádí ekvalizaci histogramu na obrázku.
    Používá optimalizovanou implementaci OpenCV.
    
    Args:
        image: PIL Image objekt
        
    Returns:
        PIL Image po ekvalizaci histogramu
    """
    # Převedení na grayscale
    image_array = np.array(image.convert("L"))
    
    # Použití optimalizované funkce z OpenCV
    equalized = cv2.equalizeHist(image_array)
    
    return Image.fromarray(equalized)