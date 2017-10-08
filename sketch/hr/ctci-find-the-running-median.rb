#!/usr/bin/env ruby

input = <<-eoi
6
12
4
5
3
8
7
eoi
$stdin = StringIO.new(input)

class PriorityQueue
  attr_reader :elements

  def initialize
    @elements = []
  end

  def <<(element)
    @elements << element
    bubble_up(@elements.size - 1)
  end

  def bubble_up(index)
    parent_index = (index / 2)
    #require 'byebug'; byebug
    return if index <= 1
    return if @elements[parent_index] >= @elements[index]
    exchange(index, parent_index)
    bubble_up(parent_index)
  end

  def bubble_down(index)
    child_index = (index * 2)
    return if child_index > @elements.size - 1
    not_the_last_element = child_index < @elements.size - 1
    left_element = @elements[child_index]
    right_element = @elements[child_index + 1]
    child_index += 1 if not_the_last_element && right_element > left_element
    return if @elements[index] >= @elements[child_index]
    exchange(index, child_index)
    bubble_down(child_index)
  end

  def exchange(source, target)
    @elements[source], @elements[target] = @elements[target], @elements[source]
  end

  def pop
    exchange(1, @elements.size - 1)
    max = @elements.pop
    bubble_down(1)
    max
  end
end

n = gets.strip.to_i
a = Array.new(n)
pq = PriorityQueue.new
require 'set'
sorted = SortedSet.new([])
for a_i in (0..n-1)
  a[a_i] = gets.strip.to_i
  sorted.add(a[a_i])

  a2 = []
  sorted.each do |e|
    a2 << e
  end
  if (a_i + 1) % 2 == 0
    left = a2[(a_i + 1)/2 - 1]
    right = a2[(a_i + 1)/2]
    median = (left.to_f + right.to_f) / 2
    puts median.to_f
  else
    median = a2[(a_i + 1)/2]
    puts median.to_f
  end

end


