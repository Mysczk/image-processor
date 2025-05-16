import numpy as np
from PIL import Image
from scipy import ndimage

def detect_edges(image, method="sobel"):
    """
    Detekuje hrany v obrázku pomocí zvoleného gradientového operátoru.
    
    Args:
        image: PIL Image objekt
        method: typ operátoru - 'sobel', 'prewitt', nebo 'scharr'
        
    Returns:
        PIL Image s detekovanými hranami
    """
    # Převedení na grayscale
    image_array = np.array(image.convert("L"), dtype=float)
    
    # Definice gradientových operátorů
    if method == "sobel":
        kernel_x = np.array([[-1, 0, 1],
                             [-2, 0, 2],
                             [-1, 0, 1]])
        kernel_y = np.array([[-1, -2, -1],
                             [0,   0,  0],
                             [1,   2,  1]])
    elif method == "prewitt":
        kernel_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])
        kernel_y = np.array([[-1, -1, -1],
                             [0,   0,  0],
                             [1,   1,  1]])
    elif method == "scharr":
        kernel_x = np.array([[-3, 0, 3],
                             [-10, 0, 10],
                             [-3, 0, 3]])
        kernel_y = np.array([[-3, -10, -3],
                             [0,    0,  0],
                             [3,   10,  3]])
    else:
        raise ValueError("Unknown method. Use 'sobel', 'prewitt' or 'scharr'.")
    
    # Konvoluce s lepším okrajovým režimem
    gx = ndimage.convolve(image_array, kernel_x, mode='reflect')
    gy = ndimage.convolve(image_array, kernel_y, mode='reflect')
    
    # Výpočet magnitudy gradientu
    magnitude = np.hypot(gx, gy)
    
    # Normalizace na rozsah 0-255
    magnitude = (magnitude / magnitude.max()) * 255
    magnitude = magnitude.astype(np.uint8)
    
    return Image.fromarray(magnitude)

# Příklad použití:
# image = Image.open("obrazek.jpg")
# edges = detect_edges(image, method="scharr")
# edges.show()
