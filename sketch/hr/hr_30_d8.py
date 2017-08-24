#!/usr/bin/env python
import re

input = '''3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
'''.split('\n')

phonebook = {}
num_records = input.pop(0)
for line in input[0:int(num_records)]:
  try:
    (name, number) = re.split('\s', line)
    phonebook[name] = number
  except ValueError:
    pass

#print(phonebook)
for query in input[int(num_records):len(input) - 1]:
  if phonebook.get(query):
    print(f'{query}={phonebook[query]}')
  else:
    print("Not found")
