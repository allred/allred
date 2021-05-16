"""CircuitPython Essentials NeoPixel example"""
import board
import digitalio
import neopixel
import random
import time
import touchio

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
    """ best at brightness=.01 """
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

def quack(wait):
    print("hullo i'm quack")
    pixels.fill(GREEN)
    pixels.show()
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(wait)

def blueblip(wait):
    itery = random.randint(0, num_pixels)
    #for i in range(itery):
    for i in range(20):
        pixel = random.randint(0, num_pixels - 1)
        pixels[pixel] = GREEN
        pixels.show()
        #pixels.fill(BLUE)
        pixels.fill(PURPLE)
        pixels.show()
    time.sleep(wait)

def colorblip(wait, color):
    brightness_mod = 0.05
    pixels.brightness += brightness_mod 
    pixels.show()
    pixels.brightness -= brightness_mod 
    pixels.show()
    pixels.fill(color)
    pixels.show()

def redblip(wait):
    colorblip(wait, RED)
    time.sleep(wait)

def greenblip(wait):
    colorblip(wait, GREEN)
    time.sleep(wait)

def color_stroll(wait=1):
    pixel = random.randint(0, num_pixels - 1)
    actionpixel = pixels[pixel]
    if actionpixel == (0, 0, 0):
        print("PUUUURPLE TIME")
        pixels.fill(PURPLE)
    print("color_stroll before: " + str(actionpixel))
    newcolor = actionpixel 
    colormod = 10
    if (time.monotonic() % 1) < .1:
        colormod += random.randint(0, 100)
        print("BOOYAH " + str(colormod))
    def randakicka(num):
        if random.randint(0,1) == 1:
            newval =  num + random.randint(0, colormod)
            if newval < 0 or newval > 255:
                return num
            return newval
        else:
            newval =  num - random.randint(0, colormod)
            if newval < 0 or newval > 255:
                return num
            return newval 
    newr = randakicka(newcolor[0])
    newg = randakicka(newcolor[1])
    newb = randakicka(newcolor[2]) 
    if (time.monotonic() % 1) > .9:
        newr = newcolor[0] - 1
        newg = newcolor[1] + 1
        newb = newcolor[2] - 1
        print("GREENIFY " + str(newg))
    newcolor = (newr, newg, newb)
    #actionpixel = (newcolor) 
    pixels[pixel] = (newcolor)
    pixels.show()
    print("color_stroll after: " + str(actionpixel))
    time.sleep(wait)


def main():
    time_touched = time.monotonic()
    while True:
        #purple_strobe(0.1)
        #rainbow_cycle(0)  # Increase the number to slow down the rainbow
        #modimporty()
        if runmode == "default":
            #intro()
            randpixel_randcolor(2.0)
        if runmode == "blueblip":
            blueblip(5.0)
        if runmode == "redblip":
            redblip(2.0)
        if runmode == "quack":
            quack(2.0)
        if runmode == "color_stroll":
            color_stroll(10 * random.random())
    #pixel = random.randint(0, num_pixels - 1)
        if time.monotonic() - time_touched < 0.15:
            continue
        if touch1.value:
            pixels.brightness += 0.05
            pixels.show()
            time_touched = time.monotonic()
            print("{}".format({"t": time.monotonic(), "touch1": touch2}))
        elif touch2.value:
            pixels.brightness -= 0.05
            pixels.show()
            time_touched = time.monotonic()
            print("{}".format({"t": time.monotonic(), "touch2": touch2}))
        print("{}".format({"t": time.monotonic(), "brightness": pixels.brightness, "runmode": runmode}))

def intro():
    color_chase(OFF, 0.1)
    color_chase(PURPLE, 0.1)  # Increase the number to slow down the color chase
    color_chase(OFF, 0.1)

if __name__ == '__main__':
    read_config()
    pixel_pin = board.NEOPIXEL
    num_pixels = num_pixels or 4
    brightness = brightness or 0.3

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    touch1 = touchio.TouchIn(board.TOUCH1)
    touch2 = touchio.TouchIn(board.TOUCH2)

    main()

