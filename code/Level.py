"""
This file organizes the different levels and provides individual functionality for each
"""

import sys, pygame, random
import config
from pygame.locals import *

lr = .5

class EnemyInfo (object):
    def __init__(self,num):
        self.encounters = 0
        self.wins = 0
        self.losses = 0
        self.NIT = False
        self.wa = 0

        def weightedAverage (self, num):
            self.wa = (1 - lr ) * self.wa +  lr * num
            if num == 0: # player has lost
                self.losses += 1
            elif num == 1: # player has won
                self.wins += 1
                

        def calculateNIT (self):
            if self.encounters >= 2 and self.wins >= self.losses + 2:
                NIT = True

class EnemyPool (object):
    def __init__(self):
        self.enemies = []

    def add_enemy(self, newEnemy):
        self.enemies.append(newEnemy)
        self.enemies(len(self.enemies)).name = EnemyInfo(len(self.enemies))


class Level(object):
    def __init__(self, num):
        self.num = num
        self.EnemyPool = EnemyPool()

    #Determines which enemies will generate in a scene, returns a list of two enemies
    def EnemyRandomizer(self):
        tempEnemies = []    #a list of all the enemies that have been encountered for this level, and one that hasn't
        tempChosen = []     #the list that will be returned containing to two enemies for the player to encounter
        #FIRST: Choose the enemies for temp enemies
        for enemy in self.EnemyPool.enemies:
            if enemy.NIT == False:  #Checks to see the most recently introduced enemy, an enemy is not recent once the NIT == True, only one recent enemy should appear at a time
                tempEnemies.append(enemy)
                break
            else:
                tempEnemies.append(enemy)
            if len(tempEnemies) = len(EnemyPool.enemies):   #if all the enemies in the pool are placed into the temp, there are no more enemies to add and the loop should break, not sure if this is necessary
                break

        #SECOND: Order the enemies by how many times they have been encountered from least to greatest.
        

        step = 0 #steo is initialized to zero, the first enemy in the list
        while len(tempChosen) < 2:
            randNum = random.randint(1, 100)
            if tempEnemies[step].NIT == False:
                chance = 100
            else:
               chance = (tempEnemies[step].losses/tempEnemies[step].wins)/tempEnemies.step[encounters]
            if randNum <= chance:
                tempChosen.append(tempEnemies[step])
            step += 1
            if step >= len(tempEnemies):
                step = 0

        return tempChosen
        
        
