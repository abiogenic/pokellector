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

# random.seed(123)

def get(string):
	wd = os.path.abspath(__file__)
	wd = wd.rsplit("/", 1)[0]

	os.chdir(wd+"/csv/")

	base = os.path.basename(string+".csv")
	file = os.path.splitext(string)
	preindexed_results = pd.read_csv(open(base), index_col=0)
	os.chdir(wd)

	return(preindexed_results)

def query():
	pokemon_species = get('pokemon_species')
	del pokemon_species ['conquest_order']
	pokemon = get('pokemon')
	species = pokemon.join(pokemon_species, on='species_id', how='left', lsuffix='', rsuffix='_species')
	return(species)