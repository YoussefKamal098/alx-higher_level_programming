#!/usr/bin/python3
"""
This module processes log data read from standard input,
tracking the total file size and counts of encountered HTTP status codes.

Example usage:
cat access.log | python script_name.py
"""

from sys import stdin


def print_info(total_size, status_codes):
    """
    Prints information about processed log data:

    - Total file size
    - Counts of HTTP status codes encountered

    Parameter:
        total_size (int): The total size of processed files.
        status_codes (dict): A dictionary where keys are HTTP
        status codes and values are their counts.
    """
    print(f"File size: {total_size}")

    for code, value in sorted(status_codes.items()):
        if value > 0:
            print("{:s}: {:d}".format(code, value))


def parse_line(line):
    """
    Parses a log line and extracts status code and file size.

    Parameter:
        line (str): The log line to parse.

    Returns:
        tuple[int, int]: A tuple containing the extracted status code
        and file size, or None if the line cannot be parsed.
    """
    tokens = line.split()

    if len(tokens) >= 2:
        status_code, file_size = tokens[-2], tokens[-1]
        return status_code, file_size
    else:
        return None, None


def process_log_data():
    """
    Reads and processes log data from standard input,
    tracking file size and HTTP status codes.

    Raises:
        KeyboardInterrupt: If the user interrupts the program with Ctrl+C.
    """

    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    total_size = 0
    lines_processed = 0

    try:
        for line in stdin:
            status_code, file_size = parse_line(line)

            if status_code in status_codes:
                status_codes[status_code] += 1

            if file_size is not None:
                total_size += file_size

            lines_processed += 1

            if lines_processed % 10 == 0:
                print_info(total_size, status_codes)

    except KeyboardInterrupt:
        print_info(total_size, status_codes)

    return total_size, status_codes


if __name__ == "__main__":
    total_size, status_codes = process_log_data()
