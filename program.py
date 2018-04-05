# C E G
# C# E G#
# D F# A
# D# G bH
# E G# H
# F A C
# F# bH C#
# G H D
# G# C D#
# A C# E
# bH D F
# H D# F#

import RPi.GPIO as GPIO
import time

from LedRing import LedRing
from NoteDial import NoteDial
from NoteDial1 import NoteDial1
from NoteDial2 import NoteDial2
from NoteDial3 import NoteDial3

freq1 = 0
noteDial1 = NoteDial()
ledRing1 = LedRing(18)

def setup():
    ledRing1.setup()
    noteDial1.begin()
    

def loop():
##    ledRing1.lightSingleLED(1,0.9)
##    time.sleep(1)
    for freq in range(131,502):        
        noteDial1.ledPower = noteDial1.calculateLedPower(freq)
        print(noteDial1.notePos)
        ledRing1.lightChord([3,5,8,10])
        ledRing1.lightLEDs(noteDial1.notePos, noteDial1.ledPreviousPower, noteDial1.notePos + 1, noteDial1.ledNextPower)
        time.sleep(0.001)
        
def clean():
    pass

# Main:
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        print("Clean up")
        ledRing1.blackout(ledRing1.strip)
        clean()
