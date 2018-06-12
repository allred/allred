#!/usr/bin/env ruby
require 'objspace'

File.open("objspace.txt", "w") do |f|
  ObjectSpace.dump_all(output: f)
end
