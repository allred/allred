require_relative 'spec_helper'
require_relative '../solution'

class SolutionTest < Minitest::Test
  def setup
    @solution = Solution.new
    @sentence1 = 'I heard the pastor sing live verses easily.'
    @condensed1 = 'I heard the pastor sing liverses easily. '
    @sentence2 = 'Deep episodes of Deep Space Nine came on the television only after the news.' 
    @condensed2 = 'Deepisodes of Deep Space Nine came on the televisionly after the news.'
    @sentence3 = 'Digital alarm clocks scare area children.'
    @condensed3 = 'Digitalarm clockscarea children.'
  end
  def test_solution
    assert_equal @solution.condense(@sentence1), @condensed1 
  end
end
