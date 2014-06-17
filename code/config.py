"""
This file contains all global variables
"""

import pygame
#from overworld import Overworld, Scene
import overworld
import unit

# initialize pygame
pygame.init()
pygame.display.set_caption("Music Theory RPG")
FPSclock = pygame.time.Clock()

# display screen values
SCREENX = 1275
SCREENY = 750
MENUTOP = SCREENY - 75
SCREEN = pygame.display.set_mode((SCREENX, SCREENY))

#playerchars
playerChars = []
tallis = unit.PlayerChar("Tallis", 1, "pianist", 20, 20, 20, "images/ally")
playerChars.append(tallis)

# initialize overworld
OVERWORLD = overworld.Overworld()
scene1 = overworld.Scene("images/overworldPlaceholder/background00.png")
marhot = unit.Enemy(10, "Marhot", 1, "flautist", 20, 20, 20, "images/enemyPlaceholder")

scene1.addUnit(marhot)
scene1.addUnit(tallis)
#scene1.addEntity("platform", "surface", "images/overworldPlaceholder/platform.png", (0, config.SCREENY - 50))
#scene1.addEntity("tree", "barrier", "images/overworldPlaceholder/tree.png", (100, 200))
scene2 = overworld.Scene("images/overworldPlaceholder/background01.png")
scene3 = overworld.Scene("images/overworldPlaceholder/background02.png")
OVERWORLD.setNeighbors(scene1, scene2, 'right', 'left')
OVERWORLD.setNeighbors(scene2, scene3, 'right', 'left')
OVERWORLD.setCurScene(scene1)
scene1.addEntity("tree", "barrier", "images/overworldPlaceholder/tree.png", (100, 200))
scene1.addEntity("ground", "floor", "images/overworldPlaceholder/ground.png", (0, SCREENY))
#scene1.addUnit(tallis)
print OVERWORLD.curScene.order
