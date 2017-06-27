#!/usr/bin/env ruby
# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/
require 'bundler/setup'

class Solution
  def spiral(n)
    spiral = ''
    # build a multi-dimensional array?
    (1..n**2).each do |f|
      len = f.to_s.length
      spiral += "#{f} "
      if f % n == 0
        spiral += "\n"
      end
    end
    return spiral
  end
end

puts Solution.new.spiral(5)
