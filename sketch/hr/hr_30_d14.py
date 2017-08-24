#!/usr/bin/env python
import sys
import io 

oldstdin = sys.stdin
text = '''3
1 2 5
'''
sys.stdin = io.StringIO(text)

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        for i1 in a:
            for i2 in a:
                diff = abs(i1 - i2)
                if diff > self.maximumDifference:
                    self.maximumDifference = diff

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
