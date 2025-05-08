import numpy as np
from PIL import Image
from scipy import ndimage

def detect_edges(image):
    """
    Detekuje hrany v obrázku pomocí Sobelových operátorů.
    Používá optimalizované scipy.ndimage.convolve funkce.
    
    Args:
        image: PIL Image objekt
        
    Returns:
        PIL Image s detekovanými hranami
    """
    # Převedení na grayscale
    image_array = np.array(image.convert("L"))
    
    # Definice Sobelových operátorů
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [0,   0,  0],
                        [1,   2,  1]])
    
    # Aplikace konvoluce přímo s využitím scipy
    gx = ndimage.convolve(image_array, sobel_x, mode='constant', cval=0.0)
    gy = ndimage.convolve(image_array, sobel_y, mode='constant', cval=0.0)
    
    # Výpočet magnitudy gradientu
    magnitude = np.sqrt(gx ** 2 + gy ** 2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)
    
    return Image.fromarray(magnitude)