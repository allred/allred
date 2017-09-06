#!/usr/bin/env ruby
# minimum number of deletions to attain an anagram

input = <<-eoi
cde
abc
eoi
$stdin = StringIO.new(input)
a = gets.strip
b = gets.strip

def number_needed(string_a, string_b)
  deletions = 0
  freq = Hash.new(0) 
  string_a.split('').each {|c| freq[c] += 1 }
  string_b.split('').each {|c| freq[c] -= 1 }
  deletions = freq.values.map(&:abs).sum
  puts deletions
end
number_needed(a, b)

=begin
a = a.split('')
b = b.split('')
a_size_orig = a.length
b_size_orig = b.length
deletions = 0
a.delete_if { |c| !b.include? c }
deletions += a_size_orig - a.length 
puts "#{a} #{b}"
b.delete_if { |c| !a.include? c }
deletions += b_size_orig - b.length 
#puts "#{a} #{b} #{deletions}"
puts deletions
=end
