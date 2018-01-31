#!/usr/bin/env ruby

names = [
  "Bob's Diner",
  "bob's Diner",
  "Bob's Diner",
  "Bob's Diner",
  "bob's Diner",
  "bobsdiner",
]

out = names.reduce(Hash.new(0)) {|memo, word| memo[word] += 1; memo}
puts o: out

=begin
freq = Hash.new(0) 
names.map {|a| freq[a] += 1 }
puts o: freq.sort_by {|k, v| -v}.take(1)[0][0]
=end
