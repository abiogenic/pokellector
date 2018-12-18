#!/usr/bin/env python3

from __future__ import absolute_import
from __future__ import print_function
import random
import os
import glob

#random.seed(123)

### Load functions

def readCSV(csvFile):
	data = []
	for line in csvFile:
		# split each line into a list of items.
		line = line.rstrip()
		items = line.split(',')
		# append this list of items to a variables called "data"
		data.append(items)
	return(data)

wd = os.path.abspath(__file__)
wd = wd.rsplit("/", 1)[0]
wd_csv = wd+"/csv/"

os.chdir(wd_csv)

data = {}

for csv in glob.glob(os.path.join("*.csv")):
	base = os.path.basename(csv)
	file = os.path.splitext(base)[0]
	csv = readCSV(open(base))
	data[str(file)] = csv

os.chdir(wd)

