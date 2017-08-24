#!/usr/bin/env python
# find "hourglasses" and sum their values
import sys
import io 

oldstdin = sys.stdin
text = '''1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''
sys.stdin = io.StringIO(text)
arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

sums = []
for i_o, arr_o in enumerate(arr):
    for i_i, arr_i in enumerate(arr_o):
        arr_top = arr_o[i_i:i_i + 3]
        if len(arr_top) != 3:
            continue
        try:
            val_middle = arr[i_o + 1][i_i + 1]
        except IndexError:
            continue
        try:
            arr_bottom = arr[i_o + 2][i_i:i_i + 3]
        except IndexError:
            continue
        sum_hourglass = sum(arr_top) + val_middle + sum(arr_bottom)
        sums.append(sum_hourglass)
        #print(i_o, {'sum': sum_hourglass, 'top': arr_top, 'middle': val_middle, 'bottom': arr_bottom})
print(max(sums))
