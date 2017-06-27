require_relative 'spec_helper'
require_relative '../solution'

class SolutionTest < Minitest::Test
  def setup
    @solution = Solution.new
    @tests = {
      5 => <<-eoc
 1  2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
      eoc
    }
  end
  def test_solution
    @tests.keys.each do |k|
      assert_equal @tests[k], @solution.spiral(k) 
    end
  end
end
