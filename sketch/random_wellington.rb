#!/usr/bin/env ruby
# break java.util.Random
# 1. determine the outputs of the generator for the first deck (easy)
# 2. determine the state of the generator for the first deck (hard)
# 3. determine the outputs of the generator for the second deck (easy)

# linear congruential generator
class Generator
  A = 0x000000000000000B
  F = 0x00000005DEECE66D
  M = 0x0000FFFFFFFFFFFF

  def initialize(seed)
    super()
    @state = (seed ^ F) & M
    return
  end

  def __next
    return @state = (A + F * @state) & M
  end

  def random(n)
    unless n > 0
      raise ArgumentError.new("n must be positive")
    end
    if n == n & -n
      k = __next >> 17
      return  (n * k) >> 31
    else
      while true
        k = __next >> 17
        r = k % n
        if k - r + n - 1 < 0x80000000
          return r
        end
      end
    end
  end 
end

# shuffle with Fisher-Yates algorithm
module Util
  class << self
    def shuffle(g, n)
      a = Array.new(n)
      j = 0
      while j < n
        k = j + 1
        i = g.random(k)
        if i != j
          a[j] = a[i]
        end
        a[i] = yield(j)
        j = k
      end
      return a
    end
  end
end

class Card
  RANKS = "A23456789TJQK".chars
  SUITS = "♣♦♥♠".chars 

  def initialize(v)
    super()
    @v = v
    return
  end

  def to_s
    return RANKS.fetch(@v >> 2) + SUITS.fetch(@v & 3)
  end
end

class Deck
  N = Card::RANKS.size * Card::SUITS.size

  def initialize(g)
    super()
    @a = Util.shuffle(g, N) { |v| Card.new(v) }
    return
  end

  def to_s
    return @a.join(" ")
  end
end

seed = 0x0000000000000000
g = Generator.new(seed)
=begin
a = Util.shuffle(g, 8) { |v| v }
puts a
#8.times do |j|
#  puts g.random(j + 1)
#end
13.times do |r|
  v = r << 2 | 3
  c = Card.new(v)
  puts c
end
=end
d1 = Deck.new(g)
puts d1
puts " "
d2 = Deck.new(g)
puts d2
