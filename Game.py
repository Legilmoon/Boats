# -*-coding:Utf-8-*

import pygame
from pygame.locals import *
from Map import *
from Boats import *


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
fullgrid_size= (20,11)
mapsize = 9
tilesize = 64

#repetition des touches
pygame.key.set_repeat(40, 30)

###### fenetre et son
window = pygame.display.set_mode((tilesize* (fullgrid_size[0]), tilesize*(fullgrid_size[1])) )#,RESIZABLE)
sono = pygame.mixer.Sound("Trinity.wav")
sono.play()


### creation du fond et de la grille, puis de la 'map' de tiles
grid = Grid(fullgrid_size[0], fullgrid_size[1], "background_black.jpg",tilesize)
commandMap = Map(mapsize, mapsize, tilesize)
tile_set = load_tile_table("blocks.png", tilesize, tilesize)
flotte_1 = Fleet()

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
				flotte_1.tilt()
			elif event.key == K_UP:
				position_perso = position_perso.move((0,-3))
			elif event.key == K_LEFT:
				position_perso = position_perso.move((-3,0))
			elif event.key == K_RIGHT:
				position_perso = position_perso.move((3,0))

	#dessin du fond, puis des cases, ensuite actualisation
	grid.draw(window)
	commandMap.draw(window, tile_set)  
	flotte_1.draw(window, tile_set)
	pygame.display.flip() 

