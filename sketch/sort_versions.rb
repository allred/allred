#!/usr/bin/env ruby

versions = %W( 
  0.1.0.8.9
  0.1.0.9
  0.0.0.1
  1.0.0
  3.0.1
  12.3
  2.0.0
)

def compare_version(a)
  arr = a.split('.')
  puts "#{arr}"
  return arr
end

versions.sort { |a,b| Gem::Version.new(a) <=> Gem::Version.new(b) }.each do |v|
  puts v
end
