# CircuitPython demo - NeoPixel
 
import time
import random
import board
import neopixel
 
pixel_pin = board.D1
num_pixels = 14
SPEED = 2
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
 
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

def burst(aPixel):
    pixels[aPixel] = WHITE
    time.sleep(0.0125)
    pixels.show()
    pixels[aPixel] = CYAN
    time.sleep(0.0125)
    pixels.show()
    pixels[aPixel] = BLUE
    time.sleep(0.0125)
    pixels.show()
    # pixels[aPixel] = LOWWHITE
    # time.sleep(0.0125)
    # pixels.show()

def palletBurst(aPixel, aPallet):
    # print('aPixel is ', aPixel)
    # print('aPallet is ', aPallet)
    aColor = random.randint(0, len(aPallet) -1)
    # print('aColor is', aColor)
    pixels[aPixel] = aPallet[aColor]
    pixels.show()
    time.sleep(0.0125)

# COLORS 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255,165,0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
SKYBLUE = (135,206,250)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)
LOWWHITE = (4, 4, 4)

# COLOR PALLETS
LIGHTNING = [WHITE, CYAN, SKYBLUE, BLUE, PURPLE]
FIRE = [RED, YELLOW, BLACK, ORANGE]

while True:
    calmTime = random.random() / SPEED
    aStrike = random.randrange(num_pixels)
    # burst(aStrike)
    palletBurst(aStrike, LIGHTNING)
    #pixels[1] = (255, 0, 255)
    #time.sleep(2)
    
    #for aPixel in range(num_pixels):
    #   # if pixel is low white
    #   burst(aPixel)
       
       
    #pixels.fill(WHITE)
    #pixels.show()
    #time.sleep(0.05)  # Increase or decrease to change the speed of the solid color change.
    #pixels.fill(CYAN)
    #pixels.show()
    #time.sleep(.01)
    #pixels.fill(BLUE)
    #pixels.show()
    #time.sleep(0.07)
    
    pixels.fill(LOWWHITE)
    # pixels.fill(BLACK)
    pixels.show()
    time.sleep(calmTime)
    
    
 
    # color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)
 
    # rainbow_cycle(0)  # Increase the number to slow down the rainbow
