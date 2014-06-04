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
		tempText = this.dialogueFont.render(tileType.capitalize(), True, (0,0,0))
		width = this.dialogueFont.size(tileType)[0]
		padding = (128-width)/2
		self.titleSurf.blit(tempText, (padding,0))
		self.imageSurf.blit(eval("this.tiles."+tileType), (0,0))
		self.drawPanel()

	def drawPanel(self):
		self.fullSurf.blit(self.titleSurf, self.titleSurfRect)
		self.fullSurf.blit(self.imageSurf, self.imageSurfRect)
		self.fullSurf.blit(self.borderTemplate,(0,0))
