#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data

#random.seed(123)

generationID = '18'

class Species:
	def __init__(self,id):
		self.id, self.identifier, self.generation_id, self.evolves_from_species_id, self.evolution_chain_id, self.color_id, self.shape_id, self.habitat_id, self.gender_rate, self.capture_rate, self.base_happiness, self.is_baby, self.hatch_counter, self.has_gender_differences, self.growth_rate_id, self.forms_switchable, self.order, self.conquest_order = data.data['pokemon_species'][id]
		self.species_id, self.height, self.weight, self.base_experience, self.order, self.is_default = data.data['pokemon'][int(id)][2:]
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
		self.nature = Nature(random.randint(0,25))
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


""" Peripheral classes, need to be addressed later 

class Trainer(object):
	def __init__(self, name, gender, party=[], pc=[]):
		self.name = name.capitalize()
		self.UUID = uuid.uuid4()
		self.gender = gender
		self.party = party
		self.pc = pc

	def addToParty(self, member):
		if len(self.party) >= 6:
			self.pc.append(member)
			print("Full party. " + str(self.name) + " added " + str(member.name) + " to the PC.")
			member.ownerUUID = self.UUID
			
		elif len(self.party) >= 0:
			self.party.append(member)
			print(str(self.name) + " added " + str(member.name) + " to the party.")
			member.ownerUUID = self.UUID

class Location(object):
	def __init__(self, name, wildpokemon, trainers):
		self.name = 
		self.wildpokemon = 
		self.trainers = 

""" 

