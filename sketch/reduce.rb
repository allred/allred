#!/usr/bin/env ruby

def sum(first, *rest)
  rest.reduce(first){|o,x| o+x}
end

puts sum(1, 7)
