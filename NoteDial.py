import ledRing

class NoteDial:
    #               C   C#   D   D#  E   F   F#  G  G#  A   hB   H   C   C#   D   D#  E   F   F#  G  G#  A   hB  H
    noteFreqList = [131,139,147,156,165,175,185,196,208,220,233,247,262,277,294,311,330,349,370,392,415,440,466,494]
    notePos = 0
    position = 0
    ledPreviousPower = 0
    ledNextPower = 0
    validIndexes = []

    chords = [
    ['C', 'E', 'G'],
    ['C#', 'E', 'G#'],
    ['D', 'F#', 'A'],
    ['D#', 'G', 'bH'],
    ['E', 'G#', 'H'],
    ['F', 'A', 'C'],
    ['F#', 'bH', 'C#'],
    ['G', 'H', 'D'],
    ['G#', 'C', 'D#'],
    ['A', 'C#', 'E'],
    ['bH', 'D', 'F'],
    ['H', 'D#', 'F#']
    ]

    notes = {
            noteFreqList[0]: 'C3',
            noteFreqList[1]: 'C#3',
            noteFreqList[2]: 'D3',
            noteFreqList[3]: 'D#3',
            noteFreqList[4]: 'E3',
            noteFreqList[5]: 'F3',
            noteFreqList[6]: 'F#3',
            noteFreqList[7]: 'G3',
            noteFreqList[8]: 'G#3',
            noteFreqList[9]: 'A3',
            noteFreqList[10]: 'bH3',
            noteFreqList[11]: 'H3',
            noteFreqList[12]: 'C4',
            noteFreqList[13]: 'C#4',
            noteFreqList[14]: 'D4',
            noteFreqList[15]: 'D#4',
            noteFreqList[16]: 'E4',
            noteFreqList[17]: 'F4',
            noteFreqList[18]: 'F#4',
            noteFreqList[19]: 'G4',
            noteFreqList[20]: 'G#4',
            noteFreqList[21]: 'A4',
            noteFreqList[22]: 'bH4',
            noteFreqList[23]: 'H4'
        }

    # def __init__(self, rotaryOutputPinA, rotaryOutputPinB):
    #     self.rotaryOutputPinA = rotaryOutputPinA
    #     self.rotaryOutputPinB = rotaryOutputPinB

    def begin(self):
        # Import rotaryencoder
        # Import ledRing
        print("Begin")
    
    def getNotePos(self, freq):
        # Go through the list in reverese order
        for pos, note in reversed(list(enumerate(self.noteFreqList))):
            if freq <= self.noteFreqList[0]:
                return 0
            elif (freq > note):
                return pos
    
    def noteToIndex(self, note):
        return self.noteFreqList.index(self.noteToFreq(note))

    def noteToFreq(self, note):
        # keyList[indexOfValue]
        return list(self.notes.keys())[list(self.notes.values()).index(note)]

    def freqToNote(self, freq):

        return self.notes.get(freq, None)

    def calculateLedPower(self, freq):
        difference = 0
        self.notePos = self.getNotePos(freq)

        prevNote = self.noteFreqList[self.notePos]
        if self.notePos < 23:
            nextNote = self.noteFreqList[self.notePos + 1]
            difference = nextNote - prevNote
        elif (self.notePos == 23):
            nextNote = self.noteFreqList[0]
            # Frequency from 131 - 502
            difference = 8
        
        # Calculates the percentage of light on each led
        self.ledNextPower = (freq - prevNote) / difference
        self.ledPreviousPower = 1 - self.ledNextPower
        
        # Debugging prints
        # print("Freq = %d" % freq)
        # print("Difference = %d, prevNote = %d, nextNote = %d" % (difference, prevNote, nextNote))
        # print("[prevPow, nextPow] = [%f, %f]\n" % (self.ledNextPower, self.ledPreviousPower))

        return [self.ledPreviousPower, self.ledNextPower]


    
# Testing
noteDial = NoteDial()

# for i in range(131, 502):
#     print(i)
#     noteDial.runLedRing(i)
    