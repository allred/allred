#!/usr/bin/env ruby

input = <<-eoi
5 4
1 2 3 4 5
eoi
$stdin = StringIO.new(input)

n,k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)

(1..k).each do |n|
  a.push(a.shift)
end
puts a.join(' ')
