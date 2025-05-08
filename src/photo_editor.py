from utils.image_loader import load_image
from utils.image_saver import save_image
from utils.logger import setup_logger
from filters import grayscale, sepia, invert
from math_utils import convolution, histogram_equalization, edge_detection
import os
import argparse
import numpy as np

SHARPEN_KERNEL = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

FILTER_MAP = {
    "1": ("Grayscale", lambda img: grayscale.apply_grayscale(img), "output_grayscale.jpg"),
    "grayscale": ("Grayscale", lambda img: grayscale.apply_grayscale(img), "output_grayscale.jpg"),
    "2": ("Sepia", lambda img: sepia.apply_sepia(img), "output_sepia.jpg"),
    "sepia": ("Sepia", lambda img: sepia.apply_sepia(img), "output_sepia.jpg"),
    "3": ("Invert", lambda img: invert.apply_invert(img), "output_invert.jpg"),
    "invert": ("Invert", lambda img: invert.apply_invert(img), "output_invert.jpg"),
    "4": ("Convolution (Sharpening)", lambda img: convolution.apply_convolution(img, SHARPEN_KERNEL), "output_convolution.jpg"),
    "convolution": ("Convolution (Sharpening)", lambda img: convolution.apply_convolution(img, SHARPEN_KERNEL), "output_convolution.jpg"),
    "5": ("Histogram Equalization", lambda img: histogram_equalization.equalize_histogram(img), "output_hist_eq.jpg"),
    "hist_eq": ("Histogram Equalization", lambda img: histogram_equalization.equalize_histogram(img), "output_hist_eq.jpg"),
    "6": ("Edge Detection", lambda img: edge_detection.detect_edges(img), "output_edges.jpg"),
    "edges": ("Edge Detection", lambda img: edge_detection.detect_edges(img), "output_edges.jpg"),
}

def list_filters():
    print("\nAvailable filters:")
    # Filter numeric keys and sort them
    numeric_keys = sorted([k for k in FILTER_MAP.keys() if k.isdigit()],
                          key=int)
    for key in numeric_keys:
        label = FILTER_MAP[key][0]
        print(f"{key} - {label}")
    print("0 - Start processing\n")

def apply_selected_filters(image, filters, output_dir, logger):
    for f in filters:
        key = f.lower()
        if key in FILTER_MAP:
            label, func, filename = FILTER_MAP[key]
            try:
                logger.info(f"Applying {label}")
                result = func(image)
                save_path = os.path.join(output_dir, filename)
                save_image(result, save_path)
                logger.info(f"Saved result to {save_path}")
            except Exception as e:
                logger.error(f"Failed to apply {label}: {e}")
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
    if not selected_filters:
        logger.info("No filters selected.")
    else:
        apply_selected_filters(image, selected_filters, output_dir, logger)
        logger.info("Processing complete. Results saved.")

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description='Command-line Photo Editor.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input image')
    parser.add_argument('--output_dir', type=str, required=True, help='Path to the output directory')
    parser.add_argument('--filters', nargs='+', help='List of filters by number or name')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        logger.error(f"Input image '{args.input}' does not exist.")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    logger.info(f"Output directory: {args.output_dir}")

    try:
        image = load_image(args.input)
    except Exception as e:
        logger.error(f"Failed to load image: {e}")
        return

    if args.interactive:
        interactive_mode(image, args.output_dir, logger)
    elif args.filters:
        apply_selected_filters(image, args.filters, args.output_dir, logger)
        logger.info("Processing complete. Results saved.")
    else:
        logger.warning("No filters specified. Use --filters or --interactive.")
        parser.print_help()

if __name__ == "__main__":
    main()
