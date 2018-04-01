# CircuitPython demo - NeoPixel
 
import time
import random
import board
import neopixel
 
pixel_pin = board.D1
num_pixels = 15
SPEED = 2
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

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

# functions
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

def multiPalletBurst(aPixel, aPallet):
    #total duration of burst
    burstDuration = .125
    
    #how many colors in the pallet?
    numColors = len(aPallet)
    print('numColors is ', numColors)
    miniBurst = burstDuration/numColors
    print('  miniBurst is', miniBurst)
    # for total number of colors in pallet, choose a random one
    for i in range(numColors):
        aColor = random.randint(0, numColors-1)
        pixels[aPixel] = aPallet[aColor]
        pixels.show()
        time.sleep(burstDuration/numColors)


#MAIN LOOP (near as I can tell)
while True:
    calmTime = random.random() / SPEED
    aStrike = random.randrange(num_pixels)
    # burst(aStrike)
    # palletBurst(aStrike, LIGHTNING)
    multiPalletBurst(aStrike, LIGHTNING)

    pixels.fill(LOWWHITE)
    pixels.show()
    time.sleep(calmTime)
