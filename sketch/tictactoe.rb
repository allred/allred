#!/usr/bin/env ruby
require 'byebug'
require 'set'

class TicTacToe
  attr_reader :count_wins, :grid, :winner, :win_mode

  def initialize(args)
    @grid = []
    @grid_h = args[:grid_h]
    @grid_v = args[:grid_v]
    (1..@grid_h).each do |x|
      @grid.push(Array.new(@grid_v))
    end
    @count_plays = 0
    @winner = nil
    @win_mode = nil
  end

  def draw?
    @grid.each do |x|
      return false if x.any? {|y| y == nil}
    end
    @win_mode = 'draw'
    return true
  end

  def horizontal_vertical_win?(mode)
    grid = @grid
    grid = @grid.transpose if mode == 'vertical'
    grid.each do |x|
      if array_has_win? x
        @win_mode = mode 
        return true
      end
    end
    return false
  end

  def array_has_win?(arr)
    #byebug
    if arr == Array.new(arr.length, 'x')
      @winner = 'x'
      return true
    elsif arr == Array.new(arr.length, 'o')
      @winner = 'o'
      return true
    end
    return false
  end

  def diagonal_win?
    index_diag = 0
    diag1 = []
    diag2 = []
    @grid.each_with_index do |x, i|
       diag1.push(x[index_diag])
       index_diag += 1
    end
    index_diag = @grid_h - 1
    @grid.each_with_index do |x, i|
       diag2.push(x[index_diag])
       index_diag -= 1
    end
    if array_has_win?(diag1)
      @win_mode = 'diag_desc'
      return true
     elsif array_has_win?(diag2)
      @win_mode = 'diag_asc'
      return true
    end 
    return false
  end

  def randplay(sigil)
    rand_h = rand(@grid_h)
    rand_v = rand(@grid_v)
    if @grid[rand_h][rand_v] == nil
      @grid[rand_h][rand_v] = sigil
      return true, [rand_h, rand_v]
    else
      return false, [rand_h, rand_v]
    end
  end

  def game_over? 
    return true if draw?
    return true if horizontal_vertical_win?('horizontal')
    return true if horizontal_vertical_win?('vertical')
    return true if diagonal_win?
    return false
  end

  def PlayAutomatically()
    sigil = 'x'
    until game_over? 
      played = false
      until played
        played, _ = randplay(sigil)
        @count_plays += 1
      end
      sigil = sigil == 'x' ? 'o' : 'x'
    end
    return [winner: @winner, plays: @count_plays, win_mode: @win_mode]
  end
end

out = [] 
count_runs = 0
win_mode = nil
grid = []
until win_mode =~ /diag/
  t = TicTacToe.new(grid_h: 3, grid_v: 3)
  out = t.PlayAutomatically()
  win_mode = t.win_mode
  count_runs += 1
  if count_runs % 10000 == 0
    puts [count_runs, out]
  end
  grid = t.grid
end
puts [runs: count_runs, out: out]
puts [grid: grid]
