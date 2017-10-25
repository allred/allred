#!/usr/bin/env ruby
# https://www.hackerrank.com/challenges/crossword-puzzle/problem

input = <<-eoi
+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA
eoi
$stdin = StringIO.new(input)
#n,k = gets.strip.split(' ').map(&:to_i)
#a = gets.strip.split(' ').map(&:to_i)
board_initial = []
boards_valid = []
(1..10).each do |l|
  line = gets.strip
  board_initial.push(line.split(''))
end
words = gets.strip.split(';').map{ |w| w.split('') }

def max_length_horizontal_dashes(line)
  line.chunk { |x| x == '-' || nil }.map { |_, x| x.size }.max 
end

def fit_word_in_board(word, board)
  # check for horizontal fit
  board.each do |line|
    length_open_horizontal = 0
    puts "#{line} #{max_length_horizontal_dashes(line)} #{word.length}"
  end
end

result = fit_word_in_board(words[0], board_initial)
#puts result
