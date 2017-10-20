#!/usr/bin/env ruby

chars = 'Thickly'.chars
# map receives [bool, arr]
first_consonants = chars.chunk {|x| x !~ /[aeiou]/}.map {|_, x| x }
puts f: first_consonants[0]
