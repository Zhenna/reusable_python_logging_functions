# write a python function to convert an input date to day of the week
# The function should take a date string in the format "YYYY-MM-DD" and return the day of the week
# Example:
# Input: "2023-10-01"
# Output: "Sunday"
from datetime import datetime

from log_functions import setup_logger, close_logger


def get_day_of_week(date_str):
    """
    Convert a date string in the format "YYYY-MM-DD" to the day of the week.

    Args:
    date_str (str): The date string in the format "YYYY-MM-DD".

    Returns:
    str: The day of the week.
    """
    try:
        # Check if the input date string is in the correct format
        datetime.strptime(date_str, "%Y-%m-%d")
        # If the format is correct, proceed to convert the date string
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        # If the format is incorrect, raise an error
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    # Get the day of the week as a string
    return date_obj.strftime("%A")


# Example usage
if __name__ == "__main__":

    # add a timestamp to the log file name
    log_filename = f"mylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logger = setup_logger(log_dir="logfiles", log_file=log_filename)

    date_input = "2023-10-01"
    day_of_week = get_day_of_week(date_input)
    print(f"The day of the week for {date_input} is {day_of_week}.")
