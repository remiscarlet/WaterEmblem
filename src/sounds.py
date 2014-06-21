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
		'''self.dismantle.set_volume(vol)
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
		self.cursorMove.set_volume(vol)'''
		for key in self.__dict__:
			eval("self."+key+".set_volume(vol)")


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


#Because loading every voice for every ship in the game is a bad idea.
#Load only the ships being used. Eg, in fleet, in the battle map, etc.
#Don't load ship voices that we KNOW aren't going to be used.
#kanmusu should be supplied as a string.
class Voices(object):
	def __init__(self, kanmusu):
		print kanmusu
		self.intro = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu,'1 - Intro.ogg'))
		self.secretary1 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '2 - Secretary1.ogg'))
		self.secretary2 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '3 - Secretary2.ogg'))
		self.secretary3 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '4 - Secretary3.ogg'))
		self.shipConstructed = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '5 - Ship Constructed.ogg'))
		self.expeditionComplete = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '6 - Expedition Complete.ogg'))
		self.returnFromSortie = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '7 - Return from Sortie.ogg'))
		self.showRank = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '8 - ShowRank.ogg'))
		self.equipment1 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '9 - Equipment Resupply1.ogg'))
		self.equipment2 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '10 - Equipment Resupply2.ogg'))
		self.dockingLight = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '11 - Docking Light.ogg'))
		self.dockingHeavy = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '12 - Docking Heavy.ogg'))
		self.joiningFleet = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '13 - Joining Fleet.ogg'))
		self.startSortie = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '14 - Start Sortie.ogg'))
		self.battleStart = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '15 - Battle Start.ogg'))
		self.attack = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '16 - Attack.ogg'))
		self.nightAttack = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '17 - Night Attack.ogg'))
		self.nightBattle = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '18 - Night Battle.ogg'))
		self.underFire1 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '19 - Under Fire1.ogg'))
		self.underFire2 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '20 - Under Fire2.ogg'))
		self.heavyDamage = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '21 - Heavy Damage.ogg'))
		self.sink = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '22 - Sink.ogg'))
		self.mvp = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '23 - MVP.ogg'))
		self.libraryInfo = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '25 - Library Info.ogg'))
		self.equipment3 = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '26 - Equipment3.ogg'))
		self.resupply = pygame.mixer.Sound(os.path.join('sounds','kanmusu',kanmusu, '27 - Resupply.ogg'))
	def setVolume(vol):
		for key in self.__dict__:
			eval("self."+key+".set_volume(vol)")