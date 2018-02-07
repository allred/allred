#!/usr/bin/env ruby

freq = "153.350M"
freq = "152.0075M"
freq = "454.075M"
freq = "929.6125M" # works for flex

cmd = <<-eoc
  rtl_fm -r 22050 -f #{freq} - | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a FLEX -f alpha -
eoc
  #rtl_fm -r 22050 -f #{freq} - | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a FLEX -f alpha /dev/stdin
  #rtl_fm -N -o 4 -A lut -s 22050 -C -f 153.350M - | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -f alpha /dev/stdin

system cmd
