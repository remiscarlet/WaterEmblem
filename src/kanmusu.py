import pygame
import math
import random
import os
import sprites




class Kanmusu(object):
	#kanmusu should be supplied in a lowercase name of kanmusu
	def __init__(self, kanmusu, pos):
		#Once we have a file with all the numbers, I'll pull it from there. For now, hardcoded.
		self.hp = 79
		self.armor = 51
		self.los = 72
		self.evasion = 51
		self.firepower = 11
		self.torpedo = 0
		self.aa = 62
		self.asw = 6
		self.speed = 3
		self.range = 1
		self.luck = 12
		self.slots = 4
		self.aircraft = (20,20,46,12)
		self.remodel = 30
		self.fuel = 100
		self.ammo = 130
		self.pos = pos
		self.miniPortrait = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu portraits","kaga.png"))
		self.name = kanmusu.capitalize()
		self.sprite = sprites.UnitSprite(kanmusu)