#!/usr/bin/python3
"""
This script imports utility functions for working with JSON
in Python and adds command-line arguments to a JSON file.

Usage:
- Run the script from the command line, providing the
  desired data to be added as command-line arguments.

Example:
```bash
python script.py item1 item2 item3
```
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError or PermissionError:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, "add_item.json")
