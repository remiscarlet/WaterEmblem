import os
import shutil

soundPath = os.path.join(os.path.curdir,"sounds")
folders = os.listdir(soundPath)
mapping = {1:"Intro",2:"Secretary1",3:"Secretary2",4:"Secretary3",5:"Ship Constructed",6:"Expedition Complete",7:"Return from Sortie",8:"Show Rank",
		   9:"Equipment Resupply1",10:"Equipment Resupply2",11:"Docking Light",12:"Docking Heavy",13:"Joining Fleet",14:"Start Sortie",
		   15:"Battle Start",16:"Attack",17:"Night Attack",18:"Night Battle",19:"Under Fire1",20:"Under Fire2",21:"Heavy Damage",
		   22:"Sink",23:"MVP",24:"Wedding",25:"Library Info",26:"Equipment3",27:"Resupply",28:"Idle Married",29:"Idle",30:"0000",31:"0100",32:"0200",33:"0300",
		   34:"0400",35:"0500",36:"0600",37:"0700",38:"0800",39:"0900",40:"1000",41:"1100",42:"1200",43:"1300",44:"1400",45:"1500",
		   46:"1600",47:"1700",48:"1800",49:"1900",50:"2000",51:"2100",52:"2200",53:"2300"}
mapping2 = {"image 1":"Fleet Icon","image 3":"Fleet Icon Damaged","image 5":"Card","image 7":"Card Damaged","image 9":"Card Vector","image 11":"Card Vector Damaged",
			"image 13":"Portrait Small","image 15":"Portrait Small Damaged","image 16":"Portrait","image 17":"Portrait Large","image 18":"Portrait Damaged","image 19":"Portrait Large Damaged",
			"image 20":"Refuel","image 21":"Refuel Vector","image 22":"Refuel Damaged","image 23":"Refuel Vector Damaged","image 25":"Library Info Overlay","image 27":"Refuel","image 29":"Refuel Damaged"}
for kanmusu in folders:
		#try:
		soundFolder = os.path.join(soundPath,kanmusu)
		#print soundFolder
		files = os.listdir(soundFolder)
		for soundFile in files:
			if soundFile.find("."):
				fileName = soundFile.split(".")[1]
				if fileName == "mp3":
					os.remove(os.path.join(soundFolder,soundFile))
		#if os.access(soundFolder,os.F_OK):
		#	os.rmdir(soundFolder)




		#except: continue






'''
image1 - fleet icon
image3 - fleet icon damaged
image5 - card
image7 - card damaged
image9 - card vector
image11 - card vector damaged
image13 - portrait small
image15 - portrait small damaged
image17 - portrait large
image19 - portrait large damaged
image21 - refuel vector
image23 - refuel vector damaged
image25 - library info tab
image27 - refuel
image29 - refuel damaged












'''