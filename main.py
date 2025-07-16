import os
import argparse
from log_config import setup_logger, close_logger
from just_another_script import get_day_of_week


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Convert a date string (YYYY-MM-DD) to the day of the week."
    )

    parser.add_argument(
        "--date_input",
        required=True,
        type=str,
        help="Date string in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--log_filename",
        required=False,
        type=str,
        default="my_logger",
        help="The base filename for the log file (timestamp will be added).",
    )
    parser.add_argument(
        "--log_dir",
        required=False,
        type=str,
        default="logfiles",
        help="Directory to save log files.",
    )

    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args()

    logger = setup_logger(
        log_dir=args.log_dir,
        log_filename=args.log_filename,
    )

    day_of_week = get_day_of_week(args.date_input, logger)
    if day_of_week:
        logger.info(f"Result: {args.date_input} is a {day_of_week}.")
    else:
        logger.warning(f"Failed to determine day of week for input: {args.date_input}")

    close_logger(logger)
