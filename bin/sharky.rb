#!/usr/bin/ruby
# purpose: de-dupe filter for tshark probe request listener
require 'json'
require 'pp'
require 'pty'
STDOUT.sync = true

syntax_tshark = "tshark -n -i mon0 subtype probereq"
#syntax_tshark = "tshark -n -e wlan.essid -e frame.number -e wlan.addr -i mon0 -T fields -E separator=, -E quote=d -E occurrence=f subtype probereq"

$database = {}
begin
  PTY.spawn(syntax_tshark) do |stdout, stdin, pid|
  begin
    stdout.each { |line|
      if line !~ /^\s*\d/
        next
      end
      components = line.chomp().strip().split(',')
      t_elapsed, mac_source = components[0].split(/\s+/)
      _, ssid = components[4].split('=')
      index = "#{mac_source}_#{ssid}"
      unless $database[index]
        $database[index] = t_elapsed
        puts JSON.generate({:t_elapsed => t_elapsed, :mac_source => mac_source, :ssid => ssid})
      end
    }
  rescue Errno::EIO
    puts "bleh"
  end
  end 
end
