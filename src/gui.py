import pygame
import math
import os

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
class GameInfoPanel5(object):
	def __init__(self):
		self.fullSurf = pygame.Surface((128,128))
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
		self.imageSurf.blit(eval("this.kanmusuPortraits."+kanmusu), (0,0))
		self.drawPanel()

	def drawPanel(self):
		self.fullSurf.blit(self.titleSurf, self.titleSurfRect)
		self.fullSurf.blit(self.imageSurf, self.imageSurfRect)
		self.fullSurf.blit(self.borderTemplate,(0,0))
