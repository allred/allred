#!/usr/bin/env ruby

class Node
  attr_reader :value
  attr_accessor :left, :right

  def initialize(v)
    @value = v
    @left = nil
    @right = nil
  end
end

class BST
  attr_accessor :root

  def initialize(root_val=nil)
    @root = Node.new(root_val)
  end

  def insert(node, v)
    if node.value == value
      return node
    elsif value < node.value
      insert(node.left, value)
    elsif value > node.value
      insert(node.right, value)
    else
      return node = Node.new(value)
    end
  end
end

bst = BST.new(5)
bst.insert(4)
puts bst.inspect
