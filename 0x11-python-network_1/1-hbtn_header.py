#!/usr/bin/python3
"""
This script fetches the value of the "X-Request-Id" header from a specified
URL.

**Functionality:**

- Takes a URL as an argument from the command line.
- Makes a GET request to the provided URL.
- Handles potential exceptions:
    - HTTPError: If the server responds with an error code, it prints a generic
        error message and the error code.
    - URLError: If there's a network issue or the URL is invalid, it prints a
        generic error message and the reason from the exception.
- If successful, it prints the value of the "X-Request-Id" header
    from the server response.
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
            print(res.headers.get("X-Request-Id"))

    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
