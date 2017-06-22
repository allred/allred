#!/usr/bin/env ruby
# https://www.reddit.com/r/dailyprogrammer/comments/6grwny/20170612_challenge_319_easy_condensing_sentences/
# https://stackoverflow.com/questions/2070574/is-there-a-reason-that-we-cannot-iterate-on-reverse-range-in-ruby

class Solution
  def truncate(s1, s2)
    return s1 + s2
  end

  def condense(s)
    sentence_condensed = ''
    words = s.split(/\s+/)
    words.each_with_index do |w, i|
      word1 = w.split('')
      if words[i+1]
        word2 = words[i+1].split('')
      else
        sentence_condensed += w
        next
      end
      #puts words[i+1].split('')
      iterator_word2 = 0
      (0..word1.length).reverse_each do |i1|
        # can't continue if strings are non-equal in length
        # also if, yeah.. that
        next if i1 - 1 < 0
        chunk1 = word1[(i1-1)..word1.length-1].join('')
        chunk2 = word2[0 .. iterator_word2].join('')
        next if chunk1.length != chunk2.length
        puts [c1: chunk1, c2: chunk2, i1: i1]
        if chunk1 == chunk2
          truncated_word = truncate(chunk1, chunk2)
          puts [MATCH: [chunk1, chunk2]]
        end
        iterator_word2 += 1
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
