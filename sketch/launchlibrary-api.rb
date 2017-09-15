#!/usr/bin/env ruby
require 'byebug'
require 'json'
require 'pp'
require 'rest-client'

class Launch 
  attr_reader :url_base, :url_request

  def initialize(args={})
    @mode = args[:mode].to_s
    @url_base = 'https://launchlibrary.net/1.2/'
    @url_request = @url_base + @mode
  end

  def request(args={})
    url_request = args[:url] || @url_request
    return RestClient.get(url_request) 
  end

  def request_json(args={})
    url_request = args[:url] || @url_request
    return JSON.parse(request(url: url_request))
  end

  def printer(args={})
    pp @url_request
  end
end

l = Launch.new(mode: 'launch/next/10')
l.request_json['launches'].each do |r|
  pp n: r['name'], t: r['net'], r: r['rocket']['name']
end
