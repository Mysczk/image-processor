import numpy as np
from PIL import Image

def equalize_histogram(image):
    image_array = np.array(image.convert("L"))
    hist, bins = np.histogram(image_array.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]
    equalized = np.interp(image_array.flatten(), bins[:-1], cdf_normalized)
    return Image.fromarray(equalized.reshape(image_array.shape).astype(np.uint8))
