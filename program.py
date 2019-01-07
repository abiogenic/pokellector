#!/usr/bin/env python3
# coding: utf-8

### Import modules
import random as rand
import uuid
import time
import sys
import os
import glob
import pandas as pd
import pygame

### Import related scripts
import data
import cookbook

os.system('clear')

""" Set random seed if desired.
	When set to any integer, this allows for debugging by making sure random events are generated from this seed.
	Comment this out for different random events each run.										
"""

# random.seed(123)

""" When this script is run it needs two additional arguments, the query and the form_id.
	For example, to query Mew, type:
		$ python program.py pokemon_species 151 
		$ python program.py moves 4														
"""

if __name__ == "__main__":
	species_id = int(sys.argv[1])
	gender_id = int(sys.argv[2])
	shiny = int(sys.argv[3])
	species_df = data.get('species')
	print("Pokémon: " + str(species_df.loc[species_id, 'identifier']).capitalize())
	print("Sprite: " + str(int(species_df.loc[species_id, 'sprite_location'])))
	if gender_id == 2:
		print("Gender: female")
	elif gender_id == 1:
		print("Gender: male")
	else:
		print("Gender: unknown")
	print("Shiny: " + str(shiny).lower())
	
	cookbook.fetch_sprite(species_df, species_id, gender_id, shiny)


