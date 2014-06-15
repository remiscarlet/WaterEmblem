#########################################
######  Sound Initialisation File  ######
#########################################
import os
import pygame

class SFX(object):
	def __init__(self):
		self.dismantle = pygame.mixer.Sound(os.path.join('sounds','sfx','2-4-11.ogg'))
		self.cancel = pygame.mixer.Sound(os.path.join('sounds','sfx','Cancel.ogg'))
		self.select = pygame.mixer.Sound(os.path.join('sounds','sfx','Select.ogg'))
		self.battleStart = pygame.mixer.Sound(os.path.join('sounds','sfx','Battle Start.ogg'))
		self.resupply = pygame.mixer.Sound(os.path.join('sounds','sfx','Resupply.ogg'))
		self.victoryS = pygame.mixer.Sound(os.path.join('sounds','sfx','Victory S.ogg'))
		self.victoryA = pygame.mixer.Sound(os.path.join('sounds','sfx','Victory A.ogg'))
		self.victoryB = pygame.mixer.Sound(os.path.join('sounds','sfx','Victory B.ogg'))
		self.repairList = pygame.mixer.Sound(os.path.join('sounds','sfx','Repair List.ogg'))
		self.questComplete = pygame.mixer.Sound(os.path.join('sounds','sfx','Quest Complete.ogg'))
		self.equipment = pygame.mixer.Sound(os.path.join('sounds','sfx','Equipment.ogg'))
		self.craftFail = pygame.mixer.Sound(os.path.join('sounds','sfx','Craft Fail.ogg'))
		self.compass = pygame.mixer.Sound(os.path.join('sounds','sfx','Compass.ogg'))
		self.modernize = pygame.mixer.Sound(os.path.join('sounds','sfx','Modernize.ogg'))
		self.sonarShort = pygame.mixer.Sound(os.path.join('sounds','sfx','Sonar (Short).ogg'))
		self.sonarLong = pygame.mixer.Sound(os.path.join('sounds','sfx','Sonar (Long).ogg'))
		self.cursorMove = pygame.mixer.Sound(os.path.join('sounds','sfx','Cursor Move.ogg'))

	def setVolume(self, vol):
		self.dismantle.set_volume(vol)
		self.cancel.set_volume(vol)
		self.select.set_volume(vol)
		self.battleStart.set_volume(vol)
		self.resupply.set_volume(vol)
		self.victoryS.set_volume(vol)
		self.victoryB.set_volume(vol)
		self.victoryA.set_volume(vol)
		self.repairList.set_volume(vol)
		self.questComplete.set_volume(vol)
		self.equipment.set_volume(vol)
		self.craftFail.set_volume(vol)
		self.compass.set_volume(vol)
		self.modernize.set_volume(vol)
		self.sonarShort.set_volume(vol)
		self.sonarLong.set_volume(vol)
		self.cursorMove.set_volume(vol)


class BGM(object):
	def __init__(self):
		self.battleBoss = os.path.join('sounds','bgm','Battle Boss.ogg')
		self.battle = os.path.join('sounds','bgm','Battle.ogg')
		self.eventBattle = os.path.join('sounds','bgm','Event Battle.ogg')
		self.eventBattle2 = os.path.join('sounds','bgm','Event Battle 2.ogg')
		self.eventBoss = os.path.join('sounds','bgm','Event Boss.ogg')
		self.eventBoss2 = os.path.join('sounds','bgm','Event Boss 2.ogg')
		self.port = os.path.join('sounds','bgm','Port.ogg')
		self.quests = os.path.join('sounds','bgm','Quests.ogg')
		self.Sortie = os.path.join('sounds','bgm','Sortie.ogg')

