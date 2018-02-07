#!/usr/bin/env ruby

cmd = <<-eoc
  rtl_fm -r 22050 -f 153.350M - | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -f alpha /dev/stdin
eoc
  #rtl_fm -N -o 4 -A lut -s 22050 -C -f 153.350M - | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -f alpha /dev/stdin

system cmd
