import time

from neopixel import *

class LedRing:
    
    LED_COUNT      = NUM_LEDS      # Number of LED pixels.
    LED_PIN        = 0      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
    LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # 0 or 1
    LED_STRIP      = ws.SK6812_STRIP_GRBW

    prevPos1 = 0
    prevPos2 = 0

    str1 = 0
    str2 = 0

    def __init__(self, LED_PIN):
        self.LED_PIN = LED_PIN

    def lightLEDs(self, pos1, str1, pos2, str2):
        # Turn off the old leds
        strip.setPixelColor(prevPos1, Color(0,0,0))
        strip.setPixelColor(prevPos2, Color(0,0,0))
        # Calculate the strength of the light
        self.str1 = 255 * str1
        self.str2 = 255 * str2
        # Light the two new leds
        strip.setPixelColor(pos1, Color(self.str1, self.str1, self.str1))
        strip.setPixelColor(pos2, Color(self.str2, self.str2, self.str2))
        prevPos1 = pos1
        prevPos2 = pos2


    def setup(self):
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

        strip.begin()
        blackout(strip)
