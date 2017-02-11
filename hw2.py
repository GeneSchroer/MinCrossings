import math

"""
l
"""
class Node:
	def __init__(self, number=None):
		self.num = number
	def setNum(number):
		self.num = number
"""
an edge on the Graph, connects two Nodes
"""
class Edge:
	def __init__(self, low_node=None, low_layer=0, high_node=None, high_layer=0 ):
		self.low_node = low_node
		self.low_layer = low_layer
		self.high_node = high_node
		self.high_layer = high_layer

class Graph:
	def __init__(self, graph=None, edges=None):
		self.graph = graph
		self.edges = edges


def findLayer(graph = None, node = None):
	if (graph == None or node == None):
		return None
	for i in range(0, len(graph)):
		for layer in graph[i]:
			if (layer == node):
				return i
	return 0 

def getPosition(graph=None, layer = None, node = None):
	if (graph ==None or layer ==None or node == None):
		return None
	for i in range(0, len(graph[layer])):
		if graph[layer][i] == node:
			return i
	return -1

"""
Add all the edges to the Graph and return the number of crossings
"""
def compute(g = Graph()):
	crossings = 0
	edges = g.edges
	graph = g.graph
	edge_list = []
	
	for current in edges:
		for i in edge_list:
			if(current.low_layer == i.low_layer \
				and current.high_layer == i.high_layer):
				current_high = getPosition(graph, \
						current.high_layer, \
						current.high_node)	
				current_low = getPosition(graph, \
						current.low_layer, \
						current.low_node)
				i_high = getPosition(graph, \
						i.high_layer, \
						i.high_node)
				i_low = getPosition(graph, \
						i.low_layer,
						i.low_node)
				if( (current_high > i_high \
				    and current_low < i_low)\
				    or \
				    (current_high < i_high \
				    and current_low > i_low)):
					crossings+= 1
		edge_list.append(current)
		

	return crossings

def permutate(raph=Graph(), layer):
	minimum = 4096
	graph = raph.graph
	edges = raph.edges
	if (layer = len(graph)):
		for i in range(0, math.factorial(len(graph[layer]))):
			permutation = compute(
			crossings = computer(


	permutation = Graph(graph, edges)

	perm_crossings = compute(permutation); 	
	if (perm_crossings < minimum):
		minimum = perm_crossings

	return minimum

"""
Parse file into Nodes, Edges, and a Graph
"""
def parseFile(stream = None):
	statement_list = stream.read().split(".\n")
	statement_list = statement_list[0:len(statement_list) -1]
	return statement_list 

def fillGraph(codes = None):
	if codes == None:
		return []
	return_list = []
	graph = []
	edge_list = []
	layers = codes[0].split("(")[1].split(")")[0]
	for i in range(0, int(layers)):
		graph.append([])
	print(graph)
	index = 0
	for i in range(1,len(codes)):
		command = codes[i].split("(")[0]		
		command_list = codes[i].split("(")[1]\
				.split(")")[0].split(",")

		if (command == "width"):
			layer = int(command_list[0])
			count = int(command_list[1])
			for i in range(0, count):
				graph[layer].append("")
			index = 0
		elif (command == "in_layer"):
			layer = int(command_list[0])
			node = command_list[1]
			graph[layer][index] = node
			index += 1
		elif (command == "edge"):
			low_node = command_list[0]
			high_node = command_list[1]
			low_layer = findLayer(graph, low_node)
			high_layer = findLayer(graph, high_node)
			edge = Edge(low_node, low_layer,\
					 high_node, high_layer)
			edge_list.append(edge)

	ret = Graph(graph, edge_list)
	return ret
	#	elif command == "in_layer":
			
        	#type = codes[i].split("(")[1].split(")")[0].split(",")
        #	print (width)

# Open file
stream = open("test.txt", "r")

# Parse file into a list

graph_codes = parseFile(stream)

ret = fillGraph(graph_codes)
graph = ret.graph
edges = ret.edges

#print (graph)
#print (edges)

minimum = permutate(ret,0)
print (minimum)
# Use that list to fill a graph

#print (files)

# Initialize the minimum number of crossings 
# to some arbitrarily high number

min_crossing = 4096


# For each permutation


# Compute the minimum number of crossings for that permutation
# (Optionally, update the min number)










