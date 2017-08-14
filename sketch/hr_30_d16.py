#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''za
'''

sys.stdin = io.StringIO(text)
S = input().strip()

try:
    output = int(S)
    print(output)
except:
    print("Bad String")

