#!/usr/bin/env python
from collections import defaultdict, Counter

def fizzbuzz():
  for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
      print("{0} FizzBuzz".format(str(n)))
    elif n % 3 == 0:
      print("{0} Fizz".format(str(n)))
    elif n % 5 == 0:
      print("{0} Buzz".format(str(n)))
    else:
      print(n)

def palindrome(s):
  arr = list(s) 
  is_palindrome = True

  if arr[0:(int(len(arr)/2)) != arr[(int(len(arr[::-1])/2)):len(arr)-1]:
      is_palindrome = False
  return is_palindrome

  for idx, val in enumerate(arr):
    if arr[idx] != arr[(len(arr) - 1) - idx]:
      is_palindrome = False 
  return is_palindrome

#print(palindrome('racecar'))

def permutation(s):
  arr = list(s)
  is_permutation = True
  #counts = defaultdict(int) 
  counts = Counter()
  count_odd = 0
  for idx, val in enumerate(arr):
    counts[val] += 1
  for key, val in counts.items():
    if val % 2 != 0:
      count_odd += 1
  if count_odd > 1:
    is_permutation = False
  return is_permutation
    
print(permutation('rraac'))
