#!/usr/bin/env ruby
# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

class Solution
  def spiral(n)
    spiral = ''
    (1..n**2).each do |f|
      spiral += "#{f} "
    end
    return spiral
  end
end

puts Solution.new.spiral(5)
