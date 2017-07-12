#!/usr/bin/env ruby

target = 12
valids = {}
result = []
arr = [1, 3, 7, 9]
arr.each do |n|
  if target - n > 0
    valids[target - n] = true
  end
  if valids[n]
    result = [n, target - n]
  end
end
puts [result: result]
