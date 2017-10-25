#!/usr/bin/env ruby
arr = [1, 2, 3, [4, 5, [6], [ ] ] ]

def flatten(array); return array.flatten; end
out = flatten(arr)
puts([out: out])

