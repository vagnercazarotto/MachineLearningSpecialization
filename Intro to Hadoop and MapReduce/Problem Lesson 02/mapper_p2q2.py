#!/usr/bin/python
"""
Write a MapReduce program which determines the number of hits to the site made by each
different IP address.
How many hits were made by the IP address 10.99.99.186?
"""

import sys


for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) > 1:
		ip = data[0]
		print "{0}\t{1}".format(ip,1)
