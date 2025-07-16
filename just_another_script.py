from datetime import datetime
import logging
import re


def get_day_of_week(date_str: str, logger: logging.Logger) -> str:
    """
    Convert a date string in the format "YYYY-MM-DD" to the corresponding day of the week.

    Args:
        date_str (str): The date string to convert.
        logger (logging.Logger): Logger instance for logging information and errors.

    Returns:
        str: The day of the week if valid; otherwise, returns None.
    """
    logger.info(f"Received date input: '{date_str}'")

    # Check if input matches the required pattern
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        logger.error(
            f"Invalid format: '{date_str}' does not match 'YYYY-MM-DD'. "
            "Expected format: 4-digit year, 2-digit month, 2-digit day (e.g., 2023-10-01)."
        )
        return None

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        day_of_week = date_obj.strftime("%A")
        logger.info(f"Converted date '{date_str}' to day of week: {day_of_week}")
        return day_of_week

    except ValueError as ve:
        logger.exception(
            f"Date parsing failed for input '{date_str}'. "
            f"This could be due to an invalid date value (e.g., February 30). Error: {ve}"
        )
        return None

    except Exception as e:
        logger.exception(
            f"Unexpected error while converting date '{date_str}' to day of week: {e}"
        )
        return None
