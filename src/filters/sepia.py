from PIL import Image

def apply_sepia(image):
    """
    Aplication of sepia filter on an image.
    """
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            # Omezit hodnoty na max 255
            pixels[x, y] = (min(255, tr), min(255, tg), min(255, tb))

    return image
