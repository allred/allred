#!/usr/bin/env ruby

text = 'reviver'

array = text.split('')
palindrome = true 
array.each_with_index do |c, i|
  start = array[0..i]
  xend = array[array.length - (i + 1) .. -1]
  if start != xend.reverse
    palindrome = false
  end

  puts "start: #{start.join('')}"
  puts "end: #{xend.join('')}"
end
puts "palindrome: #{palindrome}"
