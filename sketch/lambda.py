#!/usr/bin/env python
import operator
from functools import reduce

x = [1, 2, 3]
print(list(map(lambda y: y * 2, x)))

z = [5, 4, 3]
w = map(lambda y: y + 1, z)
print(list(w))

print(reduce(lambda x, y: x + y, x))
print(reduce(operator.add, x))
