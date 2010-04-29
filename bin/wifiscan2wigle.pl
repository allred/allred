#!/usr/bin/perl
# purpose : convert KML files from Android WifiScan App to Wigle CSV format
# usage   : run in the dir containing the KML files, i.e.
#           cd dir_containing_kml_files; wifiscan2wigle.pl > uploadme2wigle.csv
# notes   : 
# - successfully used to convert WifiScan KML files generated in 2009-06
# TODO    :
# - tie $dir_kml to an optional script argument
# - assume a more reasonable AccuracyMeters value?

use Data::Dumper;
use Date::Parse;
use File::Find;
use Geo::KML;
use Text::CSV;
use XML::LibXML::Simple;
use YAML;
use strict;
use warnings;

my $dir_kml = '.';
my %stats;
my $header;

# kismet example:

my $header_kismet = qq(Network;NetType;ESSID;BSSID;Info;Channel;Cloaked;Encryption;Decrypted;MaxRate;MaxSeenRate;Beacon;LLC;Data;Crypt;Weak;Total;Carrier;Encoding;FirstTime;LastTime;BestQuality;BestSignal;BestNoise;GPSMinLat;GPSMinLon;GPSMinAlt;GPSMinSpd;GPSMaxLat;GPSMaxLon;GPSMaxAlt;GPSMaxSpd;GPSBestLat;GPSBestLon;GPSBestAlt;DataSize;IPType;IP;);
# 1;infrastructure;flux;00:1B:2B:35:C9:17;AP-NYC-1540-28F\000\002\000\000;6;No;None;No;18.0;1000;0;1517;0;0;0;1517;IEEE 802.11b;;Wed Apr 14 12:08:17 2010;Wed Apr 14 17:41:36 2010;0;-59;0;90.000000;180.000000;0.000000;0.000000;-90.000000;-180.000000;0.000000;0.000000;0.000000;0.000000;0.000000;0;None;0.0.0.0;

# wigle example

my $header_wigle = 'WigleWifi-1.0
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters';
# 00:11:92:9a:21:23,viavoice,[WPA2-PSK-CCMP],2010-04-28 10:55:01,6,-85,40.759452,-73.985257,0,875

$header = $header_wigle;

my $csv = Text::CSV->new({
  sep_char => ',',
});

print $header . "\n";
my @files_kml = glob "$dir_kml/*";
foreach my $file (@files_kml) {
  my $ref = XMLin($file);
  #print Dumper $ref;
  #my ($ns, $data) = Geo::KML->read_kml($file);
  my $network = 0;
  my $placemark = $ref->{Document}->{Folder}->{Placemark};

  # either hash or array depending on the version

  if (ref $placemark eq 'HASH') {
    foreach my $essid (keys %$placemark) {
      my $placemark = $placemark->{$essid};
      process_placemark($placemark, $essid);
    }
  }
  elsif (ref $placemark eq 'ARRAY') {
    foreach my $rec (@$placemark) {
      process_placemark($rec);
    }
  }
  else {
    die "unknown ref type: " . ref $placemark;
  }
}
print STDERR Dump \%stats;

sub process_placemark {
  my $placemark = shift;
  my $essid = shift || $placemark->{name} || die "no name";
  #unless (ref $placemark eq 'HASH') {
  #  die Dumper $placemark;
  #}
  my $coordinates = $placemark->{Point}->{coordinates};
  my $description = $placemark->{description};
  #$description =~ /
  #/xms;
  $description =~ /BSSID.*?>\s*(\S+).*/;
  my $bssid = $1;
  my $caps;
  if ($description =~ /Caps.*?>\s*(\[\S+\]).*/) {
    $caps = $1;
  }
  $description =~ /Channel.*?>\s*(\S+).*/;
  my $channel = $1;
  $description =~ /Signal.*?>\s*(\S+).*/;
  my $signal = $1;
  $description =~ /Last\s+Seen.*?>\s*(.*M)/;
  my $last_seen = $1;

  $signal =~ s/db//;
  my ($longitude, $latitude) = split ',', $coordinates;
  my ($sec, $min, $hour, $day, $month, $year, $zone) = strptime($last_seen);
  $year += 1900;
  $month++;
  if ($month < 10) {
    $month = "0$month";
  }
  if ($day < 10) {
    $day = "0$day";
  }
  my $first_seen = "$year-$month-$day $hour:$min:$sec";
  #die Dumper $first_seen;

  unless ($bssid && $channel && $signal && $last_seen && $latitude && $longitude) {
    die Dumper { 
      rec => $placemark,
      essid => $essid,
      bssid => $bssid,
      caps => $caps,
      channel => $channel,
      signal => $signal,
      latitude => $latitude,
      longitude => $longitude,
      seen => $first_seen,
    };
  }

  # MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters';
  # 00:11:92:9a:21:23,viavoice,[WPA2-PSK-CCMP],2010-04-28 10:55:01,6,-85,40.759452,-73.985257,0,875

  #combineprint(
  unless ($caps) { $caps = ''; }
  print qq($bssid,$essid,$caps,$first_seen,$channel,$signal,$latitude,$longitude,0,250\n);
  $stats{ssids_total}++;
}

sub combineprint {
  $csv->combine(@_);
  print $csv->string . "\n";
}
