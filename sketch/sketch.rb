#!/usr/bin/env ruby

def starts_with?(string, start)
  if string =~ /^#{start}/
    return true
  else
    return false
  end
end

did_start = starts_with?('blah', 'bl')
arr = 'howdy'.chars
arr = 'howdy'.scan(/\w/)

m = 'the quick brown fox'.match(/(?<fooo>\w+)/)
puts m.is_a? Array
puts m.class
puts m.names
puts m.captures

m = "paul 12345".match(/(?<name>.*)\s+(?<phone>.*)/)
puts [m: m[:name]]

