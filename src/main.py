from utils.image_loader import load_image
from utils.image_saver import save_image
from utils.logger import setup_logger
from filters import grayscale, sepia, invert
from math_utils import convolution, histogram_equalization, edge_detection
import os
import argparse
import numpy as np

def list_filters():
    print("\nAvailable filters:")
    print("1 - Grayscale")
    print("2 - Sepia")
    print("3 - Invert")
    print("4 - Convolution (Sharpening)")
    print("5 - Histogram Equalization")
    print("6 - Edge Detection")

def apply_selected_filters(image, filters, output_dir, logger):
    for i, f in enumerate(filters, start=1):
        if f in ["1", "grayscale"]:
            logger.info("Applying Grayscale")
            result = grayscale.apply_grayscale(image)
            save_image(result, os.path.join(output_dir, f"output_grayscale.jpg"))

        elif f in ["2", "sepia"]:
            logger.info("Applying Sepia")
            result = sepia.apply_sepia(image)
            save_image(result, os.path.join(output_dir, f"output_sepia.jpg"))

        elif f in ["3", "invert"]:
            logger.info("Applying Invert")
            result = invert.apply_invert(image)
            save_image(result, os.path.join(output_dir, f"output_invert.jpg"))

        elif f in ["4", "convolution"]:
            logger.info("Applying Convolution (Sharpening)")
            sharpen_kernel = np.array([[0, -1, 0],
                                       [-1, 5, -1],
                                       [0, -1, 0]])
            result = convolution.apply_convolution(image, sharpen_kernel)
            save_image(result, os.path.join(output_dir, f"output_convolution.jpg"))

        elif f in ["5", "hist_eq"]:
            logger.info("Applying Histogram Equalization")
            result = histogram_equalization.equalize_histogram(image)
            save_image(result, os.path.join(output_dir, f"output_hist_eq.jpg"))

        elif f in ["6", "edges"]:
            logger.info("Applying Edge Detection")
            result = edge_detection.detect_edges(image)
            save_image(result, os.path.join(output_dir, f"output_edges.jpg"))

        else:
            logger.warning(f"Unknown filter: {f}")

def interactive_mode(image, output_dir, logger):
    selected_filters = []
    while True:
        list_filters()
        choice = input("Select filter number (0 = start processing): ").strip()
        if choice == "0":
            break
        selected_filters.append(choice)

    apply_selected_filters(image, selected_filters, output_dir, logger)
    logger.info("Processing complete. Results saved.")

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description='Command-line Photo Editor.')
    parser.add_argument('--input', type=str, help='Path to the input image', required=True)
    parser.add_argument('--output_dir', type=str, help='Path to the output directory', required=True)
    parser.add_argument('--filters', nargs='+', help='List of filters by number or name')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        logger.error("Input image does not exist.")
        return

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        logger.info(f"Created output directory: {args.output_dir}")

    image = load_image(args.input)

    if args.interactive:
        interactive_mode(image, args.output_dir, logger)

    elif args.filters:
        apply_selected_filters(image, args.filters, args.output_dir, logger)
        logger.info("Processing complete. Results saved.")

    else:
        print("\nYou must specify either --filters or --interactive")
        parser.print_help()

if __name__ == "__main__":
    main()
