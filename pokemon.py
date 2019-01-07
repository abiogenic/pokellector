#!/usr/bin/env python3
# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
import functions as fc
import classes as cl

generationID = '18'
languageID = '9'

class Species:
	def __init__(self,form_id):
		for line in data.data['pokemon']:
			if line[0] == str(form_id): 
				self.form_id, self.form_identifier, self.species_id, self.height, self.weight, self.base_experience, self.order, self.is_default = line

		for line in data.data['pokemon_species']:
			if line[0] == self.species_id:
				self.species_id, self.species_identifier, self.generation_id, self.evolves_from_species_id, self.evolution_chain_id, self.color_id, self.shape_id, self.habitat_id, self.gender_rate, self.capture_rate, self.base_happiness, self.is_baby, self.hatch_counter, self.has_gender_differences, self.growth_rate_id, self.forms_switchable, self.order, self.conquest_order = line

		""" Look for special species and genus names """

		self.species_name = ""
		self.genus_name = ""

		for line in data.data['pokemon_species_names']:
			if line[0] == self.form_id and line[1] == languageID:
				self.species_name, self.genus_name = line[2:]

		""" Look for special names """

		self.form_name = ""
		self.pokemon_name = self.form_identifier

		for line in data.data['pokemon_form_names']:
			if line[0] == self.form_id and line[1] == languageID:
				self.form_name, self.pokemon_name = line[2:]

		### Fetch variables from IDs
		self.color = data.data['pokemon_colors'][int(self.color_id)][1]
		self.shape = data.data['pokemon_shapes'][int(self.shape_id)][1]
		
		### Adjust measurements to human readable format
		self.height = int(self.height)/10
		self.weight = int(self.weight)/10

	def __str__(self):
		return str([self.__dict__])

class Pokemon:
	def __init__(self,key,id,level,location_area_id):
		for line in data.data['pokemon']:
			if line[0] == str(id):
				self.id, self.identifier, self.species_id, self.height, self.weight, self.base_experience, self.order, self.is_default = line
		self.level = level
		#self.ability = Ability()
		self.nature = cl.Nature(random.randint(1,25))
		gender = fc.generateGender(self.species_id)
		self.gender = cl.Gender(gender)
		self.nickname = ""
		self.species_name = ""
		self.genus_name = ""
		for line in data.data['pokemon_species_names']:
			if line[0] == self.id and line[1] == languageID:
				self.species_name, self.genus_name = line[2:]
		self.location = cl.Location(location_area_id)


	def __str__(self):
		return str(self.species_name).capitalize() + ", Level " + str(self.level)
		#return str(self.__dict__.keys())