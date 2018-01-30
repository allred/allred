#!/usr/bin/env ruby
require 'json'
require 'rest-client'


class Pokemon
  attr_reader :data

  def initialize(args=[])
    @num_pokemon = 802 
    @uri_base = "http://pokeapi.co/api/v2"
    @data = self.gen_rand 
  end

  def gen_rand
    num_rand = rand(@num_pokemon + 1)
    uri = "#{@uri_base}/pokemon/#{num_rand}/"
    @data = JSON.parse(RestClient.get(uri))
  end

  def get_hp
  end

end

mon1 = Pokemon.new 
mon2 = Pokemon.new 

name1 = mon1.data.fetch("name")
name2 = mon2.data.fetch("name")

puts name1, name2
