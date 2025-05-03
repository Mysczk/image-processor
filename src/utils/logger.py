import logging
import os

def setup_logger(log_file="image_processor.log"):
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("ImageProcessorLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(os.path.join("logs", log_file))
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
