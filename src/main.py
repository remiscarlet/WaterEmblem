#######################################
###### Main file for WaterEmblem ######
#######################################
import os
import pygame
import random
import gui
import sprites
import defaultVals
import string
import sounds
import levels
import popup
try: 
	import thread
except ImportError:
	import dummy_thread as thread

#############################
###### Primary Class ######
#############################
class WaterEmblem(object):
	############################
	###### Initialisation ######
	############################
	def __init__(self, config, win):
		self.init(config, win)

	def init(self, config, win):
		self.varInit(config, win)
		self.fontInit()
		self.configInit(config)
		self.preGuiInit()
		self.levelInit()
		self.guiInit()
		self.soundInit()
		self.keyInit(config)
		self.spriteInit()

	def varInit(self, config, win=None):
		#self.configInit(config)
		#screenSize = config["Screen Size"].split("x")
		self.isRunning = True
		self.trueWidth = 640#int(screenSize[0])
		self.trueHeight = 480#int(screenSize[1])
		self.width,self.height = 640,480
		self.clock = pygame.time.Clock()
		self.ticks = 0 #Used for general events
		self.win = pygame.Surface((640,480))
		self.trueWin = win
		self.status = {"menu":False, "options":False, "paused":False, "instructions":False,
					   "editor":False, "playing":True, "gameOver":False, "gameWin":False}
		self.musicPlaying = False

	def fontInit(self):
		self.dialogueFont = pygame.font.Font(os.path.join(os.path.curdir,'fonts','LTYPE.TTF'), 16)
		self.nameFont = pygame.font.Font(os.path.join(os.path.curdir,'fonts','LTYPE.TTF'), 8)

	def configInit(self, config):
		self.config = config
		#Set the vols of sfx and bgm to float from 0 to 1
		self.config["SFX"] = int(self.config["SFX"])/100.0
		self.config["BGM"] = int(self.config["BGM"])/100.0

	def preGuiInit(self):
		self.gameBoardWin = pygame.Surface((640,352))
		self.gameBoardWinRect = (0,0,640,352) #Topleft corner of gameBoardWin on the display surface to blit to
		self.gameInfoWin = pygame.Surface((640,128))
		self.gameInfoWinRect = (0,352,640,128) #Same as above

	def levelInit(self):
		self.currentLevel = levels.Level(self)


	############################################################################
	########### Entire below code should be looked at after UI is finalized ####
	############################################################################
	def guiInit(self):
		class tilePortraitInit(object):
			def __init__(self):
				self.ocean = pygame.image.load(os.path.join(os.path.curdir,"img","tile portraits", "actual_ocean.png"))
				self.oceanRect = self.ocean.get_rect()
				self.shallow = pygame.image.load(os.path.join(os.path.curdir,"img","tile portraits", "shallow.png"))
				self.shallowRect = self.shallow.get_rect()
		class kanmusuPortraitInit(object):
			def __init__(self):
				self.kaga = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu portraits", "kaga.png"))
				self.kagaRect = self.kaga.get_rect()
		self.tilePortraits = tilePortraitInit()
		self.kanmusuPortraits = kanmusuPortraitInit()
		#panel 1
		self.gameInfoPanel1 = pygame.Surface((128,128))
		self.gameInfoPanel1.fill((255,255,255))
		gameMenu = pygame.image.load(os.path.join(os.path.curdir,"img","menu","Temp Game Menu Button.png"))
		fleetMenu = pygame.image.load(os.path.join(os.path.curdir,"img","menu","Temp Fleet Menu Button.png"))
		self.gameInfoPanel1.blit(gameMenu, (0,0))
		self.gameInfoPanel1.blit(fleetMenu, (0,20))
		pygame.draw.rect(self.gameInfoPanel1, (0,0,0), (0,0,128,128), 1)
		self.gameInfoPanel1Rect = (0,0,128,128)
		#panel 2
		#self.gameInfoPanel2 = pygame.Surface((128,128))
		#self.gameInfoPanel2.fill((255,255,255))
		#pygame.draw.rect(self.gameInfoPanel2, (0,0,0), (0,0,128,128), 1)
		#self.gameInfoPanel2Rect = (128,0,128,128)
		self.gameInfoPanel2 = gui.GameInfoPanel2(self.currentLevel)
		self.gameInfoPanel2.update(self.currentLevel)
		#panel 3
		self.gameInfoPanel3 = gui.GameInfoPanel3()
		self.gameInfoPanel3.update("o", self)
		#panel 4
		self.gameInfoPanel4 = gui.GameInfoPanel4()
		self.gameInfoPanel4.update("kaga", self)
		#panel 5
		self.gameInfoPanel5 = gui.GameInfoPanel5()
		self.gameInfoPanel5.update("kaga", self)
		#self.gameInfoPanel5 = pygame.Surface((128,128))
		#self.gameInfoPanel5.fill((255,255,255))
		#pygame.draw.rect(self.gameInfoPanel5, (0,0,0), (0,0,128,128), 1)
		#self.gameInfoPanel5Rect = (512,0,128,128)
		############################################################################
		########### Entire above code should be looked at after UI is finalized ####
		############################################################################

	def soundInit(self):
		self.bgm = sounds.BGM()
		self.sfx = sounds.SFX()
		self.sfx.setVolume(self.config["SFX"])

	def keyInit(self, config):
		try:
			self.leftKey = int(eval("pygame."+config["Left"]))
			self.rightKey = int(eval("pygame."+config["Right"]))
			self.upKey = int(eval("pygame."+config["Up"]))
			self.downKey = int(eval("pygame."+config["Down"]))
		except:
			config = remakeConfig()
			self.leftKey = int(eval("pygame."+config["Left"]))
			self.rightKey = int(eval("pygame."+config["Right"]))
			self.upKey = int(eval("pygame."+config["Up"]))
			self.downKey = int(eval("pygame."+config["Down"]))
		pygame.key.set_repeat(100, 50)

	def spriteInit(self):
		self.playerUIGroup = pygame.sprite.Group()
		self.currentLevel.cursor = sprites.Cursor(self.currentLevel)
		self.playerUIGroup.add(self.currentLevel.cursor)

	#############################
	###### Events Handling ######
	#############################

	def events(self):
		#Because the gameplay requires constant stream of keypress
		#information, continuously send anyway.
		if self.status["playing"]: self.playingUpdate()
		#for all other events
		for event in pygame.event.get():
			#quit when x button is pressed
			if event.type == pygame.QUIT: self.isRunning = False
			#check that the event has attr of key to prevent crashes
			if hasattr(event, 'key'):
				keys = pygame.key.get_pressed()
				if (event.key == self.upKey or event.key == self.downKey or
					event.key == self.leftKey or event.key == self.rightKey):
					if self.status["playing"]: self.playingUpdate(keys)




	def menuUpdate(self, key):
		pass

	def resetMenuButtons(self):
		pass

	def instructionsUpdate(self, key):
		pass

	def optionsUpdate(self, key):
		pass

	def resetOptionButtons(self):
		pass

	def pausedUpdate(self, key):
		pass

	def gameOverUpdate(self, key):
		pass

	def gameWinUpdate(self, key):
		pass

	def playingUpdate(self, keys=None):
		self.playerUIGroup.update()
		self.gameInfoPanel2.update(self.currentLevel)
		if keys != None:
			up = keys[self.upKey]
			down = keys[self.downKey]
			left = keys[self.leftKey]
			right = keys[self.rightKey]
			if down:
				self.currentLevel.cursor.moveCursor((0,-1), self.currentLevel)
				tileType = self.currentLevel.map[self.currentLevel.cursor.truePos[1]][self.currentLevel.cursor.truePos[0]]
				self.gameInfoPanel3.update(tileType,self)
			if up:
				self.currentLevel.cursor.moveCursor((0,+1), self.currentLevel)
				tileType = self.currentLevel.map[self.currentLevel.cursor.truePos[1]][self.currentLevel.cursor.truePos[0]]
				self.gameInfoPanel3.update(tileType,self)
			if left:
				self.currentLevel.cursor.moveCursor((-1,0), self.currentLevel)
				tileType = self.currentLevel.map[self.currentLevel.cursor.truePos[1]][self.currentLevel.cursor.truePos[0]]
				self.gameInfoPanel3.update(tileType,self)
			if right:
				self.currentLevel.cursor.moveCursor((+1,0), self.currentLevel)
				tileType = self.currentLevel.map[self.currentLevel.cursor.truePos[1]][self.currentLevel.cursor.truePos[0]]
				self.gameInfoPanel3.update(tileType,self)




	#########################
	###### GUI Drawing ######
	#########################

	def drawMenu(self):
		pass

	def playMusic(self, track):
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.fadeout(1000) 
		pygame.mixer.music.load(track)
		pygame.mixer.music.set_volume(self.config["BGM"])
		pygame.mixer.music.play(-1)

	def drawPlaying(self):
		def drawBoardPanel():
			boardTopLeft = self.currentLevel.boardViewTopLeft
			width = self.currentLevel.width if self.currentLevel.width<640 else 640
			height = self.currentLevel.height if self.currentLevel.height<352 else 352
			topLeft = (boardTopLeft[0]*32,boardTopLeft[1]*32,width,height)
			self.gameBoardWin.blit(self.currentLevel.mapSurf, (self.currentLevel.widthPad,self.currentLevel.heightPad), topLeft)
		def drawInfoPanel():
			def drawPanel1():
				self.gameInfoWin.blit(self.gameInfoPanel1,self.gameInfoPanel1Rect)
			def drawPanel2():
				self.gameInfoWin.blit(self.gameInfoPanel2.fullSurf,self.gameInfoPanel2.rect)
			def drawPanel3():
				self.gameInfoWin.blit(self.gameInfoPanel3.fullSurf,self.gameInfoPanel3.rect)
			def drawPanel4():
				self.gameInfoWin.blit(self.gameInfoPanel4.fullSurf,self.gameInfoPanel4.rect)
			def drawPanel5():
				self.gameInfoWin.blit(self.gameInfoPanel5.fullSurf,self.gameInfoPanel5.rect)
			drawPanel1()
			drawPanel2()
			drawPanel3()
			drawPanel4()
			drawPanel5()

		drawBoardPanel()
		drawInfoPanel()

		self.win.blit(self.gameBoardWin, self.gameBoardWinRect)
		self.win.blit(self.gameInfoWin, self.gameInfoWinRect)
		for sprite in self.playerUIGroup:
			if isinstance(sprite, sprites.Cursor):
				blit_alpha(self.win,sprite.white, sprite.rect, sprite.alpha)
			self.win.blit(sprite.image,sprite.rect)

	def drawEditor(self):
		pass

	def drawOptions(self):
		pass

	def drawInstructions(self):
		pass

	def redrawAll(self):
		self.win.fill((0,0,44))
		self.drawMenu()
		self.drawPlaying()
		self.drawEditor()
		self.drawOptions()
		self.drawInstructions()
		pygame.transform.scale(self.win, (self.trueWidth, self.trueHeight), self.trueWin)
		pygame.display.update()
		


	def run(self):
		while self.isRunning == True:
			self.clock.tick(30)
			self.ticks += 1
			self.events()
			self.redrawAll()
		pygame.quit()

###############################
###### Main Run Function ######
###############################

def run():
	#Grab some vals from the config
	config = dict()
	fin = fout = None
	#Load and parse the config file.
	try:
		fin = open("config.txt", "rt")
		contents = fin.readlines()
		assert(defaultVals.verify(contents, "config"))
		config = parseConfigVals(contents)
	except:
		config = remakeConfig()
	finally:
		if fin != None: fin.close()
		if fout != None: fout.close()
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init()
	pygame.mixer.set_num_channels(32)
	pygame.init()
	pygame.display.set_caption("Water Emblem")
	#pygame.display.set_icon(pygame.image.load(os.path.join(os.path.curdir,"img","gui","icon.png")))
	pygame.mouse.set_visible(1)
	pygame.event.set_allowed(None)
	pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN])
	screenSize = config["Screen Size"].split("x")
	trueWidth = int(screenSize[0])
	trueHeight = int(screenSize[1])
	win = pygame.display.set_mode((trueWidth,trueHeight))
	game = WaterEmblem(config, win)
	game.run()
	#except:
	#	popup.error("Fatal Error", "Yikes! A fatal error just occurred!\nFear not though, I'll just restart the program.\nBasically, pygame sucks.")
	#	run()
#########################
##### Helper Funcs ######
#########################

def remakeConfig():
	config = dict()
	popup.error("Incorrect Config", "No config file exists or is broken! Creating new one!")
	fout = open("config.txt", "wt")
	fout.write(defaultVals.config())
	fout.close()
	return parseConfigVals(defaultVals.config().split("\n"))

def parseConfigVals(config):
	#Incase for whatever reason the provided config data
	#hasn't yet been split into lines yet.
	if type(config) != list:
		config = config.split("\n")
	listOfVals = dict()
	#add the vals to a dict with the keys 
	for line in config:
		index = line.find(":")
		if index != -1:
			val = line[index+1:].strip(string.whitespace)
			key = line[0:index].strip(string.whitespace)
			listOfVals[key] = val
	return listOfVals

def modifyConfigVals(key, val):
	fin = fout = None
	try:
		fin = open("config.txt", "rt")
		fout = open("temp.txt","wt")
		content = fin.read()
		start = string.find(content, key)+len(key)+1
		end = string.find(content, "\n", start)
		part1 = content[:start]
		part2 = " "+str(val)
		part3 = content[end:]
		fout.write(part1+part2+part3)

	except:
		config = remakeConfig()
	finally:
		if fin != None: fin.close()
		if fout != None: fout.close()
		os.remove("config.txt")
		os.rename("temp.txt","config.txt")

# http://www.nerdparadise.com/tech/python/pygame/blitopacity/
# Alpha blitting for per-pixel alpha surfaces	
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)










####################
# THE ALL HOLY RUN #
####################
####################
run() ##############
####################
####################

#  .----.-----.-----.-----.
# /      \     \     \     \
#|  \/    |     |   __L_____L__
#|   |    |     |  (           \
#|    \___/    /    \______/    |
#|        \___/\___/\___/       |
# \      \     /               /
#  |                        __/
#   \_                   __/
#    |        |         |
#    |                  |
#    |                  |


























