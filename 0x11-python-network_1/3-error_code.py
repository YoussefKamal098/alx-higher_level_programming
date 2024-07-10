#!/usr/bin/python3
"""
This script fetches and displays the content of a specified URL.

**Functionality:**

- Takes a URL as an argument from the command line.
- Makes a GET request to the provided URL.
- Handles potential exceptions:
    - HTTPError: If the server responds with an error code,
        it prints only the error code.
    - URLError: If there's a network issue or the URL is invalid,
        it prints a generic error message and the reason from the exception.
- If successful, it prints the decoded content of the response body from
    the server, assuming UTF-8 encoding.
"""
import sys
from urllib.error import HTTPError, URLError
from urllib import request

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: ./script <url>")
        exit(1)

    url = sys.argv[1]
    req = request.Request(url)

    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf8'))

    except HTTPError as e:
        print('Error code: ', e.code)
