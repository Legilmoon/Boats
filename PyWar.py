# -*-coding:Utf-8-*

import pygame
from pygame.locals import *



class Grid:
	def __init__(self, nb_h, nb_v, bck, grid_size):
		self.horiz = nb_h
		self.vertic = nb_v
		self.background = pygame.image.load(bck).convert()
		self.gridSize = grid_size

	def draw(self, surface):
		surface.blit(self.background, (0,0)) 
		i=0
		while (i <= self.horiz+1):
			pygame.draw.line(surface, (0,0,244), (i*self.gridSize,0), (i*self.gridSize ,self.vertic* self.gridSize), 3)
			i+=1
		j=0
		while (j <= self.vertic+1):
			pygame.draw.line(surface, (0,0,244), (0,j*self.gridSize), (self.horiz* self.gridSize,j*self.gridSize), 3)	
			j+=1

class Tile: # Une case d'eau ou d'autre chose
	def __init__(self, let, num, stat, x, y):
		self.letter = let
		self.number = num
		self.state = stat
		self.posx = x
		self.posy = y

class Map: # grille de Tiles
	def __init__(self, nb_cases_h, nb_cases_v, gridSize):
		#Definition de la grille
		self.horiz = nb_cases_h
		self.vertic = nb_cases_v

		cx = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
		cy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

		self.tiles = []
		for tx in range(0, self.horiz):
			line = []
			self.tiles.append(line)
			for ty in range (0, self.vertic):
				line.append(Tile (cx[tx], cy[ty] , 0, tx*gridSize, ty*gridSize))
		

		print ("Carte créée: \n {}x{}\n".format(self.horiz, self.vertic))
		for tx in self.tiles:
			for ty in tx:
				print("({},{}), Px:{} Py:{}".format(ty.letter, ty.number, ty.posx, ty.posy))

	def change_state (self, x , y):
		if x< self.horiz and y< self.vertic:
			if self.tiles[x][y].state == 0:
				self.tiles[x][y].state = 1
			elif self.tiles[x][y].state == 1:
				self.tiles[x][y].state =0

	def draw (self, surface, tileset):
		for line in self.tiles:
			for tile in line:
				#choix du skin en fonction de l'etat ti.stats
				if(tile.state == 0):
					skin = tileset[7][0]
				elif (tile.state ==1):
					skin = tileset[6][0]
				#affichage du skin choisi	
				surface.blit(skin, (tile.posx , tile.posy))



#############fonction a mettre qqpart dans une classe

def load_tile_table(filename, width, height):
	image = pygame.image.load(filename).convert()
	image_width, image_height = image.get_size()
	tile_set = []
	for tile_x in range(0, image_width/width):
		line = []
		tile_set.append(line)
		for tile_y in range(0, image_height/height):
			rect = (tile_x*width, tile_y*height, width, height)
			line.append(image.subsurface(rect))
	print("tile_set chargee")
	return tile_set





pygame.init()


###### parametres de jeu

fullgrid_size= 12
mapsize = 9
tilesize = 64

#repetition des touches
pygame.key.set_repeat(40, 30)

###### fenetre
window = pygame.display.set_mode((tilesize* (fullgrid_size), tilesize*(fullgrid_size)) )#,RESIZABLE)

###### sono
sono = pygame.mixer.Sound("Trinity.wav")
#sono.play()

### creation du fond et de la grille, puis de la 'map' de tiles
grid = Grid(fullgrid_size, fullgrid_size, "background_black.jpg",tilesize)
commandMap = Map(mapsize, mapsize, tilesize)
tile_set = load_tile_table("blocks.png", tilesize, tilesize)


###### main loop
continuer = 1
while continuer:	
	for event in pygame.event.get():	#On parcours la liste de tous les événements reçus

		if event.type == QUIT:
			continuer = 0	

		if event.type == MOUSEBUTTONDOWN:
			posx,posy = event.pos 
			x = posx // grid.gridSize 
			y = posy // grid.gridSize
			commandMap.change_state(x,y)

		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				for t in commandMap.tiles:
					for ti in t:
						if ti.state == 0:
							ti.state = 1
						elif ti.state== 1:
							ti.state =0

			elif event.key == K_UP:
				position_perso = position_perso.move((0,-3))
			elif event.key == K_LEFT:
				position_perso = position_perso.move((-3,0))
			elif event.key == K_RIGHT:
				position_perso = position_perso.move((3,0))


	#dessin du fond, puis des cases, ensuite actualisation
	grid.draw(window)
	commandMap.draw(window, tile_set)  
	pygame.display.flip() 







