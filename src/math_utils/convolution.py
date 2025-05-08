import numpy as np
from PIL import Image

def apply_convolution(image, kernel):
    image_array = np.array(image.convert("L"))  # grayscale
    kernel_height, kernel_width = kernel.shape
    padded_image = np.pad(image_array, ((1, 1), (1, 1)), mode='constant')
    output = np.zeros_like(image_array)

    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            region = padded_image[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.clip(np.sum(region * kernel), 0, 255)

    return Image.fromarray(output)
