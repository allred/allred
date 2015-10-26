#!/usr/bin/ruby
require 'open3'
require 'pp'
require 'pty'

syntax_tshark = "tshark -n -i mon0 subtype probereq"
#syntax_tshark = "tshark -n -e wlan.essid -e frame.number -e wlan.addr -i mon0 -T fields -E separator=, -E quote=d -E occurrence=f subtype probereq"
#syntax_tshark = "tail -f /var/log/syslog"
#Open3.popen3(syntax_tshark) do |stdout, stderr, status, thread|
#  puts stdout.read
#end
#Open3.popen3(syntax_tshark) {|stdin, stdout, stderr, wait_thread|
#  puts stdout.read
#}
begin
  PTY.spawn(syntax_tshark) do |stdout, stdin, pid|
  begin
    stdout.each { |line|
      components = line.chomp().split(',')
      pp components 
    }
  rescue Errno::EIO
    puts "bleh"
  end
  end 
end
