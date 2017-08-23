#!/usr/bin/env python
# fine for book return
import sys
import io 

oldstdin = sys.stdin
text = '''9 6 2015
6 6 2015
'''
sys.stdin = io.StringIO(text)

def determine_fine(diff_d, diff_m, diff_y):
    if diff_y < 0:
        return 0
    if diff_y <= 0 and diff_m <= 0 and diff_d <= 0:
        return 0
    if diff_d > 0 and diff_m == 0 and diff_y ==0:
        return diff_d * 15
    if diff_m > 0 and diff_y == 0:
        return diff_m * 500
    if diff_y > 0:
        return 10000

date_returned = [int(x) for x in input().strip().split(' ')]
date_expected = [int(x) for x in input().strip().split(' ')]
diff_d = date_returned[0] - date_expected[0]
diff_m = date_returned[1] - date_expected[1]
diff_y = date_returned[2] - date_expected[2]

fine = determine_fine(diff_d, diff_m, diff_y)
print(fine)
