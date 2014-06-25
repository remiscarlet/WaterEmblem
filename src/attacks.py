import pygame
import random
import math


#
# STARTING POS AND DESTINATION ARE PROVIDED ROW,COL. EG, Y X.
# SELF.PATH IS PROVIDED IN A LIST OF DIRECTIONS, OR X Y. EG (0,1), (-1,1), (-1,-1)
#
class Torpedo(object):
	def __init__(self, torpStat, startingPos, dest, **kwargs):
		self.pos = startingPos
		self.dest = dest
		self.power = torpStat
		dx,dy = dest[1]-self.pos[1],dest[0]-self.pos[0]
		self.dist = abs(dx)+abs(dy) #cuz manhattan distance
		self.tick = 0 
		self.path = list()
		smaller = min(abs(dx),abs(dy))
		tempddx,tempddy = abs(dx)/float(smaller),abs(dy)/float(smaller)
		ddx = int(tempddx)*-1 if dx<0 else int(tempddx)
		ddy = int(tempddy)*-1 if dy<0 else int(tempddy)
		tempddy = tempddy*-1 if tempddy<0 else tempddy
		tempddx = tempddx*-1 if tempddx<0 else tempddx
		#
		# BASICALLY THE FOLLOWING MAGICALLY MAKES THE PATH.
		# I'LL DOCUMENT IT PROPERLY EVENTUALLY
		# RIGHT NOW I DON'T EVEN KNOW HOW IT REALLY WORKS
		#
		for i in xrange(smaller):
			if tempddy>tempddx:
				direction = (0,+1 if dy>0 else -1)
			if tempddy<=tempddx:
				direction = (+1 if dx>0 else -1,0)
			for j in xrange(max(ddy,ddx)):
				self.path.append(direction)
			if tempddy<=tempddx:
				direction = (0,+1 if dy>0 else -1)
			if tempddy>tempddx:
				direction = (+1 if dx>0 else -1,0)	
			self.path.append(direction)
		for i in xrange(self.dist-len(self.path)):
			if tempddy>tempddx:
				direction = (0,+1 if dy>0 else -1)
			if tempddy<tempddx:
				direction = (+1 if dx>0 else -1,0)
			self.path.append(direction)
		print "REMEMBER THIS IS PROVIDED IN (X,Y) FORM. INPUTS ARE [Y,X] OR [ROW,COL]. ADJUST ACCORDINGLY."
		print self.path


# READ THE INFO ABOVE THE CLASS. INVERTED X AND Y CUZ ROWCOL VS XY
test = Torpedo(0,(2,0),(9,3))



class Recon(object):
	def __init__(self, reconStat):
		self.stat = reconStat


class Bombers(object):
	def __init__(self, bomberStat):
		self.power = bomberStat

class TorpedoBombers(object):
	def __init__(self, torpedoStat):
		self.power = torpedoStat

