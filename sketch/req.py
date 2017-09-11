#!/usr/bin/env python
import requests
r = requests.get('http://dpaste.com/3NX4EXA.txt')
for owners in r.json().values():
    for owner in owners:
        print(owner)
