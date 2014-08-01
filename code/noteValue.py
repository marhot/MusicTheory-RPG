import sys, pygame
import config
from pygame.locals import *
import pygame.midi
pygame.init()
pygame.midi.init()
from time import sleep

#This is information specific the first level or just information on notes

pianoKeys = []
notes = []
beatsPerMeasure = 4
beat = 1/4
bpm = 120

pianoKeys.append(K_a)
pianoKeys.append(K_w)
pianoKeys.append(K_s)
pianoKeys.append(K_e)
pianoKeys.append(K_d)
pianoKeys.append(K_f)
pianoKeys.append(K_t)
pianoKeys.append(K_g)
pianoKeys.append(K_y)
pianoKeys.append(K_h)
pianoKeys.append(K_u)
pianoKeys.append(K_j)
pianoKeys.append(K_k)


class Note (object):
    def __init__ (self, pitch):
        self.pitch = pitch
        self.time = 0
        self.release = 0
        self.delay = 15

initPitch = ((4 + 2) * 12) + 2
for i in range (13):
    newNote = Note(initPitch)
    notes.append(newNote)
    initPitch += 1

#checks to see if any of the keys on the keyboard are a pianokey and returns a list of those keys
def checkKeys(keys):
    keysPlayed = []
    for key in pianoKeys:
        if keys[key]:
            keysPlayed.append(key)
    return keysPlayed

'''class Note (object):
    def __init__ (self, pitch):
        self.pitch = pitch
        self.time = 0
        self.release = 0
        self.delay = 15'''


def changeOctave(octaveNum):
    initPitch = ((octaveNum + 2) * 12 ) + 2 
    for note in notes:
        note.pitch = initPitch
        initPitch += 1


def findNote(pressedKey):
    count = 0
    for key in pianoKeys:
        if key == pressedKey:
            return pitches(count)
        count += 1

    return "note not found"


def playNote (pressedKey):
    note = findNote(pressedKey)
    if note != "note not found":
        note.time = pygame.time.get_ticks()
        midi_out.note_on(note.pitch, 127)

def stopPlayDelay ():
    currentTime = pygame.time.get_ticks()
    for note in notes:
        if currentTime - note.time >= note.release:
            midi_out.note_off(note.pitch, 127)

def stopPlayCutOff (note):
    midi_out.note_off(note.pitch, 127)
    

def playDuration(note, duration):
    note.time = pygame.time.get_ticks()
    midi_out.note_on(note.pitch, 127)
    if duration == beat:
        note.release = 60000 / bpm
    elif duration > beat:
        factor = duration/beat
        note.release = 60000 / bpm / factor
    elif duration < beat:
        factor = beat/duration
        note.release = 60000 / bpm * factor

'''class PianoKeys (object):
    def __init__ (self):
        self.octave = 4
        self.pitches = []
        initPitch = 74
        self.keys = []
        self.time1 = 0
        self.time2 = 0

        for i in range(13):
           self.pitches.append(initPitch)
           initPitch += 1

        self.keys.append(K_a)
        self.keys.append(K_w)
        self.keys.append(K_s)
        self.keys.append(K_e)
        self.keys.append(K_d)
        self.keys.append(K_f)
        self.keys.append(K_t)
        self.keys.append(K_g)
        self.keys.append(K_y)
        self.keys.append(K_h)
        self.keys.append(K_u)
        self.keys.append(K_j)
        self.keys.append(K_k)

    def setPitches  (self):
        initPitch = ((self.octave + 2) * 12 ) + 2 
        for pitch in self.pitches:
            pitch = initPitch
            initPitch += 1

    def changeOctave (self, octavenum)
        self.octave = octavenum
        self.setPitches()

    def findNote (self, pressedKey):
        count = 0
        for key in keys:
            if key == pressedKey:
                return self.pitches(count)
            count += 1

        return 0

    def PlayNote (self, key):
        pitch = self.findNote(key)
        self.time1 = pygame.time.get_tickes()
        midi_out.note_on(pitch, 137)'''


'''class Note (PianoKeys):
    def __init__ (self, value):
        self.value = value'''
        


'''class PlayNote (object):
    def __init__ (self, key):
        self.pitch = key'''
