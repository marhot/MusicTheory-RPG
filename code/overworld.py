import sys, pygame, random
import config, battle2 #battle
from unit import PlayerChar, Enemy
from pygame.locals import *

#import effects


#Overworld graph
class Overworld (object):
        def __init__(self):
                self.scenes = []
                self.curScene = None
                self.curLoc = (0, 0)

        def addScene (self, newScene):
                self.scenes.append(newScene)

        def setNeighbors (self, curScene, neighborScene, directionToNeighbor, directionFromNeighbor):
                curScene.addNeighbor(directionToNeighbor, neighborScene)
                neighborScene.addNeighbor(directionFromNeighbor, curScene)

        def changeScene (self, direction, unitName):
                if (self.curScene.neighbors[direction] != self.curScene):
                        for unit in self.curScene.units:
                                if (unit.name == unitName):
                                        self.curScene.deleteUnit(unit)
                                        self.curScene.neighbors[direction].addUnit(unit)
                        self.curScene = self.curScene.neighbors[direction]

        def displayCurScene(self):
                #image = pygame.image.load(self.curScene.imgLoc)
                #config.SCREEN.blit(image, (0,0))
                self.curScene.draw()

        def setCurScene(self, newScene):
                self.curScene = newScene




class Scene (object):
        def __init__(self,imgLoc):
                self.imgLoc = imgLoc
                self.entities = []
                self.units = []
                self.neighbors = {}
                self.neighbors['right'] = self
                self.neighbors['left'] = self
                self.order = []
                #orderNum = 0


        def addEntity(self, name, category, imgLoc, loc):
                tmp = Entity(name, category, imgLoc, loc)
                self.entities.append(tmp)
                self.order.append(tmp)

                if category == 'floor':
                        count = 0
                        for entry in self.order:
                                if entry.name == name:
                                        tmp = count
                                        break
                                count += 1
                        self.changeOrder(tmp, 0, 'front')


        def deleteEntity(self, entityName):
                for entityLoc in range (len(self.entities)):
                        if self.entities[entityLoc][0] == entityName:
                                self.entities.pop(entityLoc)


        def addUnit (self, newUnit):
                self.units.append(newUnit)
                self.order.append(newUnit)


        def deleteUnit(self, unit):
                self.units.remove(unit)


        def draw (self):
                image = pygame.image.load(self.imgLoc)
                config.SCREEN.blit(image, (0, 0))
                #for entity in self.entities:
                        #entity.draw()
                #for unit in self.units:
                        #unit.draw()
                #print self.order
                for entry in self.order:
                        entry.draw()
                        
                        
        def addNeighbor (self, direction, neighborScene):
                self.neighbors[direction] = neighborScene

       

        def collision (self, unit, entity, position):
                count = 0
                #check location of each
                if entity.category == 'floor':
                        #first find location on floor
                        floorLocY = int(unit.y + unit.height - unit.foot - (config.SCREENY - entity.height))
                        if floorLocY >= 0 and unit.y + unit.height <= config.SCREENY - 8 and unit.x >= 0 and unit.x <= config.SCREENX:
                                #print floorLocY
                                if entity.image.get_at((unit.x, floorLocY))[3] == 0:
                                        if unit.direction == 'right':
                                                unit.x -= 8
                                        elif unit.direction == 'left':
                                                unit.x += 8
                                        elif unit.direction == 'up':
                                                unit.y += 8
                                        elif unit.direction == 'down':
                                                unit.y -= 8

                if entity.category == 'platform':
                        if unit.y + unit.height + unit.z >= -4 + entity.loc[1] and unit.y + unit.height + unit.z <= 20 + entity.loc[1]:
                                unit.fall = False
                                #print 'landed on platform'

                                #'''and unit.z < 0'''
                        
                if entity.category != 'barrier':
                        return
                for entry in self.order:
                        if entry.name == unit.name:
                                tmp1 = count
                        elif entry.name == entity.name:
                                tmp2 = count
                        count += 1

                if tmp1 == tmp2:
                        print "error, unit and entity are occupying same space"

                if unit.y + unit.height > entity.loc[1] + entity.height and unit.prevY + unit.height < entity.loc[1] + entity.height:
                        #an attempt to pass through barrier has been made
                        unit.y -= 8
                        return

                elif unit.y + unit.height < entity.loc[1] + entity.height and unit.prevY + unit.height > entity.loc[1] + entity.height:
                        #an attempt to pass through barrier has been made
                        unit.y += 8
                        return


                if unit.y + unit.height >= entity.loc[1] + entity.height: #unit's y value is in front of entity
                        #place unit in front of entity
                        if tmp1 > tmp2: #unit is already in front of entity
                                return
                        if tmp1 < tmp2: #unit is behind entity and needs to be moved
                                #print 'placing unit in front'
                                self.changeOrder(tmp1, tmp2, 'back')
                #confirm if unit is in front of entity
                if (unit.y + unit.height < entity.loc[1] + entity.height): #unit's y value is behind entity's y value
                        #place unit behind entity
                        if tmp1 < tmp2: #unit is already in behind entity
                                return
                        if tmp1 > tmp2: #unit is in front of entity and needs to be moved
                                #print 'placing unit in behind'
                                self.changeOrder(tmp1, tmp2, 'forward')

                
                
        def changeOrder (self, unitLoc, entityLoc, direction):
                if direction == 'back':
                        tmp1 = self.order[unitLoc]
                        for x in range (unitLoc + 1, len(self.order)):
                                tmp2 = self.order[x]
                                self.order[x-1] = tmp2

                                if tmp2 == self.order[entityLoc]:
                                        self.order[entityLoc] = tmp1
                                        break

                if direction == 'forward':
                        #print 'forward recognized'
                        tmp1 = self.order[unitLoc]
                        x = unitLoc - 1
                        while x >= 0:     
                        #for x in range (unitLoc - 1, 0):
                                #print 'shifting'
                                tmp2 = self.order[x]
                                self.order[x + 1] = tmp2
                                x -= 1

                                if tmp2 == self.order[entityLoc]:
                                        self.order[entityLoc] = tmp1
                                        #print 'moved back'
                                        break
                                        
                if direction == 'front':
                        self.changeOrder(unitLoc, 0, 'forward')
                        return
                        
                                
        def collision_old (self, unit, entity, position):
                count = 0
                if position == 'behind':
                        #print 'checking order'
                        for entry in self.order:
                                if entry.name == unit:
                                        tmp1 = count
                                elif entry.name == entity:
                                        tmp2 = count
                                count += 1

                        if tmp1 == tmp2:
                                print 'error'
                        if tmp1 > tmp2:
                                print 'already behind'
                                return
                        if tmp1 < tmp2:
                                #print 'fixing order'
                                tmpEntity1 = self.order[tmp2]
                                for x in range (tmp2, len(self.order)):
                                        tmpEntity2 = self.order[x]
                                        self.order[x] = tmpEntity1
                                        tmpEntity1 = tmpEntity2
                                

class Entity (object):
        def __init__(self, name, category, imgLoc, loc):
                self.name = name
                self.category = category
                self.imgLoc = imgLoc
                self.loc = loc
                image = pygame.image.load(self.imgLoc)
                self.width = image.get_size()[0]
                self.height = image.get_size()[1]
                self.image = pygame.image.load(self.imgLoc)
                self.pxarray = pygame.PixelArray(image)

                if self.category == 'floor':
                        self.loc = (0, config.SCREENY - self.height)

                if self.category == 'platform':
                        self.z = -1 * self.height

        def draw(self):
                #print 'drawing tree'
                #print 'drawing ' + self.name + ' at (' + str(self.loc[0]) + ',' + str(self.loc[1]) + ')'
                image = pygame.image.load(self.imgLoc)
                config.SCREEN.blit(image, self.loc)
                


'''class Platform (Entity):
        def __init__(self, name, category, imgLoc, loc, z):
                self.name = name
                self.category = category
                self.imgLoc = imgLoc
                self.loc = loc
                image = pygame.image.load(self.imgLoc)
                self.width = image.get_size()[0]
                self.height = image.get_size()[1]
                self.image = pygame.image.load(self.imgLoc)
                self.pxarray = pygame.PixelArray(image)
                self.z = z'''
                
        

# initialize overworld with music [and other unimplemented things like character location]
# NEW TASK: initialize enemy locations randomly across map
def init(playerChars, enemies):
	for playerChar in playerChars:
		playerChar.setLoc(config.SCREENX / 2 - 150, config.SCREENY / 2 - 50, "right")
	for enemy in enemies:
		enemy.setLoc(config.SCREENX / 2 + 150, config.SCREENY / 2 - 50, "left")
	#pygame.mixer.music.load("music/overworldPlaceholder.wav")
	#pygame.mixer.music.play(-1, 0.0)


# run all unit actions in overworld
def runOverworld(playerChars, enemies, keys):
        config.OVERWORLD.displayCurScene()
	for playerChar in playerChars:
		act(playerChar, keys)
		for enemy in enemies:
			enemy.wander()
			if areTouching(playerChar, enemy):
				#battle.init(playerChar, enemy)
				return "battle"

	return "overworld"

	'''config.TEST.draw()
	config.T1 = pygame.time.get_ticks()
	print config.T1

	if (config.T1 - config.T2 >= 300):
                config.T2 = config.T1
                config.TEST.fill()'''
	
	#config.TEST.fill()


# return true if units are touching 
def areTouching(unit1, unit2):
	if unit1.x < unit2.x + unit2.width and unit1.x + unit1.width > unit2.x and unit1.y < unit2.y + unit2.height and	unit1.y + unit1.height > unit2.y:
		return True
	return False


# perform action in overworld based on keyboard input then blit image
def act(player, keys):
	if keys[K_RIGHT]:
		player.move("right")
		player.step = True
	elif keys[K_LEFT]:
		player.move("left")
                player.step = True
	elif keys[K_UP]:
		player.move("up")
		player.step = True
	elif keys[K_DOWN]:
		player.move("down")
		player.step = True
	else:
                player.step = False

        if keys[K_SPACE]:
                player.jump()

        if keys[K_1]:
                config.TEST.draw()

        if keys[K_2]:
                config.TEST.fill()
                config.T2 = pygame.time.get_ticks()
	#player.draw()

