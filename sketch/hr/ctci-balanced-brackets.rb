#!/usr/bin/env ruby

input = <<-eoi
3
{[()]}
{[(])}
{{[[(())]]}}
eoi
$stdin = StringIO.new(input)
#n,k = gets.strip.split(' ').map(&:to_i)
#a = gets.strip.split(' ').map(&:to_i)

@matchers = {
  '(' => ')',
  '{' => '}',
  '[' => ']',
}
def is_balanced(expression)
  stack = []
  expression.split('').each do |c|
    if @matchers.key?(c)
      stack.push(@matchers[c])
    else 
      if stack.length == 0 || c != stack[stack.length - 1]
        return false
      end
      stack.pop()
    end
  end
  return stack.length == 0
end

t = gets.strip.to_i
for a0 in (0..t-1)
  expression = gets.strip
  if is_balanced(expression)
    puts 'YES'
  else
    puts 'NO'
  end
end
