#!/usr/bin/env ruby

def prime?(n)
    if n == 1
        return false
    end
    upper = Math.sqrt(n).to_i
    (2..upper).each do |x|
        if n % x == 0
            return false
        end
    end
    return true
end

(1..20).each do |n|
  puts [n: n, p: prime?(n)]
end
