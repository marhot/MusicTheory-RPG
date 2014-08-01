import sys, pygame
import config
from pygame.locals import *

class BattleProfile(object):
    def __init__ (self, unit, HP):
        self.unitName = unit.name
        self.fullHP = HP
        self.currentHP = HP
        self.attacks = []
        self.attackButton = ("Attack", "images/battlePlaceholder/attackButton.png", unit)


    def add_attack(self, attack):
        self.append(attack)

    def changeHP (self, num):
        if num + self.currentHP >= self.fullHP:
            self.currentHP = self.fullHP

        elif num + self.currentHP <= 0:
            self.currentHP = 0

        else:
            self.currentHP += num

    def restoreHP (self):
        self.currentHP = self.fullHP

    #def makeButton(self, attack):
        #self.


class Button(object):
    def __init__(self, name, imgLoc, unit):
        self.name = name
        self.children = []
        image = pygame.image.load(self.imgLoc)
        self.unit = unit
        self.width = image.get_size()[0]
        self.height = image.get_size()[1]

    def display(self):
        config.SCREEN.blit(image, self.unit.width/2 - self.width/2 + self.unit.x, unit.height + self.height/2 + self.unit.y)


    def select(self):
        for attack in self.unit.attacks:
            if attack.name == self.name:
                keys = pygame.key.get_pressed()
                attack.runInterface(keys)
    #def displayChildren(self):
        #for child in self.children:
            #config.SCREEN.blit(image, self.unit.x, 


