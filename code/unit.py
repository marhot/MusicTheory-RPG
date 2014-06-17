import sys, pygame, random
import config
from basicAttack import BasicAttack
from pygame.locals import *

# general framework of units
# children: PlayerChar, Enemy
class Unit(object):
	# create a unit with the given name, class, and stats, initializing at full HP
	def __init__(self, name, level, unitClass, HP, melody, rhythm, imgLoc):	
		# class statistics
		self.stats = {}
		self.basicAttacks = []
		self.name = name
		self.unitClass = unitClass
		self.level = level
		self.totalExp = 0
		self.expAtNext = int(4 * (level ** 3.15) + 10)
		self.expToNext = self.expAtNext - self.totalExp
		self.step = False
		self.stepNum = 0
		self.stepCount = 1

		# battle statistics
		self.status = "normal"
		self.stats["maxHP"] = HP
		self.stats["curHP"] = HP
		self.stats["melody"] = melody
		self.stats["rhythm"] = rhythm

		# drawing data
		self.x = 0
		self.y = 0
		self.direction = "down"
		self.imgLoc = imgLoc
                tmp = pygame.image.load(self.imgLoc + '/' + self.direction + ".png")
		self.width = tmp.get_size()[0]
		self.height = tmp.get_size()[1]
		self.foot = self.height * .25


	# print out name, class, all stats, and all learned moves
	def printSummary(self):
		print self.name
		print "level " + str(self.level) + ' ' + self.unitClass
		print "Total EXP: " + str(self.totalExp)
		print "Next: " + str(self.expAtNext)
		print "Remaining: " + str(self.expToNext)
		print "HP: " + str(self.stats["curHP"]) + " / " + str(self.stats["maxHP"])
		print "Melody: " + str(self.stats["melody"])
		print "Rhythm: " + str(self.stats["rhythm"])

		print "Basic Attacks:"
		for i in self.basicAttacks:
			print "   " + i.name + " " + i.power + ": " + i.description
		print ""


	# learn a new basic attack
	def addBasicAttack(self, name, power, description):
		newAttack = BasicAttack(name, power, description)
		self.basicAttacks.append(newAttack)


	# Take the given amount of damage. Use negative values for recovery.
	def takeDamage(self, dmg):
#		print self.name + " took " + str(dmg) + " damage."


		# CURRENTLY TRYING TO MAKE THE VALUE SHOW ABOVE THE TARGET'S HEAD AND DRIFT UPWARDS
		font = pygame.font.SysFont("timesNewRoman", 25)
		if dmg >= 0:	# red for damage
			dmgSurface = font.render(str(dmg), True, (255, 0, 0))
		else:			# green for healing
			dmgSurface = font.render(str(dmg), True, (0, 255, 0))
		dmgRect = dmgSurface.get_rect()
		dmgRect.midbottom = (self.x + 50, self.y)
		i = 0
		while i < 5:
			i += 1
			dmgRect.bottom -= 1
			pygame.draw.rect(SCREEN, (255, 255, 255), (dmgRect.left, dmgRect.top, dmgRect.right - dmgRect.left, dmgRect.bottom - dmgRect.top), 1)
			SCREEN.blit(dmgSurface, dmgRect)
			pygame.display.update()
			pygame.time.wait(100)

		self.stats["curHP"] -= dmg

		# HP will never exceed maximum or be negative
		if self.stats["curHP"] > self.stats["maxHP"]:
			self.stats["curHP"] = self.stats["maxHP"]
		elif self.stats["curHP"] <= 0:
			self.stats["curHP"] = 0
			self.status = "dead"
			print self.name + " died."


	# attack a target to deal damage
	# also checks for victory and awards experience accordingly
	def attack(self, move, accuracy, target):
		if move in self.basicAttacks:
			attack = self.stats["melody"]
			defense = target.stats["melody"]
			dmg = attack * move.power * move.power * accuracy * accuracy / defense / 15
			print self.name + " used " + move.name + " on " + target.name
			if target.status == "defend":
				dmg /= 2
			target.takeDamage(int(dmg), SCREEN)
			if isinstance(self, PlayerChar) and target.status == "dead":
				self.gainExp(target, accuracy)
		else:
			print "ERROR: " + self.name + " used invalid move " + move + " on " + target.name


	# change the x y position and direction
	def setLoc(self, xPos, yPos, direction):
		self.x = xPos
		self.y = yPos
		self.direction = direction


	# move in specified direction and change image to face that direction
	def move(self, direction):
		if(direction == "right"):
			self.direction = direction
			self.x += 4
		elif(direction == "left"):
			self.direction = direction
			self.x -= 4
		elif(direction == "up" and self.y >= 4):
			self.direction = direction
			if self.y >= 4:
				self.y -= 4
		elif(direction == "down" and self.y < config.SCREENY - 100):
			self.direction = direction
			if self.y < config.SCREENY - 100:
				self.y += 4


	# blit unit onto screen
	def draw(self):
                #print 'drawing ' + self.name + ' at (' + str(self.x) + ',' + str(self.y) + ')'
                #print config.OVERWORLD.curScene.order
                if self.step == True:
                        print self.stepCount
                        image = pygame.image.load(self.imgLoc + '/' + self.direction + str(self.stepNum) + '.png')
                        '''if self.stepNum == 0:
                                self.stepNum = 1
                        elif self.stepNum == 1:
                                self.stepNum = 0'''
                        if self.stepCount > 0:
                                self.stepNum = 1
                                self.stepCount += 1
                                if self.stepCount == 4:
                                        self.stepCount = -1
                        elif self.stepCount < 0:
                                self.stepNum = 0
                                self.stepCount -= 1
                                if self.stepCount == -4:
                                        self.stepCount = 1
                else:
                        image = pygame.image.load(self.imgLoc + '/' + self.direction + ".png")
		#image = pygame.image.load(self.imgLoc + '/' + self.direction + ".png")
		config.SCREEN.blit(image, (self.x, self.y))
		pygame.draw.circle(config.SCREEN, (255, 0, 0), (self.x, self.y), 10) 



class PlayerChar(Unit):

        def move(self, direction):
		if(direction == "right"):
			self.direction = direction
			self.x += 8
		elif(direction == "left"):
			self.direction = direction
			self.x -= 8
		elif(direction == "up" and self.y >= 4):
			self.direction = direction
			if self.y >= 8:
				self.y -= 8
		elif(direction == "down" and self.y < config.SCREENY - 100):
			self.direction = direction
			if self.y < config.SCREENY - 100:
				self.y += 8

		#check to see if entity is encountered
		for entity in config.OVERWORLD.curScene.entities:
                        #if (self.width > entity.loc[0] and self.x < entity.width) or (self.x < entity.width and self.x > entity.loc[0]):
                        if self.name != entity.name and (self.x >= entity.loc[0] and self.x <= entity.loc[0] + entity.width) or (self.x + self.width >= entity.loc[0] and self.x + self.width <= entity.loc[0] + entity.width) and ((self.y + self.height <= entity.loc[1] and self.y + self.height >= entity.loc[1] + entity.height) or (self.y >= entity.loc[1] and self.y <= entity.loc[1] + entity.height)):
                                #player has enocountered an entity in the x direction
                                print 'x collision between'
                                print ' '
                                print self.name
                                print ' and '
                                print entity.name
                                config.OVERWORLD.curScene.collision(self, entity, 'behind')
                                #if (entity.category == 'temporary string'):
                                        #START HERE
                                        
                if (self.x == 0):
                        print 'zero'


		#implement something for when world ends here
                tmpscn = config.OVERWORLD.curScene
		if (self.x + self.width/2 < 0):
                        config.OVERWORLD.changeScene('left', self.name)
                        if (config.OVERWORLD.curScene != tmpscn):
                                self.setLoc(config.SCREENX - self.width/2, self.y, self.direction)
                        else :
                                self.x = 0 -  self.width/2

                elif (self.x + self.width/2 > config.SCREENX):
                        config.OVERWORLD.changeScene('right', self.name)
                        if (config.OVERWORLD.curScene != tmpscn):
                                self.setLoc(-1 * self.width/2, self.y, self.direction)
                        else:
                                self.x = config.SCREENX - self.width/2
                                

	# change player status to defend
	def defend(self):
		self.status = "defend"
		print self.name + " defended."

	# gain experience and check for leveling up
	def gainExp(self, target, accuracy):
		print "Defeated enemy!"
		print "Gained " + str(target.expVal) + " experience"
		self.totalExp += target.expVal * accuracy
		if self.totalExp >= self.expAtNext:
			self.levelUp()


	# increase level by one, recalculate experience for next level, and increase stats
	def levelUp(self):
		self.level += 1
		self.expToNext = int(4 * (self.level ** 3.15) + 10)

		"""

		figure out how you want stat gains to work and put the code here

		"""


	# displays unit name, HP filled green to current percent, and integer values of current and maximum health
	# place in correct Y position based on y length of screen
	# potential errors: will not work without correct font installed on computer
	def showHPbar(self, screenY):
		X = 10
		Y = config.SCREENY - 40
		length = 80
		height = 20

		# draw bar
		pygame.draw.rect(config.SCREEN, (0, 255, 0), (X, Y, int(length * self.stats["curHP"] / self.stats["maxHP"]), height))	# shows percent remaining HP as green bar
		pygame.draw.rect(config.SCREEN, (0, 0, 0), (X, Y, length, height), 1)		# shows maximum HP as black border
		
		# create text surfaces
		font = pygame.font.SysFont("timesNewRoman", 18)
		
		slashSurface = font.render(" / ", True, (0, 0, 0))
		HPleftSurface = font.render(str(self.stats["curHP"]), True, (0, 0, 0))
		HPtotalSurface = font.render(str(self.stats["maxHP"]), True, (0, 0, 0))
		nameSurface = font.render(self.name, True, (0, 0, 0))

		# create rectangles of surfaces
		slashRect = slashSurface.get_rect()
		HPleftRect = HPleftSurface.get_rect()
		HPtotalRect = HPtotalSurface.get_rect()
		nameRect = nameSurface.get_rect()

		# move text to their respective locations
		slashRect.center = (X + length / 2, Y + height / 2)
		HPleftRect.topright = slashRect.topleft
		HPtotalRect.topleft = slashRect.topright
		nameRect.midbottom = (X + length / 2, Y)

		# print text
		SCREEN.blit(slashSurface, slashRect) 
		SCREEN.blit(HPleftSurface, HPleftRect)
		SCREEN.blit(HPtotalSurface, HPtotalRect)
		SCREEN.blit(nameSurface, nameRect)



class Enemy(Unit):
	def __init__(self, expVal, name, level, unitClass, HP, melody, rhythm, imgLoc):
		Unit.__init__(self, name, level, unitClass, HP, melody, rhythm, imgLoc)
		self.expVal = expVal			# maximum amount of experience gained from defeating
		self.wanderDirection = "none"	# direction of movement
		self.wanderTime = 0				# remaining time to move in current direction


	# randomly move around overworld, avoiding edge of screen
	def wander(self):
		# choose new direction and duration when current one expires
		if self.wanderTime <= 0:
			self.wanderTime = random.randint(1, 30)
			self.wanderDirection = random.randint(0, 5)

		# move according to wanderDirection
		if self.wanderDirection == 0:
			self.move("right")
		elif self.wanderDirection == 1:
			self.move("left")
		elif self.wanderDirection == 2:
			self.move("up")
		elif self.wanderDirection == 3:
			self.move("down")

		self.wanderTime -= 1
		self.draw()

