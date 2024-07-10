#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an
email parameter in JSON format using the Requests library.

**Functionality:**

- Takes a URL and an email address as arguments from the command line.
- Constructs a JSON object with the email address as the "email" key.
- Makes a POST request to the provided URL with the JSON
    data as the request body.
- Prints the decoded response text from the server.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("usage: ./script <url> <email>")
        exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    print(requests.post(url, data={"email": email}).text)
