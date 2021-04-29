"""CircuitPython Essentials NeoPixel example"""
import board
import digitalio
import neopixel
import random
import time

def read_config(file_config="./npconfig.py"):
    try:
        exec(open(file_config).read())
    except Exception as e:
        print(e)
    print({
        "board": dir(board),
        "config": file_config,
    })
    #print(open(file_config).read())

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def randpixel_randcolor(wait):
    pixel = random.randint(0, num_pixels - 1)
    color = random.randint(0, 256)
    #print({"p": pixel, "c": color})
    pixels[pixel] = wheel(color)
    pixels.show()
    time.sleep(wait)

def purple_strobe(wait):
    pixels.fill(OFF)
    pixels.show()
    pixels.fill(PURPLE)
    pixels.show()
    pixels.fill(OFF)
    pixels.show()
    time.sleep(wait)

OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

def main():
    while True:
        #purple_strobe(0.1)
        randpixel_randcolor(2.0)
        #rainbow_cycle(0)  # Increase the number to slow down the rainbow

def intro():
    color_chase(PURPLE, 0.1)  # Increase the number to slow down the color chase
    color_chase(OFF, 0.1)
    pixels.fill(CYAN)
    pixels.show()
    pixels.fill(PURPLE)
    pixels.show()
    pixels.fill(CYAN)
    pixels.show()
    color_chase(OFF, 0.1)

if __name__ == '__main__':
    read_config()
    pixel_pin = board.NEOPIXEL
    num_pixels = num_pixels or 4
    brightness = brightness or 0.3

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    intro()
    main()
