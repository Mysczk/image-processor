from utils.image_loader import load_image
from utils.image_saver import save_image
from utils.logger import setup_logger
from filters import grayscale, sepia, invert
from math_utils import convolution, histogram_equalization, edge_detection
import os
import argparse
import numpy as np

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description='Process images with filters and math utils.')
    parser.add_argument('--input', default=os.path.join("data", "input", "croco.jpeg"), help='Path to input image')
    parser.add_argument('--output', default=os.path.join("data", "output", "croco.jpg"), help='Path to output image')
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    try:
        logger.info(f"Loading image from {input_path}")
        image = load_image(input_path)

        logger.info("Applying Grayscale filter")
        save_image(grayscale.apply_grayscale(image), os.path.join("data/output", "croco_grayscale.jpg"))

        logger.info("Applying Sepia filter")
        save_image(sepia.apply_sepia(image), os.path.join("data/output", "croco_sepia.jpg"))

        logger.info("Applying Invert filter")
        save_image(invert.apply_invert(image), os.path.join("data/output", "croco_invert.jpg"))

        logger.info("Applying Convolution (Sharpening)")
        sharpen_kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
        conv_img = convolution.apply_convolution(image, sharpen_kernel)
        save_image(conv_img, os.path.join("data/output", "croco_convolution.jpg"))

        logger.info("Applying Histogram Equalization")
        eq_img = histogram_equalization.equalize_histogram(image)
        save_image(eq_img, os.path.join("data/output", "croco_hist_eq.jpg"))

        logger.info("Applying Edge Detection")
        edge_img = edge_detection.detect_edges(image)
        save_image(edge_img, os.path.join("data/output", "croco_edges.jpg"))

        logger.info("Image processing complete. All results saved.")

    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
