#!/usr/bin/ruby
# purpose: 
# * de-dupe filter for tcpdump probe request listener (tshark hangs a lot)
# * provide a facility for logging probe data remotely via rsyslog over udp
require 'json'
require 'pp'
require 'pty'
require 'remote_syslog_logger'
STDOUT.sync = true

syntax_tshark = "tcpdump -i mon0 -tttt -e -s 256 type mgt subtype probe-req"
$logger = nil
if ARGV[0]
  log_host = ARGV[0]
  $logger = RemoteSyslogLogger.new(log_host, 514)
  $logger.formatter = proc do |severity, datetime, progname, msg|
    "#{msg}\n"
  end
end

$database = {}
begin
  PTY.spawn(syntax_tshark) do |stdout, stdin, pid|
  begin
    stdout.each { |line|
      if line !~ /^\s*\d/
        next
      end
      components = line.chomp().strip().split(/\s+/)
      line =~ /^(\S+ \S+)/
      t_stamp = $1
      line =~ /(SA:\S+)/
      _, mac_source = $1.split(/^.*?\:/)
      if !mac_source
        next
      end
      line =~ /Probe Request \((.*?)\)/
      ssid = $1
      index = "#{mac_source}_#{ssid}"
      unless $database[index]
        $database[index] = t_stamp
        string_json = JSON.generate({:t_stamp => t_stamp, :mac_source => mac_source, :ssid => ssid})
        puts string_json
        if $logger
          $logger.info(string_json)
        end
      end
    }
  rescue Errno::EIO
    puts "bleh"
  end
  end 
end
