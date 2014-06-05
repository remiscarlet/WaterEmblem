import pygame
import math
import random
import os
import sprites




class Kanmusu(object):
	#kanmusu should be supplied in a lowercase name of kanmusu
	def __init__(self, kanmusu):
		#Once we have a file with all the numbers, I'll pull it from there. For now, hardcoded.
		self.hp = 50
		self.armor = 60
		self.los = 70
		self.evasion = 30
		self.firepower = 0
		self.torpedo = 0
		self.aa = 50
		self.asw = 0
		self.speed = 1
		self.range = 2
		self.luck = 20
		self.slots = 4
		self.aircraft = (20,20,46,12)
		self.remodel = 30
		self.fuel = 100
		self.ammo = 130
		self.miniPortrait = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu portraits","kaga.png"))
		self.name = "Kaga"
		self.sprites = sprites.UnitSprite("kaga")