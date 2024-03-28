#!/usr/bin/python3
'''
Python script that takes 2 arguments in order to solve this challenge.
'''


import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=": ")
        print(commit.get('commit').get('author').get('name'))
