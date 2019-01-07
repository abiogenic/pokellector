#!/usr/bin/env python3
# coding: utf-8

import pygame
import os
import sys

class spritesheet(object):
	def __init__(self, filename):
		try:
			self.sheet = pygame.image.load(filename).convert_alpha()
		except pygame.error as message:
			print('Unable to load spritesheet image:' + filename)
			raise SystemExit(message)
	# Load a specific image from a specific rectangle
	def image_at(self, rectangle, colorkey = None):
		"Loads sprite from x,y,x+offset,y+offset"
		rect = pygame.Rect(rectangle)
		#background = pygame.Surface(rect.size)
		sprite = pygame.Surface(rect.size).convert_alpha()
		#ackground.fill((238,238,238))
		sprite.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = sprite.get_at((0,0))
			sprite.set_colorkey(colorkey, pygame.RLEACCEL)
		sprite.blit(self.sheet, (0, 0), rect)
		return sprite
	# # Load a whole bunch of images and return them as a list
	# def images_at(self, rects, colorkey = None):
	# 	"Loads multiple images, supply a list of coordinates" 
	# 	return [self.image_at(rect, colorkey) for rect in rects]
	# # Load a whole strip of images
	# def load_strip(self, rect, image_count, colorkey = None):
	# 	"Loads a strip of images and returns them as a list"
	# 	tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
	# 			for x in range(image_count)]
	# 	return self.images_at(tups, colorkey)

""" -------- """
def display_sprite(spritesheet_filename, sprite_x, sprite_y):
	pygame.init()

	display_width = 500
	display_height = 500

	gameDisplay = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption("Pokéllector")

	black = (0,0,0)
	grey = (238,238,238)
	white = (255,255,255)
	system_blue = (123,213,251)

	clock = pygame.time.Clock()

	ss = spritesheet(spritesheet_filename)
	# Sprite is 128x128 pixels at location sprite_x, sprite_y in the file...
	image = ss.image_at((sprite_x, sprite_y, 128, 128), -1)
	# image.set_alpha(255)

	gameDisplay.fill(system_blue)
	gameDisplay.blit(image,(20,20))
	pygame.display.flip()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

""" -------- """
def fetch_sprite(dataframe, index, gender_id, shiny):
	sprite_location = dataframe.loc[index, 'sprite_location']
	if dataframe.loc[index, 'has_gender_differences'] == 1:
		#if dataframe.loc[index,'gender'] == 'female':
		if gender_id == 2:
			sprite_location = sprite_location + 1

	if shiny == 1 and dataframe.loc[index,'generation_id'] == 1 and sprite_location > 46:
		sprite_location = sprite_location - 7

	x_location = int(sprite_location)%10
	y_location = int(sprite_location/10)
	sprite_x = (x_location-1) * 128 + x_location
	sprite_y = y_location * 128 + y_location+1

	spritesheet_filename = 'spritesheets/gen' + str(int(dataframe.loc[index,'generation_id']))

	if shiny:
		spritesheet_filename = spritesheet_filename + '_shiny.png'
	else:
		spritesheet_filename = spritesheet_filename + '_normal.png'

	display_sprite(spritesheet_filename, sprite_x, sprite_y)
