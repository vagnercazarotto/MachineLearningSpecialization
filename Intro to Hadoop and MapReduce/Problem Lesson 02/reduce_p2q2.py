#!/usr/bin/python

import sys

countTotal = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# if something go worng, just ignore
		continue

	thisKey , thisCount = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", countTotal
		oldKey = thisKey
		countTotal = 0

	oldKey = thisKey
	countTotal += int(thisCount)

if oldKey != None:
	print oldKey, "\t", countTotal


