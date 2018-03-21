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

chord_1 = ''
chord_2 = ''
chord_3 = ''

def setup():
    GPIO.setup()

def loop():
    #something

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
