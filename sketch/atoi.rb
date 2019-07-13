#!/usr/bin/env ruby

def atoi(str)
  int = 0
  multiplier = 1
  str.chars.reverse.each do |c|
    int += c.to_i * multiplier
    multiplier *= 10
  end
  return int
end

puts r: atoi("991")
