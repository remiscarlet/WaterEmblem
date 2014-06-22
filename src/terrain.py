import pygame
import math
import random
import os
import sprites

#eval(terrainType+"[\"\"]")

OCEAN = {"movementCost":2,"defBonus":0,"visionCost":1}
SHALLOW = {"movementCost":2.5,"defBonus":0,"visionCost":1}

class Tiles(object):
	def __init__(self, this):
		self.ocean = Terrain("ocean",None)
		self.shallow = Terrain("shallow",None)


class Terrain(object):
	#terrainType should be supplied as an all lowercase tile name, eg "ocean"
	#direction only applies to ocean type tiles (ocean, shallow, etc) and should be supplied in a cardinal direction, "n","e","s","w", or "None"
	def __init__(self, terrainType, direction):
		self.type = terrainType
		self.image = pygame.image.load(os.path.join(os.path.curdir,"img","tiles","actual_"+terrainType+".png"))
		pygame.draw.rect(self.image, (0,0,200), (0,0,32,32), 1)
		terrainType = terrainType.upper()
		self.movementCost = eval(terrainType+"[\"movementCost\"]")
		self.defBonus = eval(terrainType+"[\"defBonus\"]")
		self.visionCost = eval(terrainType+"[\"visionCost\"]")
		self.direction = direction