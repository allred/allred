require_relative 'spec_helper'
require_relative '../solution'

class SolutionTest < Minitest::Test
  def setup
    @solution = Solution.new
  end
  def test_solution
    assert_equal 1, 1 
  end
end
