import sys, pygame
import config
from pygame.locals import *

class Fill (object):
    def __init__ (self, emptyLoc, fillingLoc, direction):
        self.empty = pygame.image.load(emptyLoc)
        self.filling = pygame.image.load(fillingLoc)
        self.direction = direction
        self.fxWidth = self.filling.get_size()[0]
        self.fxHeight = self.filling.get_size()[1]
        self.x = 0
        self.y = 0
        self.buffer = self.fxWidth/100


    def draw (self):
        config.SCREEN.blit(self.empty, (800, 300))


    '''def fill(self):
        if self.direction == 'right':
            x = 0
            while x <= self.fxWidth:
                y = 0
                pix = []
                while y <= self.fxHeight:
                    pix.append(self.filling.get_at((x, y)))
                    y += 1

                config.SCREEN.blit'''

    '''def fill(self):
        if self.direction  == "right":
            x = 0
            while x < self.fxWidth:
                y = 0
                while y < self.fxHeight:
                    self.empty.set_at((x, y),self.filling.get_at((x,y)))
                    y += 1
                x += 1
                self.draw()'''


    def fill(self):
        if self.direction == "right" and self.x < self.fxWidth:
            x = self.x
            #while self.x < self.fxWidth:
            while x <= self.x + self.buffer:
                y = 0
                while y < self.fxHeight:
                    self.empty.set_at((x, y), self.filling.get_at((x,y)))
                    y += 1
                x += 1
                if x >= self.fxWidth:
                    self.x = x
                    return
            self.x = x

            #place draw function in here.
