#!/usr/bin/env ruby

input = <<-eoi
6 4
give me one grand today night
give one grand today
eoi
$stdin = StringIO.new(input)
#n,k = gets.strip.split(' ').map(&:to_i)
#a = gets.strip.split(' ').map(&:to_i)

m,n = gets.strip.split(' ')
m = m.to_i
n = n.to_i
magazine = gets.strip
magazine = magazine.split(' ')
ransom = gets.strip
ransom = ransom.split(' ')

def ransom_valid(ransom, magazine)
  ransom_freq = Hash.new(0) 
  magazine_freq = Hash.new(0)
  ransom.each {|word| ransom_freq[word] += 1}
  magazine.each {|word| magazine_freq[word] += 1}
  ransom_freq.each do |k, v|
    if !magazine_freq.key? k or magazine_freq[k] < ransom_freq[k]
      return 'No'
    end
  end
  #print "#{ransom_freq} #{magazine_freq}"
  return 'Yes'
end
puts ransom_valid(ransom, magazine)
