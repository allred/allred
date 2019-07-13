#!/usr/bin/env ruby
class ChainLink
  attr_accessor :left, :right

  def append(link)
    raise "Link is already connected" unless @right.nil?
    @right = link
    link.left = self
  end

  def longer_side
    object_ids = {}
    left_count = 0
    right_count = 0
    right = self.right
    left = self.left 
    while right
      right_count += 1
      object_ids[right.object_id] = true
      if object_ids[right.right.object_id]
        return nil
      end
      right = right.right
    end
    while left
      object_ids[left.object_id] = true
      if object_ids[left.left.object_id]
        return nil
      end
      left_count += 1
      left = left.left
    end
    if left_count > right_count
      return :left
    elsif right_count > left_count
      return :right
    end
    return nil
  end

end

link = ChainLink.new.append(ChainLink.new.append(ChainLink.new))
puts link.longer_side == :right
