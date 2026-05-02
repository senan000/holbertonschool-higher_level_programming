#!/usr/bin/python3
"""Star Wars search."""
import sys
import requests

if __name__ == "__main__":
    r = requests.get(
        "https://swapi.co/api/people",
        params={"search": sys.argv[1]}
    ).json()

    print("Number of results: {}".format(r.get("count")))
    for p in r.get("results"):
        print(p.get("name"))
