#!/usr/bin/python3
"""
This script retrieves and prints the 10 most recent commits of a
given GitHub repository.

Usage:
    ./script <repository_name> <owner_name>

Arguments:
    repository_name: The name of the GitHub repository (e.g., "requests").
    owner_name: The owner of the GitHub repository (e.g., "psf").

**Functionality:**
    The script takes two command-line arguments: the name
    of the repository and the owner's username.
    It then constructs a URL to fetch the commits of the specified
    repository from the GitHub API.
    The script makes a GET request to this URL and retrieves the
    list of commits in JSON format.
    It then prints the SHA and author name of the first 10 commits.

Examples:
    ./script requests psf
    This command retrieves and prints the 10 most recent commits for the
    "requests" repository owned by "psf".

Error Handling:
    If fewer than two arguments are provided, the script prints
    a usage message and exits.
    If the repository has fewer than 10 commits, the script will
    handle the IndexError gracefully and stop printing.

Requirements:
    The 'requests' module must be installed in the Python environment.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("usage: ./script <repository_name> <owner_name>")
        exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print(f"{commits[i].get('sha')}: "
                  f"{commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
