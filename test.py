#!/usr/bin/env python3
# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
#import classes as cl
import functions as fc
#import pokemon as pk
import sys
import time
import os
import inspect
import pprint

# initialize list of all Pokémon 
pokemon = {}

random.seed(1234)

# Player is a player object with a name and a gender
# Attempts represents a single-use catch item

# nameInput = input("Name >> ").lower()
# genderInput = input("Gender >> ")

# if 'f' in genderInput:
# 	gender = 1
# elif 'm' in genderInput:
# 	gender = 2
# else:
# 	gender = 3

nameInput = "Caroline"
gender = 1

player = cl.Player(nameInput, gender)
attempts = 10

###############
#CRITERIA FOR ENCOUNTERED POKEMON
###############

os.system('clear')

colors = []
while len(colors) < 4:
	pokemon, key1 = fc.encounterPokemon(pokemon,100,50,'fish')
	color = pk.Species(pokemon[key1].id).color
	if color not in colors:
		colors.append(color)
print(colors)


print(pk.Species(63))