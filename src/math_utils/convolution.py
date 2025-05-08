import numpy as np
from PIL import Image
from scipy import signal

def apply_convolution(image, kernel):
    # Validate input
    if not isinstance(image, Image.Image):
        raise TypeError("Input must be a PIL Image object")
    if not isinstance(kernel, np.ndarray) or kernel.ndim != 2:
        raise TypeError("Kernel must be a 2D NumPy array")
        
    image_array = np.array(image.convert("L"))
    output = signal.convolve2d(image_array, kernel, mode='same', boundary='fill', fillvalue=0)
    output = np.clip(output, 0, 255).astype(np.uint8)

    return Image.fromarray(output)
