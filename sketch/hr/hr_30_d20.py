#!/usr/bin/env python
# bubble sort
import sys
import io 

oldstdin = sys.stdin
text = '''3
3 2 1
'''
sys.stdin = io.StringIO(text)
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

num_swaps = 0
for i in range(n):
    for j in range(0, n - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            num_swaps += 1
    if num_swaps == 0:
        break

print("Array is sorted in {} swaps.".format(num_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
