#!/usr/bin/env ruby

def flatten(array, accum=[])
  array.each do |a|
    if a.is_a? Array
      flatten(a, accum)
    else
      accum.push(a)
    end
  end
  return accum
end

flat = flatten([1, 2, [3]])
puts [f: flat]
