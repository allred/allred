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
    print(k-1 if ((k-1) | k) <= n else k-2)
    '''
    vals = []
    for x in range(1, n):
        for y in range(x + 1, n + 1):
            result = x&y
            if result < k:
                vals.append(result)
    print(max(vals))
    '''
