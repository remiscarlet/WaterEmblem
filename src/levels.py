import pygame
import random
import math
import gui
import terrain
import popup
import os
import sprites
import reachable
import kanmusu

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

TESTMAP2 = [['s','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','s','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','s','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','s','s','s','o','o','o','o','o','o','o','o','o','o','o','o','s','o','o','o','o','o',],
		   ['o','o','s','s','s','s','s','o','o','o','o','o','o','o','o','o','s','o','s','o','o','o','o',],
		   ['o','o','s','s','s','s','s','s','o','o','o','o','o','o','o','s','o','s','o','s','o','o','o',],
		   ['o','o','s','o','o','s','s','s','s','o','o','o','o','o','s','o','s','s','s','o','s','o','o',],
		   ['o','s','o','o','o','s','s','s','s','o','o','o','o','s','o','o','o','s','o','o','o','s','o',],
		   ['o','o','o','s','o','o','s','s','s','o','o','o','o','o','o','s','o','o','o','s','o','o','o',],
		   ['o','o','s','o','o','o','o','o','o','o','o','o','o','o','s','o','o','s','o','o','s','o','o',],
		   ['o','s','o','o','o','o','o','o','o','o','o','o','o','s','o','o','o','o','o','o','o','s','o',],
		   ['o','o','s','o','o','o','o','o','o','o','o','o','s','o','o','o','o','o','o','o','o','o','s',],
		   ['o','o','o','s','o','o','o','o','o','o','o','s','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','s','o','o','o','o','o','s','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','s','o','o','o','s','o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','s','o','s','o','o','o','o','o','o','o','o','o','o','o','o','o','o',],
		   ['o','o','o','o','o','o','o','s','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o',]]

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

TESTMAPUNITPOS2 = [[' ',' ',' ',' ',' ',' ',' ','A','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ','B',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',],
				  ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',],
				  [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',]]


TESTUNITLIST = {"1":"kaga","2":"taihou","3":"kongou","4":"inazuma","A":"wo","B":"re","C":"ru"}

class Level(object):
	def __init__(self, this):
		self.tiles = terrain.Tiles(self)
		self.preMapInit()
		self.spriteInit()
		self.mapInit(this)
		self.varInit()

	#	self.oceanTile = pygame.image.load(os.path.join(os.path.curdir,"img","tiles","actual_ocean.png"))
	#	pygame.draw.rect(self.oceanTile, (0,0,200), (0,0,32,32), 1)
	#	self.shallowTile = pygame.image.load(os.path.join(os.path.curdir,"img","tiles","actual_shallow.png"))
	#	pygame.draw.rect(self.shallowTile, (0,0,200), (0,0,32,32), 1)

	############
	#Eventually should modify code so it uses portraits from here and not from main.py. Bad organization.
	############
	#def tilePortraitInit(self):
	#	self.ocean = pygame.image.load(os.path.join(os.path.curdir,"img","tile portraits", "actual_ocean.png"))
	#	self.oceanRect = self.ocean.get_rect()
	#	self.shallow = pygame.image.load(os.path.join(os.path.curdir,"img","tile portraits", "shallow.png"))
	#	self.shallowRect = self.shallow.get_rect()

	def preMapInit(self):
		self.map = TESTMAP2
		self.unitPos = TESTMAPUNITPOS2
		self.playerPos = self.getShipPos()
		self.enemyPos = self.getShipPos(1)

	def spriteInit(self):
		self.kanmusuDict = dict()
		self.enemyDict = dict()
		for key in self.playerPos:
			self.kanmusuDict[key] = kanmusu.Kanmusu(key,self.playerPos[key])
		for key in self.enemyPos:
			self.enemyDict[key] = kanmusu.Enemy(key,self.enemyPos[key])
	##############
	## mapInit initializes the map and related data
	##############
	def mapInit(self, this):
		self.size = (len(self.map),len(self.map[0])) #TUPLE OF MAP SIZE. Y THEN X. AGAIN, ROW THEN COL
		self.width = self.size[1]*32
		self.height = self.size[0]*32
		self.mapRender = self.drawMap() #Makes a map surface the size of the map with 32x32 being the size of one tile
		self.mapSurf = pygame.Surface((32*self.size[1],32*self.size[0]))
		self.widthPad,self.heightPad = 0,0
		#boardViewTopLeft is the topleft position of the board currently on-screen.
		#This is for maps that are larger than the actual display screen (Read: Almost all maps)
		#This allows to keep reference as to what portion of the map is currently visible.
		self.boardViewTopLeft = [0,0]
		#because gameBoardWinRect is a Rect, 2nd and 3rd indices are the width and height.
		#self = this class. this = parent class. Horrible code. Will fix later.
		if self.width<this.gameBoardWinRect[2]: self.widthPad = (this.gameBoardWinRect[2]-self.width)/2
		if self.height<this.gameBoardWinRect[3]: self.heightPad = (this.gameBoardWinRect[3]-self.height)/2
		self.terrainCostMap = list()
		self.visionCostMap = list()
		for row in xrange(len(self.map)):
			self.terrainCostMap.append([])
			self.visionCostMap.append([])
			for col in xrange(len(self.map[row])):
				terrainType = self.map[row][col]
				if terrainType == "o": terrainType = "ocean"
				if terrainType == "s": terrainType = "shallow" 
				terrainCost = eval("self.tiles."+terrainType+".movementCost")
				visionCost = eval("self.tiles."+terrainType+".visionCost")
				self.terrainCostMap[row].append(terrainCost)
				self.visionCostMap[row].append(visionCost)

		#FOWVisibility is a list of positions that __ARE__ VISIBLE.
		self.updateFOWVisibility()

	def varInit(self):
		self.selectedKanmusu = None
		self.cursor = sprites.Cursor(self)
		self.turn = 0
		# activeAutoUnits are units the player don't control but require tick based timing.
		# Eg, fired torpedoes, aerial units, etc.
		# Maybe I should make it a dictionary with IDs?
		self.activeAutoUnits = list()



	###############
	## drawMap will take the map symbols and draw it as an actual pygame surface
	###############
	def drawMap(self):
		win = pygame.Surface((32*self.size[1],32*self.size[0]))
		for row in xrange(len(self.map)):
			for col in xrange(len(self.map[0])):
				tileType = self.map[row][col]
				pos = (32*col,32*row) #FLIPPING ROW AND COL HERE BECAUSE METHODS TAKE ARGS IN X AND Y, NOT Y AND X
				if tileType == "o":
					win.blit(self.tiles.ocean.image, pos)
				if tileType == "s":
					win.blit(self.tiles.shallow.image,pos)
		return win

	################
	## Returns a list of tiles visible based off of LoS and terrain vision cost.
	################
	# vessels should be supplied as either kanmusuDict or enemyDict
	def updateFOWVisibility(self):
		self.friendlyFOWVisibility = set()
		self.enemyFOWVisibility = set()
		vessels = [self.kanmusuDict,self.enemyDict]
		for i in xrange(len(vessels)):
			for vessel in vessels[i]:
				vessel = vessels[i][vessel]
				los = vessel.los
				distance = 3 if los<30 else round(los/10.0)
				visibility = reachable.reachable(self.visionCostMap, vessel.pos[0], vessel.pos[1], distance)[1]
				if i == 0: 
					for item in visibility:
						self.friendlyFOWVisibility.add(item)
				if i == 1:
					for item in visibility:
						self.enemyFOWVisibility.add(item)

		self.visibilityMap = pygame.Surface((32*self.size[1],32*self.size[0]), pygame.SRCALPHA, 32)
		gray = pygame.Surface((32,32), pygame.SRCALPHA, 32)
		gray.fill((155,155,155,150))
		for row in xrange(len(self.map)):
			for col in xrange(len(self.map[0])):
				if (col,row) in self.friendlyFOWVisibility: continue
				else:
					pos = (32*col,32*row) #FLIPPING ROW AND COL HERE BECAUSE METHODS TAKE ARGS IN X AND Y, NOT Y AND X
					self.visibilityMap.blit(gray, pos)

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
					pos[TESTUNITLIST[val]] = [col,row] #COL ROW -> X Y. NOTE THE INVERTED ORDER
				if whichPlayer == 1 and val.isalpha():
					pos[TESTUNITLIST[val]] = [col,row] #COL ROW -> X Y. NOTE THE INVERTED ORDER
		return pos

