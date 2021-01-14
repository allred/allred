#!/usr/bin/env python
# [(50971, 0, 45875, 3200), (50971, 0, 45875, 3200)]
from lifxlan import BLUE, LifxLAN

def main():
    night_color = (50971, 0, 45875, 3200)
    lifx = LifxLAN(2)
    devices = lifx.get_lights()
    original_colors = []
    for bulb in devices:
        original_colors.append(bulb.get_color())
    for bulb in devices:
        bulb.set_color(BLUE, rapid=False)
    for bulb in devices:
        bulb.set_color(original_colors[0])

if __name__ == '__main__':
    main()
