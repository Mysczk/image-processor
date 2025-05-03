from utils.image_loader import load_image
from utils.image_saver import save_image
from utils.logger import setup_logger
import os

def main():
    logger = setup_logger()

    input_path = os.path.join("data", "input", "croco.jpeg")
    output_path = os.path.join("data", "output", "croco.jpg")
    try:
        logger.info(f"Loading file from {input_path}")
        image = load_image(input_path)


        logger.info(f"Saving file to {output_path}")
        save_image(image, output_path)

        logger.info("Image processing success.")

    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
