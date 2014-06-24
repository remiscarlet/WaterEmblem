import pygame
import random
import math


class Torpedo(object):
	def __init__(self, torpStat, startingPos, dest, **kwargs):
		self.pos = startingPos
		self.dest = dest
		self.power = torpStat


class Recon(object):
	def __init__(self, reconStat):
		self.stat = reconStat


class Bombers(object):
	def __init__(self, bomberStat):
		self.power = bomberStat

class TorpedoBombers(object):
	def __init__(self, torpedoStat):
		self.power = torpedoStat

