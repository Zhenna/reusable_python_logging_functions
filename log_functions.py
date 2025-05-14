import os
import logging
from datetime import datetime
import pandas as pd


# from typing import Dict, List, Union
from typing import Generator, List, Tuple, Any, Dict, Union


def setup_logger(
    log_dir: str, log_filename: str = None, level=logging.INFO
) -> logging.Logger:
    """
    Set up a logger that writes to both file and console, including script name in logs.

    Args:
        log_dir (str): Directory to save the log file.
        log_filename (str): Optional log file name. If not provided, a timestamped filename is used.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    os.makedirs(log_dir, exist_ok=True)

    if not log_filename:
        log_filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    log_path = os.path.join(log_dir, log_filename)
    logger = logging.getLogger(log_path)  # Unique logger per path
    logger.setLevel(level)
    logger.propagate = False  # Prevent double logging if root logger is configured

    if not logger.handlers:
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

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
