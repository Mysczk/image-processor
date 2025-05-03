from utils.image_loader import load_image
from utils.image_saver import save_image
from utils.logger import setup_logger
from filters import grayscale, sepia, invert
import os
import argparse

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description='Process images with filters.')
    parser.add_argument(
        '--input',
        default=os.path.join("data", "input", "croco.jpeg"),
        help='Path to input image'
    )
    parser.add_argument(
        '--output',
        default=os.path.join("data", "output", "croco.jpg"),
        help='Path to output image'
    )
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    try:
        logger.info(f"Loading image from {input_path}")
        image = load_image(input_path)

        logger.info("Applying Grayscale filter")
        grayscale_image = grayscale.apply_grayscale(image)
        grayscale_output = os.path.join(os.path.dirname(output_path), "croco_grayscale.jpg")
        save_image(grayscale_image, grayscale_output)

        logger.info("Applying Sepia filter")
        sepia_image = sepia.apply_sepia(image)
        sepia_output = os.path.join(os.path.dirname(output_path), "croco_sepia.jpg")
        save_image(sepia_image, sepia_output)

        logger.info("Applying Invert filter")
        invert_image = invert.apply_invert(image)
        invert_output = os.path.join(os.path.dirname(output_path), "croco_invert.jpg")
        save_image(invert_image, invert_output)

        logger.info("Image processing complete. All filtered images saved.")

    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
