#!/usr/bin/env ruby

command = './tictactoe.rb'
output = ''
until output =~ /diag/
  output = `#{command}`
  puts output
end
