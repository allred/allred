#!/usr/bin/env ruby

a = ['one', 'two', 'three']

a.each_with_index do |w,i|
  puts [d: [w, i]]
  if i == 1
    a.insert(i+1, 'four')
  end
end

# suggestions for Austin TX:
# mickelthwait
# la barbeque
# ramen tatsuya
# mi madres
# vera cruz
# jackalope
# texas chili parlor
# el chilito
# hut's
# yellowjacket: frito pie
