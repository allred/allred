#!/usr/bin/ruby -w
# utility methods for aircrack helper suite
# 1. airscan [run briefly to detect APs]
# 2. airlisten SomeESSIDname [keep this running to capture IVs]
# 3. airauth SomeESSIDname [auth and keepalive for fake association]
# 4. aircrack SomeESSIDname
require 'csv'
require 'fileutils'
require 'pp'

$hostname = `hostname`.chomp
$dir_output = '/home/mallred/aircrack'
$iface_crack = 'wlan1'
#$mac_iface_crack = '00:c0:ca:27:4e:c4' # alfa on balzac? 
$mac_iface_crack = '00:c0:ca:27:4e:c3' # alfa on balzac? 
if ($hostname == 'djinn') then
  $iface_crack = 'wlan0'
end
FileUtils.cd($dir_output)

module AirUtils

	# purpose : parses scanner output, returns [bssid,channel] 

	def self.parse_scan(essid)
		#file_scan_last = Dir[$dir_output + "/scan*.csv"][-1]
		#file_scan_last = Dir[$dir_output + "/scan-*.csv"].sort[-2]
		file_scan_last = Dir[$dir_output + "/scan-*.csv"].sort[-1]
		puts "parsing %s" % [file_scan_last]
		CSV::Reader.parse(File.open(file_scan_last)) do |row|
		  bssid = row[0]
			channel = row[3]
			essid = row[13]
			puts "essid='%s' channel='%s' bssid='%s'" % [essid, channel, bssid]
			if (essid && essid.strip && essid.strip == ARGV[0]) then
				essid = essid.strip
				channel = channel.strip
				puts "essid='%s' channel='%s' bssid='%s'" % [essid, channel, bssid]
				return bssid, channel
			end
		end
	end

  # purpose : get list of wifi interfaces from /proc/net/wireless 

  def self.list_ifaces_wireless()
    interfaces = []
    syntax_catwireless = "tail -2 /proc/net/wireless"
    IO.popen(syntax_catwireless) { |f|
      f.readlines.each() { |row|
        components = row.split()
        iface = components[0]
        interfaces.push(iface.gsub!(':', ''))
      }
    }
    return interfaces
  end 

  # purpose : fetch MAC for an iface 

  def self.fetch_mac_for_iface(iface)
		syntax_ifconfig = "ifconfig %s" % [iface]
		cmdout = IO.popen(syntax_ifconfig)
		line_first = cmdout.readline.split()
		mac = line_first[4]
    if (mac.match('-'))
      components_mac = mac.split('-')
      mac = components_mac[0..5].join(':')
    end
    return mac
  end

	# purpose : returns the mac address of iface_crack
	# comment : assumes a lot about ifconfig output
	# NOTE: once monitor mode is enabled, the mac from ifconfig is fucked up

	def self.mymac()
		syntax_ifconfig = "ifconfig %s" % [$iface_crack]
		cmdout = IO.popen(syntax_ifconfig)
		line_first = cmdout.readline.split()
		return line_first[4]
	end

end
