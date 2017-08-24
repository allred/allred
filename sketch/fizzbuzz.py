#!/usr/bin/env python
# print out numbers 1 to 100 (inclusive)
# if the number is divisible by 3, print Fizz instead of the number
# if the number is divisible by 5, print Buzz
# if it's divisible by both 3 and 5, print FizzBuzz

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
