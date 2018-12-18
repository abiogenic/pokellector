#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
import classes as cl
import functions as fc
import sys
import time
import os


#random.seed(123)

os.system('clear')

# Player is a trainer object with a name and a gender
# Attempts represents a single-use catch item

nameInput = input("Name >> ").lower()
genderInput = input("Gender >> ")

if 'f' in genderInput:
	gender = 1
elif 'm' in genderInput:
	gender = 2
else:
	gender = 3

player = cl.Trainer(nameInput, gender)
attempts = 4

items = []
for i in range(0,20):
	randID = random.randint(1,100)
	items.append(cl.Item(randID))

for i in items:
	print(i.name)
	print(i.flavor_text)
	print(i.effect)

# All pokemon objects go in a dictionary called pokemon
# Each key of this dictionary is the UUID number of the individual
# Each pokemon object has its own stats, nature, and ability (tba) objects

os.system('clear')

pokemon = {}
for i in range(0,10):
	key = uuid.uuid1()
	level = random.randint(5,15)
	while True:
		randID = random.randint(1,151)
		species = cl.Species(randID)
		if species.growth_rate_id == '2' or species.growth_rate_id == '1':
			if species.evolves_from_species_id == '':
				if species.is_baby == '0':
					break
	entry = cl.Pokemon(key, randID, level)
	pokemon[key] = entry
	entry.stats = cl.Stats(key, pokemon[key].id, pokemon[key].level, pokemon[key].nature)

# For each pokemon in the pokemon dictionary, ask if user wants to attempt to catch it
for i in pokemon.keys():
	while attempts > 0:
		os.system('clear')
		print(str(pokemon[i]))
		print(str(pokemon[i].gender).capitalize())
		print("")
		time.sleep(1)
		catch, attempts = fc.attemptCatch(pokemon[i], attempts)
		if catch == 1:
			fc.addToParty(player, pokemon[i])
		time.sleep(1)

for i in player.party:
	print(i)

#print([str(i) for i in items])
	
