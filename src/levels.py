import pygame
import random
import math
import gui
import popup
import os
import sprites

# o = ocean
TESTMAP = [['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o',]]

TESTMAP2 = [['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','o','o','o','o','o','o',]]

TESTMAPUNITPOS = [[' ',' ',' ',' ',' ',' ',' ',' ','A','B',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ','C',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  ['3',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  ['1','2',' ',' ',' ',' ',' ',' ',' ',' ',]]

TESTMAPUNITPOS2 = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','A','B',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  ['3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  ['1','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',]]



class Level(object):
	def __init__(self, this):
		self.mapInit(this)

	##############
	## mapInit initializes the map and related data
	##############
	def mapInit(self, this):
		self.map = TESTMAP2
		self.unitPos = TESTMAPUNITPOS2
		self.playerPos = self.getShipPos()
		self.enemyPos = self.getShipPos(1)
		self.size = (len(self.map),len(self.map[0])) #TUPLE OF MAP SIZE. Y THEN X. AGAIN, ROW THEN COL
		self.width = self.size[1]*32
		self.height = self.size[0]*32
		self.mapSurf = self.drawMap() #Makes a map surface the size of the map with 32x32 being the size of one tile
		self.widthPad,self.heightPad = 0,0
		#because gameBoardWinRect is a Rect, 2nd and 3rd indices are the width and height.
		#self = this class. this = parent class. Horrible code. Will fix later.
		if self.width<this.gameBoardWinRect[2]: self.widthPad = (this.width-self.width)/2
		if self.height<this.gameBoardWinRect[3]: self.heightPad = (this.height-self.height)/2

	###############
	## drawMap will take the map symbols and draw it as an actual pygame surface
	###############
	def drawMap(self):
		win = pygame.Surface((32*self.size[1],32*self.size[0]))
		#oceanTile = pygame.Surface((32,32))
		#oceanTile.fill((0,0,150))
		oceanTile = pygame.image.load(os.path.join(os.path.curdir,"img","tiles","ocean.png"))
		pygame.draw.rect(oceanTile, (0,0,200), (0,0,32,32), 1)
		for row in xrange(len(self.map)):
			for col in xrange(len(self.map[0])):
				tileType = self.map[row][col]
				pos = (32*col,32*row) #FLIPPING ROW AND COL HERE BECAUSE METHODS TAKE ARGS IN X AND Y, NOT Y AND X
				if tileType == "o":
					win.blit(oceanTile, pos)
		return win

	#################
	## getShipPos will take the input map and return the positions of either the player's ships on the map or the enemy's ships based off of the input
	#################
	def getShipPos(self, whichPlayer = 0):
		highest = None
		found = 0
		for row in xrange(len(self.unitPos)):
			for col in xrange(len(self.unitPos[row])):
				currentVal = self.unitPos[row][col]
				if whichPlayer == 0 and currentVal.isdigit():
					if highest<currentVal: highest = currentVal
					found += 1
				if whichPlayer == 1 and currentVal.isalpha():
					if highest<currentVal: highest = currentVal
					found += 1
		if whichPlayer == 0 and found != int(highest): popup.error("Invalid Map!", "You have an invalid map!")
		if whichPlayer == 1 and found != ord(highest.lower())-ord('a')+1: popup.error("Invalid Map!", "You have an invalid map!")
		pos = dict()
		for row in xrange(len(self.unitPos)):
			for col in xrange(len(self.unitPos[row])):
				val =  self.unitPos[row][col]
				if whichPlayer == 0 and val.isdigit():
					pos[val] = [row,col] #ROW COL -> Y X. NOTE THE INVERTED ORDER
				if whichPlayer == 1 and val.isalpha():
					pos[val] = [row,col] #ROW COL -> Y X. NOTE THE INVERTED ORDER
		return pos