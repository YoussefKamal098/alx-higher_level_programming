#!/usr/bin/python3
"""
HTTP Request Script

This script makes an HTTP GET request to a specified URL and prints the
response text if the request is successful. If the request fails with
a status code of 400 or greater, it prints an error message with the
status code.

Usage:
    ./script <url>

Arguments:
    <url>  The URL to which the HTTP GET request will be made.

Example:
    ./script https://jsonplaceholder.typicode.com/posts/1

**Functionality:**
    - The script accepts a URL as a command-line argument.
    - If no URL is provided, it prints a usage message and exits.
    - It makes an HTTP GET request to the specified URL.
    - If the response status code is 400 or greater, it prints an error message
      with the status code.
    - If the response is successful (status code less than 400), it prints the
      response text.

Exit Codes:
    1: Script was called without any URL argument.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("usage: ./script <url>")
        exit(1)

    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
