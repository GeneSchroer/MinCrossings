import math


#global minimum

"""
Class to hold the name of the node and its position in the list
"""
class Node:
	def __init__(self, number=-1, position=-1):
		self.number = number
		self.position = position
"""
an edge on the Graph, connects two Nodes, connects two layers
"""
class Edge:
	def __init__(self, low_node=-1, low_layer=-1, high_node=-1, high_layer=-1 ):
		self.low_node = low_node
		self.low_layer = low_layer
		self.high_node = high_node
		self.high_layer = high_layer

"""
Class that holds the matrix of Nodes (the graph) and the list of edges
"""
class Graph:
	def __init__(self, graph=None, edges=None):
		self.graph = graph
		self.edges = edges


"""
Fill the Graph with Nodes and Edges, using commands from the input file
"""
def fillGraph(codes = None):
	if codes == None:
		return []
	return_list = []
	graph = []
	edge_list = []
	total_nodes = 0
	# determine number of layers
	layers = codes[0].split("(")[1].split(")")[0]
	for i in range(0, int(layers)):
		graph.append([])
	#print(graph)
	index = 0
	for i in range(1,len(codes)):
		#split the command from its parameters
		if(codes[i] == []):
			continue
		command = codes[i].split("(")[0]		
		command_list = codes[i].split("(")[1]\
				.split(")")[0].split(",")
		if (command == "width"):
			layer = int(command_list[0])
			count = int(command_list[1])
			node = Node()
			for i in range(0, count):
				graph[layer].append(node)
			index = 0
		elif (command == "in_layer"):
			layer = int(command_list[0])
			number = int(command_list[1].split("n")[1])
			node = Node(number, index)
	#		print (node.number)
	#		print (node.position)
			graph[layer][index] = node
			index += 1
			total_nodes += 1
		elif (command == "edge"):
			low_node = int(command_list[0].split("n")[1])
			high_node = int(command_list[1].split("n")[1])
			low_layer = findLayer(graph, low_node)
			high_layer = findLayer(graph, high_node)
			edge = Edge(low_node, low_layer,\
					 high_node, high_layer)
			edge_list.append(edge)
	#edge_list = sortEdges(edge_list)
	#edge_list = groupEdges(edge_list, total_nodes)
	#printEdges(edge_list)
	#print(total_nodes)
	#for edge in edge_list:
	#	print (edge.low_node + " " + edge.high_node)
	ret = Graph(graph, edge_list)
	return ret

"""
Finds what layer in the graph a node is in.
"""
def findLayer(graph = None, node = -1):
	if (graph == None or node == -1):
		return -1
	for i in range(0, len(graph)):
		for layer in graph[i]:
			if (layer.number == node):
				return i
	return -1 

def getPosition(graph, layer = -1,   node = -1):
	if (layer == -1 or node == None):
		return None
	layer_list = graph[layer]
	lo = 0
	hi = len(layer_list)-1

	while (hi>lo):
		lo = 0
		hi = len(layer_list)-1
		mid = math.floor( (hi-lo)/2)
		#print(mid)
		if (layer_list[mid].number == node):
			return layer_list[mid].position
		elif(layer_list[mid].number < node):
			layer_list = layer_list[mid+1:len(layer_list)]
		else:
			layer_list = layer_list[0:mid]
	return -1

def binarySearch(array, hi, lo):
	if (hi < lo):
		return -1
	mid = math.ceil( (hi-lo)/2)
#	if (array[mid].number

def computeMinimum(g = Graph(), current_min = 4096):

	graph = g.graph
	edge_list = g.edges
	crossings = 0
	# access a group of edges
	# select an edge from that group
	# select an edge from another group
	# compare with the edge of another group

	for i in range(0, len(edge_list)):
		if(len(edge_list[i]) != 0):
			for edge in edge_list[i]:
				for j in range(i, len(edge_list)):
					for target in edge_list[j]:
						if (edge.low_layer !=\
					    	target.low_layer):	
							break
						target_high\
						 = getPosition(graph,\
						   target.high_layer,\
						   target.high_node)
						edge_high\
						 = getPosition(graph,\
						   edge.high_layer,\
						   edge.high_node)
						if(edge_high\
							 > target_high):
							crossings += 1
			
	return crossings

"""
Add all the edges to the Graph and return the number of crossings

Return: The minimum number of crossings
"""
def compute(g = Graph()):
	crossings = 0
	edges = g.edges
	graph = g.graph
	edge_list = []	
	for current in edges:
		for i in edge_list:
			if(current.low_layer == i.low_layer):
				current_high = getPosition(graph, \
						current.high_layer, \
						current.high_node)
		#		print (current.high_layer)
		#		print (current.high_node)
				#print(current_high)	
				current_low = getPosition(graph, \
						current.low_layer, \
						current.low_node)
				#print(current_low)
				i_high = getPosition(graph, \
						i.high_layer, \
						i.high_node)
				#print(i_high)
				i_low = getPosition(graph, \
						i.low_layer,
						i.low_node)
				#print(i_low)
				if( (current_high > i_high \
				    and current_low < i_low)\
				    or \
				    (current_high < i_high \
				    and current_low > i_low)):
					crossings+= 1
		edge_list.append(current)
		

	return crossings
def swap(array = None, left = -1, right = -1):
	if (array ==None or left == -1 or right == -1):
		return array
	temp = array[left].position
	array[left].position = array[right].position
	array[right].position = temp
	return array
def permWrapper(g = Graph()):
	return permutate(g, 0, 400000)

def permutate(g=Graph(), layer=-1, minimum = 400000):
	if(layer == -1):
		return None
	graph = g.graph
	edges = g.edges
	layer_list = graph[layer] # list of the current layer
	top_level = len(graph)-1
	count = len(layer_list)
	i = 0	
	j = count - 1
	if (layer == top_level):
		# begin computing
		for k in range(0, math.factorial(count)):
			crossings = compute(g)
			if(crossings < minimum):
				#printGraph(graph)
				minimum = crossings
				print(minimum)
			#swap nodes in the list
			layer_list = swap(layer_list, i, j)
			#also swap edges?
			g.graph[layer] = layer_list
			i = (i + 1) % count	
			j = (j + 1) % count
	else:
		for k in range(0, math.factorial(count)):
			crossings = permutate(g, layer+1, minimum)
			if (crossings < minimum):
				minimum = crossings
			layer_list = swap(layer_list, i, j)
			g.graph[layer] = layer_list
			i = (i + 1) % count
			j = (j + 1) % count
	return minimum

"""
Parse file into Nodes, Edges, and a Graph
"""
def parseFile(stream = None):
	statement_list = stream.read().split(".\n")
	statement_list = statement_list[0:len(statement_list) -1]
	return statement_list 

def groupEdges(edge_list=[], nodes = 0):
	edge_groups = []
	for i in range(0, nodes):
		edge_groups.append([])
	for edge in edge_list:
		edge_number = int(edge.low_node.split("n")[1])
		index = edge_number - 1
		edge_groups[index].append(edge)	
	return edge_groups


def fillGraph(codes = None):
	if codes == None:
		return []
	return_list = []
	graph = []
	edge_list = []
	total_nodes = 0
	layers = codes[0].split("(")[1].split(")")[0]
	for i in range(0, int(layers)):
		graph.append([])
	#print(graph)
	index = 0
	for i in range(1,len(codes)):
		command = codes[i].split("(")[0]		
		command_list = codes[i].split("(")[1]\
				.split(")")[0].split(",")

		if (command == "width"):
			layer = int(command_list[0])
			count = int(command_list[1])
			node = Node()
			for i in range(0, count):
				graph[layer].append(node)
			index = 0
		elif (command == "in_layer"):
			layer = int(command_list[0])
			node = Node(command_list[1], index)
	#		print (node.number)
	#		print (node.position)
			graph[layer][index] = node
			index += 1
			total_nodes += 1
		elif (command == "edge"):
			low_node = command_list[0]
			high_node = command_list[1]
			low_layer = findLayer(graph, low_node)
			high_layer = findLayer(graph, high_node)
			edge = Edge(low_node, low_layer,\
					 high_node, high_layer)
			edge_list.append(edge)
	#edge_list = sortEdges(edge_list)
	#edge_list = groupEdges(edge_list, total_nodes)
	#printEdges(edge_list)
	#print(total_nodes)
	#for edge in edge_list:
	#	print (edge.low_node + " " + edge.high_node)
	ret = Graph(graph, edge_list)
	return ret
	
def sortEdges(edge_list=[], nodes = 0):
	if(edge_list ==[]):
		return edge_list
	lo = 0
	hi = len(edge_list) -1
	edge_list = mergeSortEdges(edge_list, lo, hi)
	return edge_list
def mergeSortEdges(edge_list=[], lo=-1, hi=-1):
	ret = edge_list
	lo = 0
	hi = len(edge_list)-1
	if (lo < hi):
		mid = math.floor((lo + hi) / 2)
		list1 = mergeSortEdges(edge_list[0:mid+1])
		list2 = mergeSortEdges(edge_list[mid+1: hi+1])
		ret = merge(list1, list2)
#	for r in ret:
	#	print(r.low_node)
#	print()
	return ret
def merge(list1, list2):
	new_list = []
	while(list1 != [] or list2 != []):
		if (list1 == []):
			new_list.append(list2.pop(0))
		elif(list2 == []):	
			new_list.append(list1.pop(0))
		else:
			num1 = int(list1[0].low_node.split("n")[1])	
			num2 = int(list2[0].low_node.split("n")[1])
	
			if(num1 <= num2):
				new_list.append(list1.pop(0))
			else:
				new_list.append(list2.pop(0))
#	for new in new_list:
#		print(new.low_node)
#	print ("")
	return new_list



def printEdges(edge_list = []):
	for i in range(0, len(edge_list)):
		for edge in edge_list[i]:
			print(edge.low_node)
		print()


