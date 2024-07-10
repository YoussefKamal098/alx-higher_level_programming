#!/usr/bin/python3
"""
GitHub User ID Fetch Script

This script fetches the GitHub user ID of the user provided through
command-line arguments by using Basic Authentication.

Usage:
    ./script <username> <token>

Arguments:
    <username>  The GitHub username.
    <token>     The GitHub personal access token.

Example:
    ./script myusername mytoken123

**Functionality:**
    - The script accepts two command-line arguments: username
        and personal access token.
    - It uses these credentials to authenticate with the GitHub API
        using Basic Authentication.
    - The script makes an HTTP GET request to "https://api.github.com/user"
        to fetch user details.
    - It parses the JSON response and prints the user ID.

Requirements:
    - The 'requests' module must be installed.
    - A valid GitHub username and personal access token must be provided.

Exit Codes:
    The script does not explicitly set exit codes for different
    error conditions.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    auth = sys.argv[1], sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
