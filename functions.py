#!/usr/bin/env python3
# coding: utf-8

# from __future__ import absolute_import
# from __future__ import print_function
import random
import uuid
import data
#import classes as cl
#import pokemon as pk
import time
import sys
import os

#random.seed(123)

def type(string):
	for l in string:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(0.01)

def ask(string):
	for l in string:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(0.01)
	rawInput = input()
	return(rawInput)

#### Preprocessing for classes

def findEncounterIDs():
	encounter_id_list = []
	for line in data.data['encounters']:
		encounter_id_list.append(line[0])
	encounter_id_list.remove('id')
	return(encounter_id_list)

def findLocationIDs():
	location_id_list = []
	for line in data.data['locations']:
		location_id_list.append(line[0])
	location_id_list.remove('id')
	return(location_id_list)

def generateGender(id):
	gender_rate = data.data['pokemon_species'][int(id)][8]
	if int(gender_rate) < 0:
		gender = '3'
	else:
		gender = random.uniform(0,1)
		if gender > int(gender_rate)/8:
			gender = '2'
		else:
			gender = '1'
	return(gender)

###############
#ENCOUNTER RANDOM POKEMON
###############

def encounterPokemon(pokemon_dictionary,var_rarity,var_max_level,var_shape):

	# find all encounter ids
	encounter_id_list = findEncounterIDs()

	def criteria1():
		return(rarity < var_rarity)
	def criteria2():
		return(max_level < var_max_level)
	def criteria3():
		return(shape == var_shape)
	#def criteria4():
	#	return(color == var_color)

	# while pokemon not found to meet criteria
	found = False
	while found == False:
		encounter = cl.Encounter(random.choice(encounter_id_list)) # randomly generate from encounter list
		location = cl.Location(encounter.location_area_id) # pull encounter's location information
		if location.region_id is not "":
			rarity = int(encounter.rarity)
			max_level = int(encounter.max_level)
			shape = pk.Species(encounter.pokemon_id).shape
			color = pk.Species(encounter.pokemon_id).color
			if criteria3(): # if encounter meets criteria
				if criteria2(): # if encounter meets criteria
					if criteria3(): # if encounter meets criteria
						#if criteria4(): # if encounter meets criteria
						key = uuid.uuid1() # encounter pokemon
						encountered_pokemon = pk.Pokemon(key, encounter.pokemon_id, random.randint(int(encounter.min_level), int(encounter.max_level)), encounter.location_area_id)
						pokemon_dictionary[key] = encountered_pokemon
						found = True

	#os.system('clear')
	print(str(pokemon_dictionary[key]))
	print(pk.Species(pokemon_dictionary[key].id).color)
	
	print(str(pokemon_dictionary[key].gender).capitalize())
	if pokemon_dictionary[key].location.region_name == "":
		print("From " + pokemon_dictionary[key].location.name + ".") 
	else:
		print("From " + pokemon_dictionary[key].location.name + " in the " + pokemon_dictionary[key].location.region_name + " region.")
	print("")

	return(pokemon_dictionary,key)

#### Gameplay: Classes interact

def addToBag(trainer, item, quantity):
	pass