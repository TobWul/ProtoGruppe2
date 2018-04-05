from neopixel import *

class LedRing:
    
    LED_COUNT      = 24      # Number of LED pixels.
    LED_PIN        = 0      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # 0 or 1
    LED_STRIP      = ws.SK6812_STRIP
    
##    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

    prevPos1 = 0
    prevPos2 = 0
    
    strip = 0

    def __init__(self, LedPin):
        self.LED_PIN = LedPin
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL, self.LED_STRIP)

    def lightSingleLED(self, pos, color):
        self.strip.setPixelColor(pos, color)
        self.strip.show()
        
    def turnOffLED(self, pos):
        self.strip.setPixelColor(pos, Color(0,0,0))
    
    def lightLEDs(self, pos1, str1, pos2, str2):
        
        # Turn off the old leds
        self.turnOffLED(self.prevPos1)
        self.turnOffLED(self.prevPos2)
        
        # Calculate light strength
        str1 = int(str1 * 255)
        str2 = int(str2 * 255)
        
        # Light the two new leds
        self.lightSingleLED(pos1, Color(str1, str1, str1))
        self.lightSingleLED(pos2, Color(str2, str2, str2))
        
        self.prevPos1 = pos1
        self.prevPos2 = pos2
        
    def lightChord(self, chords):
        # Chord hint color
        color = Color(255,255,0)
        for i in chords:
            self.lightSingleLED(i, color)
        
    
    def blackout(self, strip):
            for i in range(max(strip.numPixels(), strip.numPixels())):
                    strip.setPixelColor(i, Color(0,0,0))
                    strip.show()

    def setup(self):
        self.strip.begin()
        self.blackout(self.strip)
