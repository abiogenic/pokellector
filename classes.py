#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
import functions as fc

#random.seed(123)

generationID = '18'
languageID = '9'

class Species:
	def __init__(self,id):
		self.id, self.identifier, self.generation_id, self.evolves_from_species_id, self.evolution_chain_id, self.color_id, self.shape_id, self.habitat_id, self.gender_rate, self.capture_rate, self.base_happiness, self.is_baby, self.hatch_counter, self.has_gender_differences, self.growth_rate_id, self.forms_switchable, self.order, self.conquest_order = data.data['pokemon_species'][int(id)]
		self.species_id, self.height, self.weight, self.base_experience, self.order, self.is_default = data.data['pokemon'][int(id)][2:]
		
		### Fetch variables from IDs
		self.color = data.data['pokemon_colors'][int(self.color_id)][1]
		self.shape = data.data['pokemon_shapes'][int(self.shape_id)][1]
		
		### Adjust measurements to human readable format
		self.height = int(self.height)/10
		self.weight = int(self.weight)/10

		self.base = self.Base(self.id)
		self.effort = self.Effort(self.id)

		movesetlist = []
		for line in data.data['pokemon_moves']:
			if line[0] == self.id and line[1] == generationID:
				movesetlist.append(line)
		self.moveset = movesetlist

	class Base:
		def __init__(self,id):
			baselist = []
			for line in data.data['pokemon_stats']:
				if line[0] == id:
					baselist.append(int(line[2]))
			self.hp, self.attack, self.defense, self.spattack, self.spdefense, self.speed = baselist

		def __str__(self):
			return str(self.hp) + "/" + str(self.attack) + "/" + str(self.defense) + "/" + str(self.spattack) + "/" + str(self.spdefense) + "/" + str(self.speed)

	class Effort:
		def __init__(self,id):
			effortlist = []
			for line in data.data['pokemon_stats']:
				if line[0] == id:
					effortlist.append(line[3])
			self.hp, self.attack, self.defense, self.spattack, self.spdefense, self.speed = effortlist

	def __str__(self):
		return str(self.identifier).capitalize() + ", Number " + str(self.id)

class Pokemon:
	def __init__(self,key,id,level):
		self.id, self.identifier, self.species_id, self.height, self.weight, self.base_experience, self.order, self.is_default = data.data['pokemon'][int(id)]
		self.level = level
		#self.ability = Ability()
		self.nature = Nature(random.randint(1,25))
		gender_rate = data.data['pokemon_species'][int(self.species_id)][8]
		if int(gender_rate) < 0:
			gender = '3'
		else:
			gender = random.uniform(0,1)
			if gender > int(gender_rate)/8:
				gender = '2'
			else:
				gender = '1'
		self.gender = Gender(gender)
		self.stats = ""
		self.nickname = ""
		self.ownerUUID = ""

	def __str__(self):
		return str(self.identifier).capitalize() + ", Level " + str(self.level)

class Stats:
	def __init__(self,key,id,level,nature):
		self.id = id
		self.IVs = self.IVs([random.randint(0,31) for i in range(0,6)])
		self.EVs = self.EVs([0 for i in range(0,6)])
		self.base = Species.Base(id)
		self.computed = self.Computed(key,self.IVs,self.EVs,self.base,level,nature)
		self.battle = self.Battle(self.computed)

	class IVs:
		def __init__(self, IVs):
			self.hp, self.attack, self.defense, self.spattack, self.spdefense, self.speed = IVs
		
		def __str__(self):
			return str(self.hp) + "/" + str(self.attack) + "/" + str(self.defense) + "/" + str(self.spattack) + "/" + str(self.spdefense) + "/" + str(self.speed)

	class EVs:
		def __init__(self, EVs):
			self.hp, self.attack, self.defense, self.spattack, self.spdefense, self.speed = EVs
		
		def __str__(self):
			return str(self.hp) + "/" + str(self.attack) + "/" + str(self.defense) + "/" + str(self.spattack) + "/" + str(self.spdefense) + "/" + str(self.speed)

	class Computed:
		def __init__(self,key,IVs,EVs,base,level,nature):
			self.hp = int(10 + level + (((2*base.hp+IVs.hp+(EVs.hp/4))*level)/100))
			self.attack = int(5 + (((2*base.attack+IVs.attack+(EVs.attack/4))*level)/100))
			self.defense = int(5 + (((2*base.defense+IVs.defense+(EVs.defense/4))*level)/100))
			self.spattack = int(5 + (((2*base.spattack+IVs.spattack+(EVs.spattack/4))*level)/100))
			self.spdefense = int(5 + (((2*base.spdefense+IVs.spdefense+(EVs.spdefense/4))*level)/100))
			self.speed = int(5 + (((2*base.speed+IVs.speed+(EVs.speed/4))*level)/100))
			
		def __str__(self):
			return str(self.hp) + "/" + str(self.attack) + "/" + str(self.defense) + "/" + str(self.spattack) + "/" + str(self.spdefense) + "/" + str(self.speed)
			
	class Battle:
		def __init__(self,computed):
			self.hp, self.attack, self.defense, self.spattack, self.spdefense, self.speed = computed.hp, computed.attack, computed.defense, computed.spattack, computed.spdefense, computed.speed
			self.accuracy, self.evasion = 0,0
		
		def __str__(self):
			return str(self.hp) + "/" + str(self.attack) + "/" + str(self.defense) + "/" + str(self.spattack) + "/" + str(self.spdefense) + "/" + str(self.speed) +  "/" + str(self.accuracy) + "/" + str(self.evasion)
			
class Move:
	def __init__(self, moveID):
		self.id, self.identifier, self.generation_id, self.type_id, self.power, self.pp, self.accuracy, self.priority, self.target_id, self.damage_class_id, self.effect_id, self.effect_chance, self.contest_type_id, self.contest_effect_id, self.super_contest_effect_id = data.data['moves'][int(moveID)]

	def __str__(self):
		return str(self.identifier)

class Nature:
	def __init__(self, natureID):
		self.id, self.identifier, self.decreased_stat_id, self.increased_stat_id, self.hates_flavor_id, self.likes_flavor_id, self.game_index = data.data['natures'][int(natureID)]

	def __str__(self):
		return str(self.identifier)

class Trainer:
	def __init__(self, name, gender):
		self.name = name.capitalize()
		self.UUID = uuid.uuid4()
		self.gender = Gender(gender)
		self.pc = []
		self.party = Party(self.UUID)

	def __str__(self):
		return str(self.name)

class Party:
	def __init__(self, ownerUUID):
		self.ownerUUID = ownerUUID
		self._1 = []
		self._2 = []
		self._3 = []
		self._4 = []
		self._5 = []
		self._6 = []

	def find_empty_slot(self):
		party_is_full = False
		
		if trainer.party._1 == 1:
			if trainer.party._2 == 1:
				if trainer.party._3 == 1:
					if trainer.party._4 == 1:
						if trainer.party._5 == 1:
							if trainer.party._6 == 1:
								party_is_full = True
								empty_slot = ""
							else:
								empty_slot = trainer.party._6
						else:
							empty_slot = trainer.party._5
					else:
						empty_slot = trainer.party._4
				else:
					empty_slot = trainer.party._3
			else:
				empty_slot = trainer.party._2
		else:
			empty_slot = trainer.party._1
			
		return(party_is_full, empty_slot)

	def __str__(self):
		return str(self._1) + "/" + str(self._2) + "/" + str(self._3) + "/" + str(self._4) + "/" + str(self._5) + "/" + str(self._6)

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

class Location:
	# Add trainers to location
	def __init__(self, name, wildpokemon):
		self.name = name
		self.wildpokemon = wildpokemon