#!/usr/bin/env ruby

input = <<-eoi
3
1 1 2
eoi
$stdin = StringIO.new(input)
_ = gets.strip.to_i
a = gets.strip.split(' ').map(&:to_i)
freq = Hash.new(0)
a.each do |n|
  freq[n] += 1
end
freq.each do |k, v|
  if v.eql? 1
    puts k
    break
  end
end
