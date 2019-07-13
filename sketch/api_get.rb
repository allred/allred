#!/usr/bin/env ruby
require 'net/http'
require 'json'

uri_base = 'http://jservice.io/api/random'
uri = URI(uri_base)
r = Net::HTTP.get(uri)
jp = JSON.parse(r)
puts "category: #{jp[0]['category']['title']}"
puts "clue: #{jp[0]['question']}"
puts "answer: #{jp[0]['answer']}"
