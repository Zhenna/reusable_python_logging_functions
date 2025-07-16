import os
import logging
from datetime import datetime


def setup_logger(
    log_dir: str,
    log_filename: str = None,
    log_level=logging.INFO,
    log_format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
) -> logging.Logger:
    """
    Set up a logger that writes to both a file and the console.

    Args:
        log_dir (str): Directory to save the log file.
        log_filename (str, optional): Base name of the log file. If not provided, defaults to "log".
                                      A timestamp will be appended to ensure uniqueness.
        log_level (int, optional): Logging level (e.g., logging.INFO, logging.DEBUG). Defaults to logging.INFO.
        log_format (str, optional): Format string for log messages. Defaults to a standard format
                                    including timestamp, log level, filename, and message.

    Returns:
        logging.Logger: Configured logger instance.
    """
    os.makedirs(log_dir, exist_ok=True)

    if not log_filename:
        log_filename = "log"

    log_filename_timestamped = (
        f"{log_filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )
    log_path = os.path.join(log_dir, log_filename_timestamped)

    logger = logging.getLogger(log_path)
    logger.setLevel(log_level)
    logger.propagate = True

    if not logger.handlers:
        formatter = logging.Formatter(fmt=log_format, datefmt="%Y-%m-%d %H:%M:%S")

        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def close_logger(logger: logging.Logger) -> None:
    """
    Properly close and remove all handlers from a logger.

    Args:
        logger (logging.Logger): Logger instance to clean up.
    """
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
