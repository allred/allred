#!/usr/bin/env ruby

class Prime
  attr_reader :j 
  def initialize
    @j = "foo" 
  end
end

p = Prime.new
puts p.j
