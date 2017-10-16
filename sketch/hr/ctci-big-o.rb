#!/usr/bin/env ruby
#require 'math'

input = <<-eoi
3
12
5
7
eoi
$stdin = StringIO.new(input)
#n,k = gets.strip.split(' ').map(&:to_i)
#a = gets.strip.split(' ').map(&:to_i)

def is_prime?(n)
  return false if n == 1
  (2..Math.sqrt(n)).each do |j|
    if n % j == 0
      return false
    end
  end
  return true 
end

p = gets.strip.to_i
for a0 in (0..p-1)
  n = gets.strip.to_i
  if is_prime?(n)
    puts 'Prime'
  else
    puts 'Not prime'
  end
end
