#!/usr/bin/env ruby
#                     v--- initial val
fib = (1..20).reduce([1]) {|fib| fib << fib.last(2).reduce(:+) }
puts fib: fib

# where n is the nth number in the fibbonaci sequence
def fib(n, memo = {})
  if n == 0 || n == 1
    return n
  end
  memo[n] ||= fib(n-1, memo) + fib(n-2, memo)
end
puts fib(124)
