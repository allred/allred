#!/usr/bin/env ruby

text = <<-eoc
i think i went speeding by that stop sign.  you were in the pepperoni lovers lane.  Veggie pan pizza straight from the oven.  I'm going ahead and crowning the winner.  We're all winners really.  It has a french toast quality to it.  Here's the real test.  The dough has a slight moisture to it.  We really did reverse engineer the best of Pizza hut.  It's also unique.  I'm not just saying that.
eoc

freq = Hash.new{|h,k| h[k] = 0} 
text.split(/\s+/).each do |w|
  w.gsub!(/[.]$/, '')
  freq[w.downcase] += 1 
end
puts Hash[freq.sort_by {|k, v| -v}]
