#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
import random
import uuid
import data
import classes as cl
import functions as fc

#random.seed(123)

### CLUMSY LOOP TO GENERATE A STARTER POKEMON'S SPECIES WITH THE FOLLOWING:
# NOT A BABY
# NOT AN EVOLVED FORM
# GROWTH RATE 2 (MEDIUM)

while True:
	species = cl.Species(random.randint(1,807))
	if species.growth_rate_id == '2':
		if species.evolves_from_species_id == '':
			if species.is_baby == '0':
				break

print(species)
print(str(species.height) + " m")
print(str(species.weight) + " kg")
#print(species.base)

