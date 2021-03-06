import pygame
import math
import os

class GameInfoPanel2(object):
	def __init__(self, currentLevel):
		self.fullSurf = pygame.Surface((128,128))
		self.rect = (128,0,128,128)
		self.borderTemplate = pygame.Surface((128,128), pygame.SRCALPHA, 32).convert_alpha()
		pygame.draw.rect(self.borderTemplate, (0,0,0), (0,0,128,128), 1) 
		self.minimapInit(currentLevel)
		self.minimapOverlayInit(currentLevel)


	def minimapInit(self, currentLevel):
		fullMap = currentLevel.mapRender
		width,height = currentLevel.width,currentLevel.height
		#This gets the ratio of size between the minimap (128x128) and the actual map layout.
		#We will use this ratio to scale everything in the minimap based off of the actual mapsurf we draw on the board
		#as well as the "current view" window. Note the 128.0 because integer division
		self.sizeRatio = max(width,height)/128.0 
		self.minimap = pygame.transform.smoothscale(fullMap, (int(width/self.sizeRatio)-1,int(height/self.sizeRatio)-1))
		self.minimapRect = self.minimap.get_rect()
		self.widthPad = (128-self.minimapRect[2])/2.0
		self.heightPad = (128-self.minimapRect[3])/2.0
		self.minimapRect.topleft = (self.widthPad,self.heightPad)
		self.scaleTileSize = 32.0/self.sizeRatio

	def minimapOverlayInit(self, currentLevel):
		overlay = pygame.Surface((640,352), pygame.SRCALPHA, 32).convert_alpha()
		temp = pygame.Surface((640,352))
		temp.fill((20,20,20))
		blit_alpha(overlay, temp, (0,0,640,352), 100)
		self.overlay = pygame.transform.smoothscale(overlay, (int(640/self.sizeRatio),int(352/self.sizeRatio)))
		pygame.draw.rect(self.overlay, (0,0,0), (0,0,int(640/self.sizeRatio),int(352/self.sizeRatio)), 1)
		self.overlayRect = self.overlay.get_rect()
		self.overlayTopLeft = (self.widthPad,self.heightPad)
		self.overlayRect.topleft = self.overlayTopLeft


	def update(self, currentLevel):
		topLeft = currentLevel.boardViewTopLeft
		self.overlayRect = (int(topLeft[0]*self.scaleTileSize+self.overlayTopLeft[0]),
							int(topLeft[1]*self.scaleTileSize+self.overlayTopLeft[1]),
							self.overlayRect[2],self.overlayRect[3])
		self.fullSurf.blit(self.minimap,self.minimapRect)
		self.fullSurf.blit(self.overlay, self.overlayRect)



class GameInfoPanel3(object):
	def __init__(self):
		self.fullSurf = pygame.Surface((128,128))
		self.rect = (256,0,128,128)
		#Make sure to render a blank/alpha surface
		self.borderTemplate = pygame.Surface((128,128), pygame.SRCALPHA, 32).convert_alpha()
		pygame.draw.rect(self.borderTemplate, (0,0,0), (0,0,128,20), 1)
		pygame.draw.rect(self.borderTemplate, (0,0,0), (0,0,128,128), 1)
		self.titleSurf = pygame.Surface((128,20))
		self.titleSurf.fill((255,255,255))
		self.titleSurfRect = (0,0,128,20)
		self.imageSurf = pygame.Surface((128,108))
		self.imageSurfRect = (0,20,128,108)


	#TileType should be all undercase name of the tile
	#"this" is just the self of the parent class, or the main class.
	def update(self, tileType, this):
		tile = None
		if tileType == "o": tile = "ocean"
		if tileType == "s": tile = "shallow"
		tempText = this.dialogueFont.render(tile.capitalize(), True, (0,0,0))
		width = this.dialogueFont.size(tile)[0]
		padding = (128-width)/2
		self.titleSurf.fill((255,255,255))
		self.titleSurf.blit(tempText, (padding,0))
		self.imageSurf.blit(eval("this.tilePortraits."+tile), (0,0))
		self.drawPanel()

	def drawPanel(self):
		self.fullSurf.blit(self.titleSurf, self.titleSurfRect)
		self.fullSurf.blit(self.imageSurf, self.imageSurfRect)
		self.fullSurf.blit(self.borderTemplate,(0,0))

class GameInfoPanel4(object):
	def __init__(self):
		self.fullSurf = pygame.Surface((128,128))
		self.fullSurf.fill((255,255,255))
		UIPath = os.path.join(os.path.curdir,"img","UI")
		self.hpOverlay = pygame.image.load(os.path.join(UIPath,"HP Bar Overlay.png"))
		self.hpRed = pygame.image.load(os.path.join(UIPath,"HP Bar Red.png"))
		self.hpOrange = pygame.image.load(os.path.join(UIPath,"HP Bar Orange.png"))
		self.hpGreen = pygame.image.load(os.path.join(UIPath,"HP Bar Green.png"))
		self.rect = (384,0,128,128)
		self.borderTemplate = pygame.Surface((128,128), pygame.SRCALPHA, 32).convert_alpha()
		pygame.draw.rect(self.borderTemplate, (0,0,0), (0,0,128,128), 1)
		self.icons = dict()
		self.iconRect = dict()
		self.stats = dict()
		self.statRect = dict()
		self.iconSurf = pygame.Surface((128,128))
		self.iconSurf.fill((255,255,255))
		iconList = ["armor","asw","firepower","torpedo","aa","los"]
		for i in xrange(len(iconList)):
			icon = iconList[i]
			self.icons[icon] = pygame.image.load(os.path.join(os.path.curdir,"img","UI","Icon_"+icon+".png"))
			self.stats[icon] = 0
			self.statRect[icon] = ((i/3)*64+32,(i%3)*32+40,16,16)
			self.iconRect[icon] = ((i/3)*64+8,(i%3)*32+40,16,16)
			self.iconSurf.blit(self.icons[icon],self.iconRect[icon])



	def update(self, kanmusu, this):
		self.fullSurf.blit(self.iconSurf,(0,0))
		for key in self.stats:
			val = str(eval("this.currentLevel.kanmusuDict[kanmusu]."+key))
			tempText = this.statFont.render(val, True, (0,0,0))
			self.fullSurf.blit(tempText, self.statRect[key])
		hp,maxhp = this.currentLevel.kanmusuDict[kanmusu].currentHP,this.currentLevel.kanmusuDict[kanmusu].maxHP
		self.drawHealthBar(hp, maxhp, this)
		self.fullSurf.blit(self.borderTemplate, (0,0))


	def drawHealthBar(self,hp,maxhp,this):
		percentage = int(math.ceil((float(hp)/maxhp)*100))
		rect = (0,0,percentage,18)
		if percentage>=70:
			self.fullSurf.blit(self.hpGreen,(14,24),rect)
		if percentage>40 and percentage<70:
			self.fullSurf.blit(self.hpOrange,(14,24),rect)
		if percentage<40:
			self.fullSurf.blit(self.hpRed,(14,24),rect)
		self.fullSurf.blit(self.hpOverlay,(14,24))
		hpText = this.statFont.render(str(hp)+"/"+str(maxhp),True,(0,0,0))
		self.fullSurf.blit(hpText, (14,5,100,14))



class GameInfoPanel5(object):
	def __init__(self):
		self.fullSurf = pygame.Surface((128,128))
		self.fullSurf.fill((255,255,255))
		self.rect = (512,0,128,128)
		#Make sure to render a blank/alpha surface
		self.borderTemplate = pygame.Surface((128,128), pygame.SRCALPHA, 32).convert_alpha()
		pygame.draw.rect(self.borderTemplate, (0,0,0), (0,108,128,20), 1)
		pygame.draw.rect(self.borderTemplate, (0,0,0), (0,0,128,128), 1)
		self.titleSurf = pygame.Surface((128,20))
		self.titleSurf.fill((255,255,255))
		self.titleSurfRect = (0,108,128,20)
		self.imageSurf = pygame.Surface((128,108))
		self.imageSurfRect = (0,0,128,108)

	#TileType should be all undercase name of the tile
	#"this" is just the self of the parent class, or the main class.
	def update(self, kanmusu, this):
		tempText = this.dialogueFont.render(kanmusu.capitalize(), True, (0,0,0))
		width = this.dialogueFont.size(kanmusu)[0]
		padding = (128-width)/2
		self.titleSurf.fill((255,255,255))
		self.titleSurf.blit(tempText, (padding,0))
		self.imageSurf.fill((0,0,0))
		self.imageSurf.blit(this.currentLevel.kanmusuDict[kanmusu].miniPortrait, (0,0))
		self.drawPanel()

	def drawPanel(self):
		self.fullSurf.blit(self.titleSurf, self.titleSurfRect)
		self.fullSurf.blit(self.imageSurf, self.imageSurfRect)
		self.fullSurf.blit(self.borderTemplate,(0,0))

class ContextMenu(object):
	def __init__(self):
		self.bg = pygame.image.load(os.path.join(os.path.curdir,"img","UI","ContextMenuBG.png"))
		self.menu = pygame.image.load(os.path.join(os.path.curdir,"img","UI","ContextMenuNormal.png"))
		self.select = pygame.image.load(os.path.join(os.path.curdir,"img","UI","ContextMenuSelect.png"))
		self.selectRect = [0,0,0,96]
		self.image = pygame.Surface((100,96),pygame.SRCALPHA, 32).convert_alpha()
		self.image.blit(self.bg,(0,0))
		self.image.blit(self.select,self.selectRect)
		self.image.blit(self.menu,(0,0))
		self.tick = 0
		self.selected = None
		self.pos = 0
		self.isOn = False
	def update(self, move=None):
		self.tick += 1
		self.selectRect[2] = self.selectRect[2]+6 if self.selectRect[2]<=90 else 96
		if move == "up":
			self.pos = (self.pos-1) if self.pos >=1 else 2
		if move == "down":
			self.pos = (self.pos+1)%3
		self.selectRect[1] = self.pos*32
		self.image.fill(0)
		self.image.blit(self.bg,(0,0))
		self.image.blit(self.select,self.selectRect)
		self.image.blit(self.menu,(0,0))
	def reset(self):
		self.pos = 0
		self.isOn = False
		self.update()


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

