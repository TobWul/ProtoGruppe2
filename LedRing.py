import time

from neopixel import *

class LedRing():
    
    def __init__():
        self.LED_1_COUNT      = NUM_LEDS      # Number of LED pixels.
        self.LED_1_PIN        = 18      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
        LED_1_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_1_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
        LED_1_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
        LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_1_CHANNEL    = 0       # 0 or 1
        LED_1_STRIP      = ws.SK6812_STRIP_GRBW
