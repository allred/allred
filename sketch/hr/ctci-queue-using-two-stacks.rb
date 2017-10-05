#!/usr/bin/env ruby

input = <<-eoi
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
eoi
$stdin = StringIO.new(input)
queue = []
(1..gets.strip.to_i).each do |_|
  op,n = gets.strip.split(' ').map(&:to_i)
  if op == 1 
    queue.push(n)
  elsif op == 2
    _ = queue.shift
  elsif op == 3
   puts queue[0] 
  end
end
