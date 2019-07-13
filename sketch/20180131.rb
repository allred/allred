#!/usr/bin/env ruby
require 'json'
require 'rest-client'
require 'minitest/autorun'

class Api 
  attr_reader :num_pokemon
  @@num_pokemon = 802
  @@api_uri_base = "http://pokeapi.co/api/v2"

  def initalize(args=[])
    @data = {} 
  end

  def gen_rand
    num_rand = rand(@@num_pokemon + 1)
    uri = "#{@@api_uri_base}/pokemon/#{num_rand}/"
    @data = JSON.parse(RestClient.get(uri))
  end
end

class Pokemon
  attr_reader :hp

  def initialize(args=[])
    @hp = 0
  end
end

class PokemonTest < Minitest::Test
  def setup
    @p = Pokemon.new
    @a = Api.new
  end

  def test_gen_rand
    mon = @a.gen_rand 
    assert mon.is_a? Hash
  end

  def test_hp
    assert_equal @p.hp, 0
  end
end
