#!/usr/bin/env ruby
require 'ipaddr'

def ip_to_color(ip)
  hex = IPAddr.new("74.65.200.253").to_i.to_s(16)
  components = []
  hex.scan(/(\w\w)/).each do |x|
    components.push(x.first)
  end
  return components[1,3].join('')
end

puts ip_to_color("74.65.200.253")
