#include <Rotary.h>
#include <FastLED.h>

#define NUM_LEDS_PER_STRIP 24

CRGB ledRing1[NUM_LEDS_PER_STRIP];
CRGB ledRing2[NUM_LEDS_PER_STRIP];
CRGB ledRing3[NUM_LEDS_PER_STRIP];

// Note variables
int noteFreqList[] = {131,139,147,156,165,175,185,196,208,220,233,247,262,277,294,311,330,349,370,392,415,440,466,494};
float ledPreviousPower = 0;
float ledNextPower = 0;

// NoteDial 3 variables
int chordPos = 0;
int note1 = 0;
int note2 = 0;
int note3 = 0;

Rotary r1 = Rotary(2,3);
Rotary r2 = Rotary(4,5);
Rotary r3 = Rotary(6,7);

int MAX_ROTATION = 500;
int MIN_ROTATION = 131;

int MAX_STR = 255;
int GREEN = 90;
int YELLOW = 30;

int counter1 = MIN_ROTATION;
int counter2 = MIN_ROTATION;
int counter3 = MIN_ROTATION;

unsigned char result1;
unsigned char result2;
unsigned char result3;



int chords[12][3] = {
  {131, 165, 196}, // {"C", "E", "G"},
  {139, 175, 208}, // {"C#", "F", "G#"},
  {147, 185, 220}, // {"D", "F#", "A"},
  {156, 196, 233}, // {"D#", "G", "bH"},
  {165, 208, 247}, // {"E", "G#", "H"},
  {175, 220, 131}, // {"F", "A", "C"},
  {185, 233, 139}, // {"F#", "bH", "C#"},
  {196, 247, 147}, // {"G", "H", "D"},
  {208, 131, 156}, // {"G#", "C", "D#"},
  {220, 139, 165}, // {"A", "C#", "E"},
  {233, 147, 175}, // {"bH", "D", "F"},
  {247, 156, 185} // {"H", "D#", "F#"}
};

// Valid notes defining
int validNotes2[12] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int validNotes3[2] = {-1, -1};

int getNotePos(int freq) {
  for (int pos = 23; pos >= 0; pos--) {
    if (freq <= noteFreqList[0]) {
      return 0;
    }
    else if (freq > noteFreqList[pos]) {
      return pos;
    }
  }
}

void resetLeds() {
  for (int i = 0; i < 24; i++) {
    ledRing1[i] = CRGB::Black;
    ledRing2[i] = CRGB::Black;
    ledRing3[i] = CRGB::Black;
  }
}

void lightLeds(int freq1, int freq2, int freq3) {
  boolean led2Correct = false;
  boolean led3Correct = false;

  int led1Pos = getNotePos(freq1);
  int led2Pos = getNotePos(freq2);
  int led3Pos = getNotePos(freq3);
  float led1Str = calculateNextLedPower(freq1);
  float led2Str = calculateNextLedPower(freq2);
  float led3Str = calculateNextLedPower(freq3);

  calculateValidNotes2(freq1);
  calculateValidNotes3(freq1, freq2);

  // Position lights
  ledRing1[led1Pos] = CHSV( 0, 0, MAX_STR * (1 - led1Str));
  if (led1Pos == 23) {
    ledRing1[0] = CHSV( 0, 0, MAX_STR * led1Str);
  } else {
    ledRing1[led1Pos + 1] = CHSV( 0, 0, MAX_STR * led1Str);
  }

  ledRing2[led2Pos] = CHSV( 0, 0, MAX_STR * (1 - led2Str));
  if (led2Pos == 23) {
    ledRing2[0] = CHSV( 0, 0, MAX_STR * led2Str);
  } else {
    ledRing2[led2Pos + 1] = CHSV( 0, 0, MAX_STR * led2Str);
  }
  
  ledRing3[led3Pos] = CHSV( 0, 0, MAX_STR * (1 - led3Str));
  if (led3Pos == 23) {
    ledRing3[0] = CHSV( 0, 0, MAX_STR * led3Str);
  } else {
    ledRing3[led3Pos + 1] = CHSV( 0, 0, MAX_STR * led3Str);
  }

  if (freqToIndex(freq1) >= 0) {
    
  }

  if (freqToIndex(freq1) >= 0) {
    // Ledring 2 valid notes
    for (int i = 0; i < 12; i++) {
      // Serial.println(validNotes2[i]);
      if (validNotes2[i] >= 0) {
        // Green if on this note
        if (freqToIndex(freq2) == validNotes2[i]) {
          ledRing2[validNotes2[i]] = CHSV(GREEN, 255, 255);
        } else {
          ledRing2[validNotes2[i]] = CHSV(YELLOW, 255, 255);
          if (led2Pos == validNotes2[i] && led2Str < 1) {
            ledRing2[led2Pos] = CHSV( YELLOW, 255, MAX_STR * (1 - led2Str));
          }
          if ((led2Pos + 1) == validNotes2[i]) {
            ledRing2[led2Pos + 1] = CHSV( YELLOW, 255, MAX_STR * led2Str);
          }
        }
      }
    }
  }
  // Ledring 3 valid notes
  if (freqToIndex(freq1) >= 0 && freqToIndex(freq2) >= 0) {
    
    if (validNotes3[0] >= 0 && validNotes3[1] >= 0) {
      // On correct position
      if (freqToIndex(freq3) == validNotes3[0]) {
        ledRing3[validNotes3[0]] = CHSV(GREEN, 255, 255);
      } else {
        ledRing3[validNotes3[0]] = CHSV(YELLOW, 255, 255);
      }
      // On correct position
      if (freqToIndex(freq3) == validNotes3[1]) {
        ledRing3[validNotes3[1]] = CHSV(GREEN, 255, 255);
      } else {
        ledRing3[validNotes3[1]] = CHSV(YELLOW, 255, 255);
      }
    }
  }

  if (freqToIndex(freq1) >= 0) {
      Serial.print("led1Pos: ");
      Serial.println(led1Pos);
      if (freq1 == 131) {
        ledRing1[led1Pos] = CHSV(GREEN, 255, 255);
      } else {
        ledRing1[led1Pos + 1] = CHSV(GREEN, 255, 255);
      }
  }

  FastLED.show();
  resetLeds();
}

float calculateNextLedPower(int freq) {
  float difference = 0;
  int notePos = getNotePos(freq);
  
  int prevNote = noteFreqList[notePos];
  int nextNote = 0;

  if (notePos < 23) {
    nextNote = noteFreqList[notePos + 1];
    difference = nextNote - prevNote;
  }
  else if (notePos == 23) {
    nextNote = noteFreqList[0];
    difference = 8;
  }

  return (freq - prevNote) / difference;
}

void resetValidNotes2Array() {
  for (int i = 0; i < 12; i++) {
    validNotes2[i] = -1;
  }
}

void resetValidNotes3Array() {
  validNotes3[0] = -1;
  validNotes3[1] = -1;
}

void calculateValidNotes2(int freq) {
  int baseChordList[] = {3,4,5,7,8,9,15,16,17,19,20,21};
  int currentNote = freqToIndex(freq);
  for (int i = 0; i < 12; i++) {
    int calculatedNote = currentNote + baseChordList[i];
    if (calculatedNote > 23) {
      calculatedNote = calculatedNote - 24;
      validNotes2[i] = calculatedNote;
    } else {
      validNotes2[i] = calculatedNote;
    }
  }
}

int freqToIndex(int freq) {
  for (int i = 0; i < 24; i++) {
    if (freq == noteFreqList[i]) {
      return i;
    }
  }
  return -1;
}

void calculateValidNotes3(int freq1, int freq2) {
  int note3 = -1;
  resetValidNotes3Array();

  // Runs throught the chords-list
  for (int i = 0; i < 12; i++) {

    // Will return the freq of the last note if it exists or -1
    // Reset to 3 octave
    int freq1Index = freqToIndex(freq1);
    int freq2Index = freqToIndex(freq2);

    // Calculate only for one octave and add the 4 octave at the end
    if (freq1Index > 11) {
      freq1 = noteFreqList[freq1Index - 12];
    }
    if (freq2Index > 11) {
      freq2 = noteFreqList[freq2Index - 12];
    }

    // Set initial value for the position of the chords
    int chord1Pos = -1;
    int chord2Pos = -1;

    for (int j = 0; j < 3; j++) {
      if (chords[i][j] == freq1) {
        chord1Pos = j;
      }
      if (chords[i][j] == freq2) {
        chord2Pos = j;
      }
      
      // Breaking the loop
      if (chord1Pos >= 0 && chord2Pos >= 0) {
        int sum = chord1Pos + chord2Pos;
        if (sum == 1) {
          note3 = chords[i][2];
        }
        else if (sum == 2) {
          note3 = chords[i][1];
        }
        else if (sum == 3) {
          note3 = chords[i][0];
        }
        // Returns a negative number to make it easy to check if there is a valid note 
        else {
          note3 = -1;
        }
      }  
    }

    if (note3 >= 0) {
      int note3Pos = freqToIndex(note3);
      validNotes3[0] = note3Pos;
      validNotes3[1] = note3Pos + 12;
      break;
    }
  }
}

void updateRotation() {
  result1 = r1.process();
  result2 = r2.process();
  result3 = r3.process();

  if (result1) {
    if (result1 == DIR_CW) {
      counter1++;
      if (counter1 > MAX_ROTATION) {
        counter1 = MIN_ROTATION;
      }
    } 
    else {
      counter1--;
      if (counter1 < MIN_ROTATION) {
        counter1 = MAX_ROTATION;
      }
    }
    Serial.print("1 ");
    Serial.println(counter1);
  }

  if (result2) {
    if (result2 == DIR_CW) {
      counter2++;
      if (counter2 > MAX_ROTATION) {
        counter2 = MIN_ROTATION;
      }
    } 
    else {
      counter2--;
      if (counter2 < MIN_ROTATION) {
        counter2 = MAX_ROTATION;
      }
    }
    Serial.print("2 ");
    Serial.println(counter2);
  }
  
  if (result3) {
    if (result3 == DIR_CW) {
      counter3++;
      if (counter3 > MAX_ROTATION) {
        counter3 = MIN_ROTATION;
      }
    } 
    else {
      counter3--;
      if (counter3 < MIN_ROTATION) {
        counter3 = MAX_ROTATION;
      }
    }
    Serial.print("3 ");
    Serial.println(counter3);
  }

  if (result1 || result2 || result3) {
    lightLeds(counter1, counter2, counter3);
  }
}

void setup() {

  Serial.begin(9600);

  // The three LED rings with 24 leds on each, connected to pins: 10, 11 and 12
  FastLED.addLeds<NEOPIXEL, 10>(ledRing1, NUM_LEDS_PER_STRIP);
  FastLED.addLeds<NEOPIXEL, 11>(ledRing2, NUM_LEDS_PER_STRIP);
  FastLED.addLeds<NEOPIXEL, 12>(ledRing3, NUM_LEDS_PER_STRIP);

}

void loop() {
  
  updateRotation();

}