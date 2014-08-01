import sys, pygame
import config
import noteValue
from pygame.locals import *

class Attack(object):
    def __init__ (self, name, power, interface, begincon, endcon, numKeys):
        self.name = name
        self.power = power
        self.interface = interface
        self.begincon = begincon
        self.endcon = endcon
        self.numKeys = numKeys

    def runInterface(self, keys):
        #self.interface
        pianoKeys = noteValue.checkKeys(keys)
        intKeys = []

        if self.begincon:
            if self.numKeys == 0:
                self.interface
            elif self.numKeys == 1 and pianoKeys.get_size() == 1:
                self.interface (pianoKeys[0])
            elif pianoKeys.get_size() >= self.numKeys:
                for i in range (self.numKeys):
                    intKeys.append(pianoKeys[i])
                self.interface(intKeys)


class Button(object):
    def __init__(self, name, imgLoc, unit):
        self.name = name
        self.children = []
        image = pygame.image.load(self.imgLoc)
        self.unit = unit
        self.width = image.get_size()[0]
        self.height = image.get_size()[1]

    def display(self):
        config.SCREEN.blit(image, self.unit.width/2 - self.width/2, unit.height + self.height/2)

