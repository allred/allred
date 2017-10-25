require_relative 'test_helper'
require 'minesweeper'

class MineSweeperTest < Minitest::Test
  def setup
    @size = 4
    @ms = MineSweeper.new(size: @size, num_mines: 2)
  end

  def _test_play_lost
    move = [rand(@ms.size), rand(@ms.size)]
    @ms.mines_locations << move 
    @ms.play(*move)
    assert_equal true, @ms.lost
  end

  def _test_play_not_lost
     move = [0, 1]
     @ms.mines_locations.delete(move)
     @ms.play(*move)
     assert_equal false, @ms.lost
  end

  def test_display
     size = 6
     mines = 5
     moves = 2
     d = MineSweeper.new(size: size, num_mines: mines)
     (1..moves).each do |_|
       break if d.lost
       move = [rand(size), rand(size)]
       puts [move: move]
       d.play(*move)
       d.display
     end
  end

  def test_size
    assert_equal @size, @ms.size
  end

  def strio(input)
    $stdin = StringIO.new(input)
  end
end
