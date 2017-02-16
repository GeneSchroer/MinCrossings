import math
import sys
from util2 import *


# Open file
minimum = 4096

if(len(sys.argv) != 2):
	print("Usage: python3 hw2.py FILE")
else:
	stream = open(sys.argv[1], "r")
	# Parse file into a list
	
	graph_codes = parseFile(stream)

	ret = fillGraph(graph_codes)
	graph = ret.graph
	edges = ret.edges


	minimum = permWrapper(ret)
	print (minimum)
# Use that list to fill a graph

#print (files)

# Initialize the minimum number of crossings 
# to some arbitrarily high number



# For each permutation


# Compute the minimum number of crossings for that permutation
# (Optionally, update the min number)










