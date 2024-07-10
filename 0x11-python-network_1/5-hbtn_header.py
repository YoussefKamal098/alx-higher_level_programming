#!/usr/bin/python3
"""
This script fetches the value of the "X-Request-Id" header from a
specified URL using the Requests library.

**Functionality:**

- Takes a URL as an argument from the command line.
- Makes a GET request to the provided URL.
- Extracts the value of the "X-Request-Id" header from the response,
    if it exists.
- Prints the value of the "X-Request-Id" header
    (or an empty string if not found).
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: ./script <url>")
        exit(1)

    url = sys.argv[1]
    res = requests.get(url)
    print(f"{res.headers.get('X-Request-Id')}")
