import pygame
import math
import random
import os
import sprites

KAGA = {"hp":79,"armor":51,"los":72,"evasion":51,"firepower":11,"torpedo":0,"aa":62,"asw":6,"speed":6,
	    "range":2,"luck":12,"slots":4,"aircraft":(20,20,46,12),"remodel":30,"fuel":100,"ammo":130,"class":"cv"}
TAIHOU = {"hp":67,"armor":40,"los":47,"evasion":33,"firepower":0,"torpedo":0,"aa":42,"asw":0,"speed":6,
	    "range":2,"luck":2,"slots":4,"aircraft":(18,18,18,7),"remodel":40,"fuel":100,"ammo":130,"class":"cv"}
KONGOU = {"hp":75,"armor":89,"los":37,"evasion":52,"firepower":135,"torpedo":0,"aa":73,"asw":2,"speed":8,
	    "range":3,"luck":12,"slots":4,"aircraft":(3,3,3,3),"remodel":25,"fuel":100,"ammo":130,"class":"fastbb"}

WO = {"hp":85,"armor":40,"los":40,"evasion":4,"firepower":0,"torpedo":0,"aa":30,"asw":0,"speed":6,
	    "range":3,"luck":1,"slots":3,"aircraft":(27,27,27),"class":"cv"}
RE = {"hp":180,"armor":110,"los":50,"evasion":45,"firepower":90,"torpedo":100,"aa":80,"asw":90,"speed":6,
	    "range":4,"luck":60,"slots":4,"aircraft":(0,0,0,140),"class":"bbv"}
RU = {"hp":90,"armor":70,"los":20,"evasion":3,"firepower":65,"torpedo":0,"aa":70,"asw":0,"speed":3,
	    "range":4,"luck":5,"slots":3,"aircraft":(3,3,3),"class":"bb"}


class Kanmusu(object):
	#kanmusu should be supplied in a lowercase name of kanmusu
	def __init__(self, kanmusu, pos):
		#Once we have a file with all the numbers, I'll pull it from there. For now, hardcoded.
		kanmusu = kanmusu.upper()
		self.hp = eval(kanmusu+"[\"hp\"]")
		self.armor = eval(kanmusu+"[\"armor\"]")
		self.los = eval(kanmusu+"[\"los\"]")
		self.evasion = eval(kanmusu+"[\"evasion\"]")
		self.firepower = eval(kanmusu+"[\"firepower\"]")
		self.torpedo = eval(kanmusu+"[\"torpedo\"]")
		self.aa = eval(kanmusu+"[\"aa\"]")
		self.asw = eval(kanmusu+"[\"asw\"]")
		self.speed = eval(kanmusu+"[\"speed\"]")
		self.range = eval(kanmusu+"[\"range\"]")
		self.luck = eval(kanmusu+"[\"luck\"]")
		self.slots = eval(kanmusu+"[\"slots\"]")
		self.aircraft = eval(kanmusu+"[\"aircraft\"]")
		self.remodel = eval(kanmusu+"[\"remodel\"]")
		self.fuel = eval(kanmusu+"[\"fuel\"]")
		self.ammo = eval(kanmusu+"[\"ammo\"]")
		self.shipClass = eval(kanmusu+"[\"class\"]")
		self.pos = pos
		kanmusu = kanmusu.lower()
		image = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu",kanmusu,"9 - Card Vector.png"))
		tempImage = pygame.transform.smoothscale(image, (128,192))
		self.miniPortrait = pygame.Surface((128,108))
		self.miniPortrait.blit(tempImage,(0,0,128,108))
		self.name = kanmusu.capitalize()
		self.sprite = sprites.UnitSprite(kanmusu)

class Enemy(object):
	#shipType is the variant of the ship. Eg, kai, flagship, flagship-kai, elite, etc.
	def __init__(self, ship, pos, shipType="normal"):
		#Once we have a file with all the numbers, I'll pull it from there. For now, hardcoded.
		ship = ship.upper()
		self.hp = eval(ship+"[\"hp\"]")
		self.armor = eval(ship+"[\"armor\"]")
		self.los = eval(ship+"[\"los\"]")
		self.evasion = eval(ship+"[\"evasion\"]")
		self.firepower = eval(ship+"[\"firepower\"]")
		self.torpedo = eval(ship+"[\"torpedo\"]")
		self.aa = eval(ship+"[\"aa\"]")
		self.asw = eval(ship+"[\"asw\"]")
		self.speed = eval(ship+"[\"speed\"]")
		self.range = eval(ship+"[\"range\"]")
		self.luck = eval(ship+"[\"luck\"]")
		self.slots = eval(ship+"[\"slots\"]")
		self.aircraft = eval(ship+"[\"aircraft\"]")
		self.shipClass = eval(ship+"[\"class\"]")
		self.pos = pos
		ship = ship.lower()
		image = pygame.image.load(os.path.join(os.path.curdir,"img","enemy",ship,shipType+".png"))
		size = image.get_rect()
		newWidth = 128
		ratio = float(size[2])/newWidth
		newHeight = int(size[3]/ratio)
		tempImage = pygame.transform.smoothscale(image, (newWidth,newHeight))
		self.miniPortrait = pygame.Surface((128,108))
		self.miniPortrait.blit(tempImage,(0,0,128,108))
		self.name = ship.capitalize()
		self.sprite = sprites.EnemySprite(ship, shipType)