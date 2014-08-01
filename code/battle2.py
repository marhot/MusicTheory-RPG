import sys, pygame
import config
from pygame.locals import *


class Battle (object):
    def __init__ (self, playerChars, enemies, levelNum):
        self.init = False
        self.phase = "player"
        self.levelNum = levelNum
        self.players = []
        self.enemies = []
        for player in playerChars:
            self.players.append(player)
        for enemy in enemies:
            self.enemies.append(enemy)


    '''def select (self):
        for player in players:
            player.BattleProfile.attacks'''


    #def select (self):
        #for player in players:
            #player.attack


    #def attack (self):
        #if self.phase == "player":

        #for player in players:
            #player

    #def start(playerChars, enemies):
        #for player in playerChars:
            #place players and enemies into pos
        #self.init = False




def init(players, enemies):
    
    px = 75
    ex = 200
    for player in players:
        player.setLoc(px, config.MENUTOP/ 2 - 50, "right")
        px += 50

    for enemy in enemies:
        enemy.setLoc(config.SCREENX - ex, config.MENUTOP / 2 - 50, "left")
        ex -= 50

    #player.setLoc(75, config.MENUTOP / 2 - 50, "right")
    #enemy.setLoc(config.SCREENX - 200, config.MENUTOP / 2 - 50, "left")
    #enemy.stats["curHP"] = enemy.stats["maxHP"]
    #enemy.status = "normal"


#def runbattle (playerChars, enemies):
    #if getBattleStatus(

#def buttonPressed(

#def movePointer(pointer, direction, step):

class Pointer(object):
    def __init__ (self, image, x, winY, loseY):
        self.image = image
        self.x = x
        self.winY = winY
        self.loseY = loseY
        self.currentLoc = "win"

        self.pointWin()
        print "made pointer"


    def pointWin(self):
        config.SCREEN.blit(self.image, (self.x, self.winY))
        pygame.display.update()

    def pointLose (self):
        config.SCREEN.blit(self.image, (self.x, self.loseY))
        pygame.display.update()

    def movePointer(self, direction):
        if direction == "up" and self.currentLoc == "lose":
            self.pointLose()
            self.currentLoc = "win"

        elif direction == "down" and self.currentLoc == "win":
            self.pointWin()
            self.currentLoc = "lose"

    def draw(self):
        if self.currentLoc == "win":
            config.SCREEN.blit(self.image, (self.x, self.winY))
        else:
            config.SCREEN.blit(self.image, (self.x, self.loseY))
        pygame.display.update()

def runBattle (playerChars, enemies, newBattle):
    print "at battle"
    battleBox = pygame.image.load("images/battlePlaceholder/battleBox.png")
    battleBoxX = config.SCREENX/2 - battleBox.get_size()[0]/2
    battleBoxY = config.SCREENY/2 - battleBox.get_size()[1]/2
    winButton = pygame.image.load("images/battlePlaceholder/winButton.png")
    loseButton = pygame.image.load("images/battlePlaceholder/loseButton.png")
    buttonWidth = winButton.get_size()[0]
    buttonHeight = winButton.get_size()[1]
    buttonX = battleBoxX + battleBox.get_size()[0]/2 - buttonWidth/2
    winY = battleBoxY + buttonHeight * 2/3
    loseY = battleBoxY + battleBox.get_size()[1] - buttonHeight * 2/3 - buttonHeight
    pointer = pygame.image.load("images/battlePlaceholder/pointer.png")
    print "all pictures loaded"
    pointerWidth = pointer.get_size()[0]
    pointerHeight = pointer.get_size()[1]
    pointerX = buttonX - pointerWidth * 3/2
    pointWinY = winY - pointerHeight/2 + buttonHeight/2
    pointLoseY = loseY - pointerHeight/2 + buttonHeight/2
    score = False
    config.SCREEN.blit(battleBox, (battleBoxX, battleBoxY))
    config.SCREEN.blit(winButton, (buttonX, winY))
    config.SCREEN.blit(loseButton, (buttonX, loseY))
    #config.SCREEN.blit(pointer, (pointerX, pointWinY))
    print "printed box and buttons"
    pointer2 = Pointer(pointer, pointerX, pointWinY, pointLoseY)
    #pointer2.draw()

    for player in playerChars:
        player.setLoc(75, config.MENUTOP/2 - 50, "right")
    for enemy in enemies:
        enemy.setLoc(config.SCREENX - 200, config.MENUTOP/2 -50, "left")

    print "characters loaded"

    pygame.display.update()

    #pointerKeys = pygame.key.get_pressed()

    while score == False:
        #print "entered while loop"

        config.SCREEN.blit(battleBox, (battleBoxX, battleBoxY))
        config.SCREEN.blit(winButton, (buttonX, winY))
        config.SCREEN.blit(loseButton, (buttonX, loseY))
        pointer2.draw()
        
        pointerKeys = pygame.key.get_pressed()
        #print keys[K_UP]
        #print keys[K_DOWN]
        
        if pointerKeys[K_UP]:
            pointer2.movePointer("up")
            print "yo"
        elif pointerKeys[K_DOWN]:
            pointer2.movePointer("down")
            print "ho"
        elif pointerKeys[K_RETURN]:
            print "here!"
            score = True

        #print keys

        pointer2.draw()

       

        pygame.display.update()
        pygame.event.pump()
            
    #config.scene1.deleteUnit(marhot)   

    return "overworld"



    


    

   
