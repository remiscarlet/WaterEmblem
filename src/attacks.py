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
		#
		# Okay I think I know what I'm doing.
		# First, figure out just how many steps/turns/ticks it's going to take. Since torps travel 1 tile per tick and this is a quad-directional movement system
		# We can just take L1 distance (Manhattan). That's simple (Done above). After that, we know how long it takes so we get the x and y offsets from start to dest
		# and divide both by the smaller value. Let's assume x is smaller and y is larger. For now, assume x=3 and y=7. If we divide both by 3, we get x2=1 and y2=2.
		# Now what we have is a single "section" within the total number of movements. This one section is 1 of x movements (horizontal) and 2 of y, vertical. 
		# This one section, for example, might be the following movements: left, up, up. Now this is one section, we multiply this section by the smaller of x and y; x, or 3.
		# This gives us the movements: left up up, left up up, left up up. This in total now has an offset of x=3 and y=6. The second for loop takes care of what you might
		# consider the "remainder" and adds one more of the y, or "up". Now our final moveset is left up up, left up up, left up up, up. The algorithm below obviously
		# takes care of negative offsets and whatot as well.
		#
		# Just be mindful of the yx input and the xy output. (Rowcol and (x,y) cartesian)
		#
		self.path = list()
		smaller = min(abs(dx),abs(dy))
		tempddx,tempddy = abs(dx)/float(smaller),abs(dy)/float(smaller)
		ddx = int(tempddx)*-1 if dx<0 else int(tempddx)
		ddy = int(tempddy)*-1 if dy<0 else int(tempddy)
		tempddy = tempddy*-1 if tempddy<0 else tempddy
		tempddx = tempddx*-1 if tempddx<0 else tempddx
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
	def update(self):
		dx,dy = self.path[self.tick]
		self.pos = self.pos[0]+dy,self.pos[1]+dx
		if self.tick <self.dist:
			self.tick+=1
		else: self.destroy
	def destroy(self):
		pass


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

