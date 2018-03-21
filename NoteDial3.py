from NoteDial import NoteDial

# Last dial
class NoteDial3(NoteDial):

    def __init__(self, rotaryOutputPinA, rotaryOutputPinB):
        NoteDial.__init__(rotaryOutputPinA, rotaryOutputPinB)

    def getRemainingNote(self, index1, index2):
        # 0 + 1 = 1 | (2)
        # 0 + 2 = 2 | (1)
        # 1 + 2 = 3 | (0)
        sum = index1 + index2
        if (sum == 1):
            return 2
        elif (sum == 2):
            return 1
        elif (sum == 3):
            return 0

    def validNotes(self, freq1, freq2):
        self.validIndexes = [] # List reset

        note1 = self.freqToNote(freq1)
        note2 = self.freqToNote(freq2)
        # Returns only the letter. C3 -> C
        if (len(note1) > 2):
            note1 = note1[0:2]
        else:
            note1 = note1[0]

        if (len(note2) > 2):
            note2 = note2[0:2]
        else:
            note2 = note2[0]

        print('Note 1: ', note1)
        print('Note 2: ', note2)
            
        note3 = -1 # If not in list returns -1

        # Debugging code
        

        for i in range(0, len(self.chords)):
            if (note1 in self.chords[i] and note2 in self.chords[i]):
                # noteToIndex(chords[note3Index])
                note3 = self.chords[i][self.getRemainingNote(self.chords[i].index(note1), self.chords[i].index(note2))]
                break
        
        print('Note 3: ', note3)
        self.validIndexes = [self.noteToIndex(note3 + '3'), self.noteToIndex(note3 + '4')] # Returns the notes in the two octaves


n = NoteDial3(2,3)
n.validNotes(147,220)
print('Note 3 indexes: ', n.validIndexes)