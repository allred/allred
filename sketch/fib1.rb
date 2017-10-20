#!/usr/bin/env ruby
#                     v--- initial val
fib = (1..20).reduce([1]) {|fib| fib << fib.last(2).reduce(:+) }
puts fib: fib

