#!/usr/bin/env python
# primes
import sys
import io 

oldstdin = sys.stdin
text = '''3
12
5
7
'''
sys.stdin = io.StringIO(text)

from math import sqrt 
primes_found = {}

def is_prime(n):
    if n == 1:
        return 'Not prime'
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            return 'Not prime' 
    return 'Prime' 

T = int(input())
for i in range(T):
    n = int(input())
    print(is_prime(n))
