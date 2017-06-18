#!/usr/bin/env ruby
# https://www.reddit.com/r/dailyprogrammer/comments/6grwny/20170612_challenge_319_easy_condensing_sentences/
# https://stackoverflow.com/questions/2070574/is-there-a-reason-that-we-cannot-iterate-on-reverse-range-in-ruby

class Solution
  def condense(s)
    sentence_condensed = ''
    words = s.split(/\s+/)
    words.each_with_index do |w, i|
      unless words[i+1]
        sentence_condensed += w
      end
      word1 = w.split('')
      (0..word1.length).reverse_each do |i1|
        # need to iterate from the end of word 1
        # and increase the length to find longest match
        puts i1
        chunk1 = word1[i1..word1.length-1].join('')
        puts [d: chunk1]
      end
    end
    return sentence_condensed
  end
end

s = 'I heard the pastor sing live verses easily.'
sentence = Solution.new.condense(s)
puts [s1: s]
puts [s2: sentence]

=begin
class Solution
  def initialize(args={})
  end
  def condense(s)
    #/(?=foo)/.match(s)
    condensed = [] 
    sentence_condensed = ''
    words = s.split(/\s+/)
    words.each_with_index do |w, i|
      next unless w
      chars1 = w.split('')
      #(r.first).downto(r.last).each do |i|
      was_condensed = false
      if words[i+1]
        chars2 = words[i+1].split('')
        index = 0
        (chars1.length-1).downto(0).each do |i|
          if chars2[index]
            puts [d: [chars1[i], chars2[index]]]
            if chars1[i] == chars2[index]
              chars1.delete_at(i)
              was_condensed = true
            end
          end
          index += 1
        end
        word_condensed = ''
        if was_condensed
          word_condensed = chars1.join('') + chars2.join('')
          words[i+i] = word_condensed
        else
          word_condensed = chars1.join('')
        end
        condensed.push(word_condensed)
      end
    end
    sentence_condensed = condensed.join(' ')
    return sentence_condensed
  end
end
=end

=begin
    if match ="howdy dere pardner".match(/(\S+)/)
      one, two, three = match.captures
      puts one
    end
=end
