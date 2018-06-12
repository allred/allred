#!/usr/bin/env ruby
require 'rspec/autorun'

class Changer
  def make_change(price: 0, paid: 0)
    puts price, paid
  end

  def coin_counter(denomination: 1, change: 0)
    count = 0
    if change / denomination > 0
      count = (change / denomination).round
    end
    return count
  end
end

RSpec.describe Changer, "#make_change" do
  context "change divisible by 10" do
    it "produces dimes" do
      c = Changer.new
      expect(c.coin_counter(denomination: 10, change: 100)).to eq 10
    end
  end
end
