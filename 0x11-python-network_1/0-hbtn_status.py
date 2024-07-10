#!/usr/bin/python3
"""
This script fetches the response body from a specified URL and displays
information about it.

**Functionality:**

- Makes a GET request to the provided
    URL ("https://alx-intranet.hbtn.io/status").
- Reads the response body from the opened URL connection.
- Prints details about the response body:
    - Type of the response body data.
    - Content of the response body as raw bytes.
    - Decoded content of the response body as a string using UTF-8 encoding.
"""
from urllib import request

if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")

    with request.urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf8')}")
