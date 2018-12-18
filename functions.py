#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
import classes as cl
import time
import sys
import os

#random.seed(123)

def write(string):
	for l in string:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(0.01)
	rawInput = input()
	return(rawInput)

def addToParty(trainer, pokemon):
	"""
	After capturing or obtaining a Pokemon, check if party is full
	If party is full, append Pokemon to PC
	If else, append Pokemon to party
	Assign pokemon.ownerUUID to trainer.UUID
	"""

	party_is_full, empty_slot = trainer.party.find_empty_slot()

	if party_is_full == True:
		trainer.pc.append(pokemon)
		print("Full party. " + str(trainer.name) + " added " + str(pokemon.identifier) + " to the PC.")

	else:
		empty_slot = pokemon
		print(str(trainer.name) + " added " + str(pokemon.identifier) + " to the party.")
		
	pokemon.ownerUUID = trainer.UUID

def addToBag(trainer, item, quantity):
	"""
	After obtaining an item, check item category
	Check quantity in bag
	Sum quantity in bag and quantity to add
	Append to bag
	"""
		
	pokemon.ownerUUID = trainer.UUID

def attemptCatch(pokemon, attempts):
	rawInput = write("Would you like to try to catch this Pokémon? >> ")
	while attempts > 0:

		if 'n' in rawInput:
			time.sleep(1)
			os.system('clear')
			return(0, attempts)

		elif 'y' in rawInput:
			capture_rate = cl.Species(pokemon.id).capture_rate
			roll = random.randint(0,255)

			if roll < int(capture_rate):
				time.sleep(0.05)
				print("Caught!")
				time.sleep(1)
				#os.system('clear')
				attempts = attempts - 1
				return(1, attempts)
			else:
				time.sleep(0.05)
				print("Missed")
				time.sleep(1)
				attempts = attempts - 1
				rawInput = write("Would you like to try to again? >> ")
	return(0, attempts)

######## Pseduo-code

### Scene outline

# Enter Room

# Observe Room

# 	if observe:
# 		interact
# 		make a note

# 	if not observe:

# Leave Room