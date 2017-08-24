#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''4
3 5
2 4
-1 -2
-1 3
'''
sys.stdin = io.StringIO(text)

class Calculator():
    def power(self, int1, int2):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        return pow(int1, int2)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
