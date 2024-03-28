#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''


import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = "http://0.0.0.0:5000/search_user"

    res = requests.post(url, data={'q': q})
    try:
        res_dict = res.json()
        id, name = res_dict.get('id'), res_dict.get('name')
        if len(res_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
