# -*-coding:Utf-8-*

import pygame
from pygame.locals import *
from Map import *

class Boat:
	def __init__(self, siz, gridSize, ori, position):
		self.orientation = ori
		self.size = siz
		self.gridSize = gridSize
		self.pos = position
		self.tiles = []
		for ti in range(0, self.size):
			if self.orientation== 'H':
				self.tiles.append(Tile('boat','boat', 3, (self.pos[0]+ti)*gridSize, (self.pos[1])*gridSize)) 
			elif self.orientation == 'V':
				self.tiles.append(Tile('boat','boat', 3, (self.pos[0])*gridSize, (self.pos[1]+ti)*gridSize))

	def draw (self, surface, tileset):
		for tile in range(0,self.size):
			surface.blit(tileset[3][0], (self.tiles[tile].posx , self.tiles[tile].posy))

	def tilt (self):
		if self.orientation == 'H':
			self.orientation ='V'
			for ti in range(0,self.size):
				self.tiles[ti].setPos( self.pos[0]*self.gridSize, (self.pos[1]+ti)*self.gridSize )
		elif self.orientation =='V':
			self.orientation = 'H'
			for ti in range(0,self.size):
				self.tiles[ti].setPos( (self.pos[0]+ti)*self.gridSize , self.pos[1]*self.gridSize )


class Fleet:
	def __init__ (self):
		self.boats = [Boat(3, 64,'V', (10,1)), Boat (4, 64, 'H',(10, 5)), Boat (2, 64, 'V', (11,8)) ]

	def draw (self, surface, tileset):
		for boat_instance in self.boats:
			boat_instance.draw(surface, tileset)

	def tilt (self):
		for boat_instance in self.boats:
			boat_instance.tilt()


