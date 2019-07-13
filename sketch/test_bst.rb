#!/usr/bin/env ruby

module BST
  class EmptyNode
    def insert(*)
      false
    end
    def include?(*)
      false
    end
    def delete(*)
      false
    end
  end

  class Node
    attr_reader :value
    attr_accessor :left, :right

    def initialize(v)
      @value = v
      @left = EmptyNode.new
      @right = EmptyNode.new
    end

    def insert(v)
      case value <=> v
      when 1 then insert_left(v)
      when -1 then insert_right(v)
      when 0 then false
      end 
    end

    def include?(v)
      case value <=> v
      when 1 then left.include?(v)
      when -1 then right.include?(v)
      when 0 then true
      end
    end

    def delete(v)
    end

    private

    # if left fails insert (empty), create a new node

    def insert_left(v)
      left.insert(v) or self.left = Node.new(v)
    end

    # if right fails insert (empty), create a new node

    def insert_right(v)
      right.insert(v) or self.right = Node.new(v)
    end
  end
end

tree = BST::Node.new(5)
tree.insert(7)
puts tree.right.inspect

puts tree.include?(10)

