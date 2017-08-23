#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''3
5 2
8 5
2 2
'''
sys.stdin = io.StringIO(text)
import itertools
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    for x in itertools.product(range(1,n), range(2, 3)):
        print(x)
