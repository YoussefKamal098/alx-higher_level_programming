#!/usr/bin/python3
"""
This script fetches the response body from a specified URL and
displays basic information about it.

**Functionality:**

- Makes a GET request to the provided URL
    ("https://alx-intranet.hbtn.io/status") using the Requests library.
- Prints details about the response body:
    - Type of the response body data (typically a string).
    - Content of the response body as decoded text
        (assuming UTF-8 encoding).
"""
import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
