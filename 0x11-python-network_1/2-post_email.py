#!/usr/bin/python3
"""
This script sends an HTTP POST request to a specified URL with an email
parameter.

**Functionality:**

- Takes a URL and an email address as arguments from the command line.
- Encodes the email data using `urllib.parse.urlencode` and sets the
    request body.
- Makes a POST request to the provided URL with the encoded data.
- Handles potential exceptions:
    - HTTPError: If the server responds with an error code, it prints
        a generic error message and the error code.
    - URLError: If there's a network issue or the URL is invalid,
        it prints a generic error message and the reason from the exception.
- If successful, it prints the decoded response body from the server.

"""
import sys
import urllib.parse
from urllib.error import HTTPError, URLError
from urllib import request

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("usage: ./script <url> <email>")
        exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {
        "email": email,
    }

    data = urllib.parse.urlencode(data).encode("ascii")
    req = request.Request(url, data=data)

    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf8'))

    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
