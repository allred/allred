#!/usr/bin/env ruby

def fizzbuzz(num)
  case
  when num % 15 == 0
    puts "FizzBuzz"
  when num % 3 == 0
    puts "fizz"
  when num % 5 == 0
    puts "buzz"
  else
    puts num
  end
end

def fizzbuzzer(min, max)
  #min.upto(max).each {|n| fizzbuzz(n)}
  (min..max).each {|n| fizzbuzz(n)}
end

fizzbuzzer(1, 20)
