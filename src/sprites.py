#####################################
###### Sprites Management File ######
#####################################
import sprites
import os
import pygame
import math
import random

class UnitSprite(pygame.sprite.Sprite):
	def __init__(self, kanmusu):
		pygame.sprite.Sprite.__init__(self)
		if os.access(os.path.join(os.path.curdir,"img","kanmusu",kanmusu,"Sprite.png"), os.F_OK):
			self.image = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu",kanmusu,"Sprite.png"))
		else:
			temp = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu",kanmusu,"13 - Portrait Small.png"))
			tempImage = pygame.transform.smoothscale(temp, (21,32))
			self.image = pygame.Surface((32,32), pygame.SRCALPHA).convert_alpha()
			self.image.blit(tempImage, (5,0))

class EnemySprite(pygame.sprite.Sprite):
	def __init__(self, ship, shipType):
		pygame.sprite.Sprite.__init__(self)
		temp = pygame.image.load(os.path.join(os.path.curdir,"img","enemy",ship,shipType+".png"))
		size = temp.get_rect()
		side = 32
		larger = max(size[3],size[2])
		ratio = float(larger)/side
		newWidth = int(size[2]/ratio)
		newHeight = int(size[3]/ratio)
		tempImage = pygame.transform.smoothscale(temp, (newWidth,newHeight))
		self.image = pygame.Surface((32,32), pygame.SRCALPHA).convert_alpha()
		widthPad = (32-newWidth)/2
		heightPad = (32-newHeight)/2
		self.image.blit(tempImage, (widthPad,heightPad))

class Cursor(pygame.sprite.Sprite):
	def __init__(self, currentLevel):
		pygame.sprite.Sprite.__init__(self)
		self.cursor = pygame.image.load(os.path.join(os.path.curdir,"img","UI","SelectionCursor.png"))
		self.white = pygame.Surface((32,32))
		self.white.fill((255,255,255))
		self.blank = pygame.Surface((32,32), pygame.SRCALPHA, 32).convert_alpha()
		self.image = pygame.Surface((32,32), pygame.SRCALPHA, 32).convert_alpha()
		self.image.blit(self.blank, (0,0))
		self.image.blit(self.cursor,(0,0))
		# MAPSIZE IA IN XY, NOT YX
		self.mapSize = (currentLevel.size[1],currentLevel.size[0])
		# POS IS SAVED AS XY, NOT YX.
		self.pos = [0,0]
		self.truePos = [self.pos[0]+currentLevel.boardViewTopLeft[0],self.pos[1]+currentLevel.boardViewTopLeft[1]]
		self.rect = self.image.get_rect()
		self.rect.topleft = (currentLevel.widthPad,currentLevel.heightPad)
		self.tick = 0
		self.alpha = 0


	def update(self):
		self.tick += 1
		if self.tick <= 20:
			self.alpha += 10
		if self.tick > 20:
			self.alpha -= 10 if self.alpha>0 else 0
			if self.tick>=50: self.tick = 0

	#############
	## Supplied dir should be a tuple with direction. Eg, (0,1), (-1,+1), (1,0), etc
	#############
	def moveCursor(self, direc, currentLevel):
		newPos = [self.pos[0]+direc[0],self.pos[1]-direc[1]]
		if (newPos[0]>=-1 and newPos[0]<self.mapSize[0] and
			newPos[1]>=-1 and newPos[1]<self.mapSize[1]):
			if (newPos[1]<11 and newPos[1]>=0 and
				newPos[0]<20 and newPos[0]>=0):
				self.pos = [self.pos[0]+direc[0],self.pos[1]-direc[1]]
				self.rect.topleft = (self.rect.left+32*direc[0],self.rect.top-32*direc[1])
			elif newPos[1]>=11 and currentLevel.boardViewTopLeft[1]<self.mapSize[1]-11:
				currentLevel.boardViewTopLeft[1]+=1
			elif newPos[1]==-1 and currentLevel.boardViewTopLeft[1]>0:
				currentLevel.boardViewTopLeft[1]-=1
			elif newPos[0]>=20 and currentLevel.boardViewTopLeft[0]<self.mapSize[0]-20:
				currentLevel.boardViewTopLeft[0]+=1
			elif newPos[0]==-1 and currentLevel.boardViewTopLeft[0]>0:
				currentLevel.boardViewTopLeft[0]-=1
			self.truePos = [self.pos[0]+currentLevel.boardViewTopLeft[0],self.pos[1]+currentLevel.boardViewTopLeft[1]]



		
	




### NOT MY CODE ###
# http://www.pygame.org/wiki/RotateCenter
# No name provided to credit.
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
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



