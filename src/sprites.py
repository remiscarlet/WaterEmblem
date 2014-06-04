#####################################
###### Sprites Management File ######
#####################################
import sprites
import os
import pygame
import math
import random

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
		self.pos = [0,0]
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
	def moveCursor(self, direc):
		self.pos = [self.pos[0]+direc[0],self.pos[1]+direc[1]]
		self.rect.topleft = (32*self.pos[1],32*self.pos[0])


		
	




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



