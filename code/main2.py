import sys, pygame
import config, overworld
from unit import PlayerChar, Enemy
from pygame.locals import *
import battle2

#tallis = PlayerChar("Tallis", 1, "pianist", 20, 20, 20, "images/allyPlaceholder")
#marhot = Enemy(10, "Marhot", 1, "flautist", 20, 20, 20, "images/enemyPlaceholder")
#playerChars = []
#enemies = []
#playerChars.append(tallis)
#enemies.append(marhot)
mode = "overworld"
overworld.init(config.playerChars, config.enemies)

while True:
        config.SCREEN.fill((255, 255, 255))     # paint background
        keys = pygame.key.get_pressed()         # get all currently pressed keys

        for event in pygame.event.get():
                # close when the corner x button is clicked
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        if mode == "overworld":
                mode = overworld.runOverworld(config.playerChars, config.enemies, keys)
                #print "overworld"
        elif mode == "battle":
                #print "you are here"
                #mode = battle.runBattle(config.playerChars, config.enemies, units)
                newBattle = battle2.Battle(config.playerChars, config.enemies, 0) # eventually that number should be a variable that keeps track of what the current level is
                #mode = battle.runBattle(config.playerChars, enemies, units)
                mode = battle2.runBattle (config.playerChars, config.enemies, newBattle)
        else:
                print "WARNING: Invalid mode detected. Expected 'battle' or 'overworld', instead found", mode

        pygame.display.update()
