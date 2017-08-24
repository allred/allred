#!/usr/bin/env python
input = [2, 'Hacker', 'Rank']

n = input.pop(0)
for word in input:
  evens = []
  odds = []
  for i, letter in enumerate(list(word)):
    if i % 2 == 0:
      evens.append(letter)
    else:
      odds.append(letter)
  print("{} {}".format("".join(evens), "".join(odds)))
  print('%s %s' % ('x', 'y'))
