



#################################
######  Default Vals File  ######
#################################
'''
The purpose of this file is to provide several functions that will
provide "default" values for the game to write in the case that
a necessary file such as a config is missing.
'''

def config():
	return '''
###Config###

Screen Size: 640x480
BGM: 100
SFX: 100
Keybindings:
	Up: K_UP
	Down: K_DOWN
	Left: K_LEFT
	Right: K_RIGHT
	Confirm: K_z
	Cancel: K_x
'''

def getListOfVals(defVal):
	#Gets a list of entires in whatever file we're looking for.
	#The keys are denoted by the : symbol.
	content = eval(defVal+"()").split("\n")
	listOfVals = list()
	for line in content:
		index = line.find(":")
		if index != -1:
			listOfVals.append(line[0:index+1])
	return listOfVals


def verify(contents, defVal):
	#Incase for whatever crazy reason the provided contents
	#hasn't yet been split into lines yet.
	if type(contents) != list:
		contents = contents.split("\n")
	#find the keys we need to look for
	checkAgainst = getListOfVals(defVal)
	counter = 0
	for line in contents:
		line = line.strip("\n")
		#If we find the key we're looking for in the current line, increment
		#and look for the next key.
		if line.find(checkAgainst[counter]) == 0:
			counter+=1
		#If the counter and len are equal, it means we have found
		#all of the keys so at least that part of the config isn't broken.
		if counter == len(checkAgainst):
			return True
	return False















