#!/usr/bin/env python3
# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
import functions as fc

#random.seed(123)

class Nature:
	def __init__(self, natureID):
		self.id, self.identifier, self.decreased_stat_id, self.increased_stat_id, self.hates_flavor_id, self.likes_flavor_id, self.game_index = data.data['natures'][int(natureID)]

	def __str__(self):
		return str(self.identifier)

class Player:
	def __init__(self, name, gender):
		self.name = name
		self.gender = Gender(gender)
		self.pc = []
		self.party = []

	def __str__(self):
		return str(self.name)

class Item:
	def __init__(self, id):
		''' pulls information from items.csv with id '''
		''' pulls information from item_categories.csv '''
		''' pulls information from items_names and item_flavor_text '''

		self.id, self.identifier, self.category_id, self.cost,fling_power, self.fling_effect_id = data.data['items'][int(id)]
		self.pocket_id, self.identifier = data.data['item_categories'][int(self.category_id)][1], data.data['item_categories'][int(self.category_id)][2]
		
		''' self.name, self.flavor_text, self.short_effect, and self.effect have to look for their translations and generations '''

		for line in data.data['item_names']:
			if line[0] == self.id and line[1] == languageID:
				self.name = line[2]
		
		for line in data.data['item_flavor_text']:
			if line[0] == self.id and line[1] == generationID and line[2] == languageID:
				self.flavor_text = line[2]

		for line in data.data['item_prose']:
			if line[0] == self.id and line[1] == languageID:
				self.short_effect = line[2]
				self.effect = line[3]

	def __str__(self):
		return str(self.name)

class Gender:
	def __init__(self, id):
		self.id, self.identifier = data.data['genders'][int(id)]

	def __str__(self):
		return str(self.identifier)

""" Peripheral classes, need to be addressed later 

class PC:
	def __init__(self):

""" 

class Encounter:
	def __init__(self, id): #, encounter_method_id):
		self.id = str(id)
		#self.encounter_method_id = str(encounter_method_id)
		for line in data.data['encounters']:
			if line[0] == self.id:
				self.location_area_id, self.encounter_slot_id, self.pokemon_id, self.min_level, self.max_level = line[2:]
		for line in data.data['encounter_slots']:
			if line[0] == self.encounter_slot_id: #and line[2] == self.encounter_method_id: 
				self.slot, self.rarity = line[3:]

class Location:
	def __init__(self, id):
		self.id = str(id)
		self.region_name = ""
		self.region_id = ""
		for line in data.data['locations']:
			if line[0] == self.id:
				self.region_id, self.identifier = line[1:]
		for line in data.data['region_names']:
			if line[0] == self.region_id and line[1] == languageID:
				self.region_name = line[2]
		for line in data.data['location_names']:
			if line[0] == self.id and line[1] == languageID:
				self.name, self.subtitle = line[2:]
