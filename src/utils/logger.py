import logging
import os

def setup_logger(log_file="image_processor.log"):
    """
    Configures and returns a logger for image processing tasks.
    
    Creates a logger named "ImageProcessorLogger" with both file and console handlers. Log files are stored in the "logs" directory, with file logs capturing DEBUG and higher level messages and console output showing INFO and higher. Both handlers use a consistent timestamped format.
    
    Args:
        log_file: Name of the log file to write logs to within the "logs" directory.
    
    Returns:
        A configured logging.Logger instance.
    """
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
