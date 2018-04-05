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
import LedRing

from NoteDial import NoteDial
from NoteDial1 import NoteDial1
from NoteDial2 import NoteDial2
from NoteDial3 import NoteDial3

freq1 = 0
noteDial1 = NoteDial1()
ledRing1 = LedRing(18)
rotary1 = Rotary(pinNum)

def setup():
    GPIO.setup()

def loop():
    for freq in range(131,502):
        noteDial1.ledPower = noteDial1.calculateLedPower(freq)
        ledRing1.lightLeds(noteDial1.notePos, noteDial1.ledPreviousPower, noteDial1.notePos + 1, noteDial1.ledNextPower)


def clean():
    GPIO.cleanup()

# Main:
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    except:
        print("General error")
    finally:
        print("Clean up")
        clean()
