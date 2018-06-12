#!/usr/bin/env ruby

people = {
  :fred => 23,
  :joan => 18,
  :pete => 54,
}

puts people.values.sort
puts people.keys.sort
puts people.sort_by { |name, age| age }
