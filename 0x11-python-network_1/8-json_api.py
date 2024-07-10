#!/usr/bin/python3
"""
User Search Script

This script sends an HTTP POST request to a specified URL
with a query parameter. The parameter is derived from the first
command-line argument. If no argument is
provided, an empty string is used as the query parameter.

Usage:
    ./script [letter]

Arguments:
    [letter]  An optional string to be used as the value
    for the query parameter 'q'.

Example:
    ./script a

**Functionality:**
    - The script constructs a payload with the query parameter
        'q' set to the value
      of the first command-line argument or an empty string if
        no argument is provided.
    - It sends an HTTP POST request to "http://0.0.0.0:5000/search_user"
        with the payload.
    - It attempts to parse the JSON response.
    - If the response contains no result, it prints "No result".
    - If the response is a valid JSON with data, it prints the
        user's id and name in the format: "[id] name".
    - If the response is not a valid JSON, it prints "Not a valid JSON".

Requirements:
    - The 'requests' module must be installed.

Exit Codes:
    The script does not explicitly set exit codes for
    different error conditions.
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        json_response = res.json()
        if not json_response:
            print("No result")
        else:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
