from NoteDial import NoteDial

# Master dial
class NoteDial1(NoteDial):


    def validNotes(self):
        # All notes are valid
        # Reset the validIndexes list
        self.validIndexes = []
        # Populates list with numbers from 0-23
        for i in range(0,24):
            self.validIndexes.append(i)
        