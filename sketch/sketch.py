#!/usr/bin/env python
import re

arr = [1, 4, 8, 9, 7, 5]

def e_arr():
    for i, v in enumerate(arr):
        yield (i, v)

for i, v in e_arr():
    print(i, v)

match = re.search('(?P<name>.*)\s+(?P<phone>.*)', 'paul 12345')
name = match.group('name')
phone = match.group('phone')
print(name, phone)

m = re.findall('H', 'hHhHH')
print(len(m))
