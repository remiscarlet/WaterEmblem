import os
import pygame


class basicAnimation(object):
	def __init__(self):
		self.tick = 0
		self.blackOverlayThing = pygame.image.load(os.path.join(os.path.curdir,"img","UI", "Battle - Friendly Template Overlay.png")).convert_alpha()
		#self.blackOverlayThing = pygame.Surface((640,352), pygame.SRCALPHA, 32)
		#self.blackOverlayThing.blit(temp,(0,0))
		#self.blackOverlayThing.convert_alpha()
		self.equipment = pygame.image.load(os.path.join(os.path.curdir,"img","equipment","friendly","35.6cm.png"))
		self.blackOverlayThingRect = [0,0,100,352]
		self.blackOverlayThingAlpha = 4
		self.attacker = None
		self.defender = None
	#newBattle is called whenever a new animation is started. Essentially a callable init that only "re-inits"
	#necessary info such as the attacker and defender stuff.
	def newBattle(self):
		self.tick = 0
	#update will be called per tick to update the animation. newBattle will reset the tick count.
	def update(self):
		self.tick += 1
		#overlaything
		if self.tick <=5:
			self.blackOverlayThingAlpha += 50
		if self.tick <=3:
			self.blackOverlayThingRect[2] += 180
		if self.tick >= 40:
			self.blackOverlayThingAlpha -= 50

class ShipToShipBattle(basicAnimation):
	def __init__(self, attacker, friendly=True):
		basicAnimation.__init__(self)
		if friendly:
			self.attacker = pygame.image.load(os.path.join(os.path.curdir,"img","kanmusu",attacker,"9 - Card Vector.png"))
			self.attackerRect = [-20,0]
			self.attackerAlpha = 0
	def update(self):
		basicAnimation.update(self)
		if self.tick<=5:
			self.attackerRect[0]+=5
			self.attackerAlpha+=50
		if self.tick>=35:
			self.attackerRect[0]+=5
			self.attackerAlpha-=50
		return self.tick>= 45

class AircraftToShipBattle(basicAnimation):
	def __init__(self):
		pass
	def newBattle(self, attacker, defender):
		pass

class LandToShipBattle(basicAnimation):
	def __init__(self):
		pass
	def newBattle(self, attacker, defender):
		pass

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location, location)