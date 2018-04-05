from NoteDial import NoteDial

# Second dial
class NoteDial2(NoteDial):


    def getOtherNotes(self, noteIndex):
        if (noteIndex == 0):
            return [1, 2]
        elif (noteIndex == 1):
            return [0, 2]
        elif (noteIndex == 2):
            return [1, 2]


    def validNotes(self, freq):
        self.validIndexes = [] # List reset
        note = self.freqToNote(freq)
        if (note == 'C3' or note == 'C4'):
            # C E G
            # F A C
            # G# C D#
            self.validIndexes.append(self.noteToIndex('E3'))
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('F3'))
            self.validIndexes.append(self.noteToIndex('A3'))
            self.validIndexes.append(self.noteToIndex('G#3'))
            self.validIndexes.append(self.noteToIndex('D#3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('E4'))
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('F4'))
            self.validIndexes.append(self.noteToIndex('A4'))
            self.validIndexes.append(self.noteToIndex('G#4'))
            self.validIndexes.append(self.noteToIndex('D#4'))
        elif (note == 'C#3' or note == 'C#4'):
            # C# E G#
            # F# bH C#
            # A C# E
            self.validIndexes.append(self.noteToIndex('E3'))
            self.validIndexes.append(self.noteToIndex('G#3'))
            self.validIndexes.append(self.noteToIndex('F#3'))
            self.validIndexes.append(self.noteToIndex('bH3'))
            self.validIndexes.append(self.noteToIndex('A3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('E4'))
            self.validIndexes.append(self.noteToIndex('G#4'))
            self.validIndexes.append(self.noteToIndex('F#4'))
            self.validIndexes.append(self.noteToIndex('bH4'))
            self.validIndexes.append(self.noteToIndex('A4'))
        elif (note == 'D3' or note == 'D4'):
            # D F# A
            # G B D
            # bH D F
            self.validIndexes.append(self.noteToIndex('F#3'))
            self.validIndexes.append(self.noteToIndex('A3'))
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('H3'))
            self.validIndexes.append(self.noteToIndex('bH3'))
            self.validIndexes.append(self.noteToIndex('F3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('F#4'))
            self.validIndexes.append(self.noteToIndex('A4'))
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('H4'))
            self.validIndexes.append(self.noteToIndex('bH4'))
            self.validIndexes.append(self.noteToIndex('F4'))
        elif (note == 'D#3' or note == 'D#4'):
            # D# G bH
            # G# C D#
            # H D# F#
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('bH3'))
            self.validIndexes.append(self.noteToIndex('G#3'))
            self.validIndexes.append(self.noteToIndex('C3'))
            self.validIndexes.append(self.noteToIndex('H3'))
            self.validIndexes.append(self.noteToIndex('F#3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('bH4'))
            self.validIndexes.append(self.noteToIndex('G#4'))
            self.validIndexes.append(self.noteToIndex('C4'))
            self.validIndexes.append(self.noteToIndex('H4'))
            self.validIndexes.append(self.noteToIndex('F#4'))
        elif (note == 'E3' or note == 'E4'):
            # C E G
            # C# E G#
            # E G# H
            # A C# E
            self.validIndexes.append(self.noteToIndex('C3'))
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('C#3'))
            self.validIndexes.append(self.noteToIndex('G#3'))
            self.validIndexes.append(self.noteToIndex('H3'))
            self.validIndexes.append(self.noteToIndex('bH3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('C4'))
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('C#4'))
            self.validIndexes.append(self.noteToIndex('G#4'))
            self.validIndexes.append(self.noteToIndex('H4'))
            self.validIndexes.append(self.noteToIndex('bH4'))
        elif (note == 'F3' or note == 'F4'):
            # F A C
            # bH D F
            self.validIndexes.append(self.noteToIndex('A3'))
            self.validIndexes.append(self.noteToIndex('C3'))
            self.validIndexes.append(self.noteToIndex('bH3'))
            self.validIndexes.append(self.noteToIndex('D3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('A4'))
            self.validIndexes.append(self.noteToIndex('C4'))
            self.validIndexes.append(self.noteToIndex('bH4'))
            self.validIndexes.append(self.noteToIndex('D4'))
        elif (note == 'F#3' or note == 'F#4'):
            # D F# A
            # F# bH C#
            # H D# F#
            self.validIndexes.append(self.noteToIndex('D3'))
            self.validIndexes.append(self.noteToIndex('A3'))
            self.validIndexes.append(self.noteToIndex('bH3'))
            self.validIndexes.append(self.noteToIndex('C#3'))
            self.validIndexes.append(self.noteToIndex('H3'))
            self.validIndexes.append(self.noteToIndex('D#3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('D4'))
            self.validIndexes.append(self.noteToIndex('A4'))
            self.validIndexes.append(self.noteToIndex('bH4'))
            self.validIndexes.append(self.noteToIndex('C#4'))
            self.validIndexes.append(self.noteToIndex('H4'))
            self.validIndexes.append(self.noteToIndex('D#4'))
        elif (note == 'G3' or note == 'G4'):
            # C E G
            # G H D
            self.validIndexes.append(self.noteToIndex('C3'))
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('H3'))
            self.validIndexes.append(self.noteToIndex('D3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('C4'))
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('H4'))
            self.validIndexes.append(self.noteToIndex('D4'))
        elif (note == 'G#3' or note == 'G#4'):
            # C# E G#
            # E G# H
            # G# C D#
            self.validIndexes.append(self.noteToIndex('C#3'))
            self.validIndexes.append(self.noteToIndex('E3'))
            self.validIndexes.append(self.noteToIndex('H3'))
            self.validIndexes.append(self.noteToIndex('C3'))
            self.validIndexes.append(self.noteToIndex('D#3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('C#4'))
            self.validIndexes.append(self.noteToIndex('E4'))
            self.validIndexes.append(self.noteToIndex('H4'))
            self.validIndexes.append(self.noteToIndex('C4'))
            self.validIndexes.append(self.noteToIndex('D#4'))
        elif (note == 'A3' or note == 'A4'):
            # D F# A
            # F A C
            # A C# E
            self.validIndexes.append(self.noteToIndex('D3'))
            self.validIndexes.append(self.noteToIndex('F#3'))
            self.validIndexes.append(self.noteToIndex('F3'))
            self.validIndexes.append(self.noteToIndex('C3'))
            self.validIndexes.append(self.noteToIndex('C#3'))
            self.validIndexes.append(self.noteToIndex('E3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('D4'))
            self.validIndexes.append(self.noteToIndex('F#4'))
            self.validIndexes.append(self.noteToIndex('F4'))
            self.validIndexes.append(self.noteToIndex('C4'))
            self.validIndexes.append(self.noteToIndex('C#4'))
            self.validIndexes.append(self.noteToIndex('E4'))
        elif (note == 'bH3' or note == 'bH4'):
            # D# G bH
            # F# bH C#
            # bH D F
            self.validIndexes.append(self.noteToIndex('D#3'))
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('G#3'))
            self.validIndexes.append(self.noteToIndex('C#3'))
            self.validIndexes.append(self.noteToIndex('D3'))
            self.validIndexes.append(self.noteToIndex('F3'))
            # Octave
            self.validIndexes.append(self.noteToIndex('D#4'))
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('G#4'))
            self.validIndexes.append(self.noteToIndex('C#4'))
            self.validIndexes.append(self.noteToIndex('D4'))
            self.validIndexes.append(self.noteToIndex('F4'))
        elif (note == 'H3' or note == 'H4'):
            # E G# H
            # G H D
            # H D# F#
            self.validIndexes.append(self.noteToIndex('E3'))
            self.validIndexes.append(self.noteToIndex('G#3'))
            self.validIndexes.append(self.noteToIndex('G3'))
            self.validIndexes.append(self.noteToIndex('D3'))
            self.validIndexes.append(self.noteToIndex('D#3'))
            self.validIndexes.append(self.noteToIndex('F#3'))
            # Octagve
            self.validIndexes.append(self.noteToIndex('E4'))
            self.validIndexes.append(self.noteToIndex('G#4'))
            self.validIndexes.append(self.noteToIndex('G4'))
            self.validIndexes.append(self.noteToIndex('D4'))
            self.validIndexes.append(self.noteToIndex('D#4'))
            self.validIndexes.append(self.noteToIndex('F#4'))
            
        print(note, ': ', self.validIndexes)
            

# Testing:
# n = NoteDial2(2,3)
# n.validNotes(131)