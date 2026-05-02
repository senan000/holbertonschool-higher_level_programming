#!/usr/bin/python3
"""Displays X-Request-Id header."""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers.get("X-Request-Id"))
