#!/usr/bin/env ruby

header_read = false
col_names = []
count = 0
File.open("pokemon.csv", "r") do |f|
  f.each_line do |l|
    row = l.chomp.split(',')
    unless header_read
      col_names = row
      header_read = true
      next
    end
    count += 1
    pdata = row.each_with_index.map {|d,i| [col_names[i], d] }.to_h
    puts pdata
  end
end
puts count
