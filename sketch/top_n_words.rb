#!/usr/bin/env ruby

def top_n_words(text, n_words)
  freq = Hash.new(0)
  text.split(/\W*\b\W*/).map(&:downcase).each do |w|
    freq[w] += 1
  end
  freq.sort_by {|x| [-x[1], x[0]]}.take(n_words)
end

paragraph = "Some text: is here and here and there are some words.  Some other words are here.  However; There you have it."

puts top_n_words(paragraph, 3)
