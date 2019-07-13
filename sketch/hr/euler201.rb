#!/usr/bin/env ruby
# find unique subsets of length k
# print the sum of those subsets whose sums are also unique

input = <<-eoi
6 3
1 3 6 8 10 11
eoi
$stdin = StringIO.new(input)
_, k = gets.strip.split(' ').map(&:to_i)
a = gets.strip.split(' ').map(&:to_i)

# swap elements
subs = []
def subsets(arr, pos, depth, start)
  if pos == depth
    (0..depth-1).each do |i|
      puts i
      subsets.push(arr[i])
    end
    return arr
  end
  (start..arr.length-1).each do |i|
    # when not enough elements left

    if (depth - pos + i > arr.length)
      puts "whoo"
      return
    end

    # swap pos and i

    temp = arr[pos]
    arr[pos] = arr[i]
    arr[i] = temp

    puts a: [temp, arr[pos], arr[i]]
=begin
    subsets(arr, pos+1, depth, i+1)
=end

    # swap back

    temp = arr[pos]
    arr[pos] = arr[i]
    arr[i] = temp
  end
end

subs = subsets(a, 0, k, 0)
puts s: subs
