import numpy as np
from PIL import Image
from .convolution import apply_convolution

def detect_edges(image):
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [0,   0,  0],
                        [1,   2,  1]])

    gx = np.array(apply_convolution(image, sobel_x))
    gy = np.array(apply_convolution(image, sobel_y))

    magnitude = np.sqrt(gx ** 2 + gy ** 2)
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

    return Image.fromarray(magnitude)
