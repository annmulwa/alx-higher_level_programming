#!/usr/bin/python3
'''
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
'''


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status = response.status_code
    print(response.text) if status < 400 else print(
        "Error code: {}".format(status))
