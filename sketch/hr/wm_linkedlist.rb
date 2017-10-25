#!/usr/bin/env ruby
# remove nodes larger than x (last number in input)

input = <<-eoi
5
1
2
3
4
5
3
eoi
$stdin = StringIO.new(input)

class Node
  attr_accessor :data, :next
  def initialize(data)
    @data = data
    @next = nil
  end
end

class Solution
  def insert(head, value)
    p = Node.new(value)
    if head == nil
      head = p
    elsif head.next == nil
      head.next = p
    else
      current = head
      while current.next != nil
        current = current.next
      end
      current.next = p
    end
    return head
  end

  def display(head)
    current = head
    while current
      puts current.data, " "
      current = current.next
    end
  end
end

#n,k = gets.strip.split(' ').map(&:to_i)
#a = gets.strip.split(' ').map(&:to_i)

mylist = Solution.new
head = nil
T = gets.to_i
(1..T).each do |_|
  data = gets.to_i
  head = mylist.insert(head, data)
end
x = gets.to_i

def removeGreater(list, x)
  if list.data > x
    return removeGreater(list.next)
  end
  if list.next.data > 5
    list.next = list.next.next
    return removeGreater(list.next)
  end
  return list 
end

res = removeGreater(head, x)
while res
  puts res.data
  res = res.next
end
