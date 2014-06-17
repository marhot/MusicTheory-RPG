import sys, pygame
import config, overworld
from unit import PlayerChar, Enemy
from pygame.locals import *

#tallis = PlayerChar("Tallis", 1, "pianist", 20, 20, 20, "images/allyPlaceholder")
marhot = Enemy(10, "Marhot", 1, "flautist", 20, 20, 20, "images/enemyPlaceholder")
#playerChars = []
enemies = []
#playerChars.append(tallis)
enemies.append(marhot)
mode = "overworld"
overworld.init(config.playerChars, enemies)

while True:
	config.SCREEN.fill((255, 255, 255))	# paint background
	keys = pygame.key.get_pressed()		# get all currently pressed keys

	for event in pygame.event.get():
		# close when the corner x button is clicked
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if mode == "overworld":
		overworld.runOverworld(config.playerChars, enemies, keys)
	elif mode == "battle":
		mode = battle.runBattle(config.playerChars, enemies, units)
	else:
		print "WARNING: Invalid mode detected. Expected 'battle' or 'overworld', instead found", mode

	pygame.display.update()
