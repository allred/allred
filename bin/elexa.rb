#!/usr/bin/env ruby
# purpose: webserver front end to generate and speak alexa commands
# aplay -L to get audio device
require 'sinatra'

configure do
  @@dir_scripts = File.expand_path File.dirname(__FILE__)
  @@wake_word = 'alexa'
  @@wake_word = 'ahlexah.'
  @@device_audio = "plughw:CARD=PCH,DEV=0"
end

def espeak(phrase)
  cmd = <<-eoc
    #{@@dir_scripts}/es "#{@@wake_word} #{phrase}"
  eoc
    #espeak -v en-us -m '#{@@wake_word} <break time="2s"/> #{phrase}' --stdout | aplay -D #{@@device_audio}
  puts [c: cmd]
  system cmd
  cmd
end

get '/bedroom_on' do
  espeak('bed room on')
end
