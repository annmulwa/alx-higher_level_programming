#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''


import requests

response = requests.get("https://alx-intranet.hbtn.io/status")
text = response.text
print("Body response:")
print("\t- type: {}".format(type(text)))
print("\t- content: {}".format(text))
