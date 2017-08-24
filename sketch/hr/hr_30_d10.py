#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''13
'''
sys.stdin = io.StringIO(text)
n = input().strip()
base2 = bin(int(n))
consecutives = {}
index = 0
for i, n in enumerate(base2.strip('^0b')):
    if int(n) == 1:
        consecutives.setdefault(index, 0)
        consecutives[index] += 1
    else:
        index += 1 
print(max(consecutives.values()))


