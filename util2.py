import itertools
import math
import collections

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


def permWrapper(g=Graph()):
	permutate(g, 400000)

def permutate(g=Graph(), minimum = 4000):
	crossings = 0
	graph = g.graph
	edges = g.edges
	#for edge in edges:
	#	print(str(edge.low_node) + " " + str(edge.high_node))
	permutation_list= []
	for layer in graph:
	#	print(layer)
		p = list(itertools.permutations(layer))
	#	print(list(p))
		permutation_list.append( p)

#	print((permutation_list))
		
	permutated_graph = list(itertools.product(*permutation_list))
	permutated_graph = upgradeGraph(permutated_graph)
	for perm in permutated_graph:
		crossings = compute(perm, edges)
		if (crossings < minimum):
			minimum = crossings
			print (perm)
			print (minimum)

			

#	print("2 " + str(permutated_graph[2][0]))
	#print (permutated_graph[2][0].keys())


#	print((permutated_graph))
def upgradeGraph(permutated_graph):
	for i in range(0, len(permutated_graph)):	
		perm = list(permutated_graph[i])
		for j in range(0, len(perm)):
			perm[j] = list(perm[j])
			#perm[j] = collections.\
			#	OrderedDict( (l,-1) for l in\
			#	 list(perm[j]) )
			#index = 0
			#for k in perm[j]:
			#	k = index
			#	index += 1
		permutated_graph[i] = perm
	#	permutated_graph[i] = dict( (j,k) for j in range(0, len(perm)) for k in perm)
	print(permutated_graph[0])
#	print(permutated_graph[0][0][1])
	#print(permutated_graph[0])
	#crossings = compute(graph, edge)
	#if (crossings < minimum):
	#	minimum = crossings
	#	print(minimum)
	return permutated_graph
def groupEdges(edge_list = []):
	grouped_edges = {}
	current = -1
	for edge in edge_list:
		n = edge.low_node
		if (n != current):
			grouped_edges[n] = []
			grouped_edges[n].append(edge)
			current = n
		else:
			grouped_edges[n].append(edge)

#	for edge in grouped_edges:
#		for e in grouped_edges[edge]:
#			print(e.low_node)
#		print()
	return grouped_edges
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
	total_nodes = 0
	index=0
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
		#	node = Node()
			for i in range(0, count):
				graph[layer].append(-1)
			
			index = 0
		elif (command == "in_layer"):
			layer = int(command_list[0])
			node = int(command_list[1].split("n")[1])
	#		print (node.number)
	#		print (node.position)
			graph[layer][index] = node
			#print(graph[layer].keys())
			index += 1
		elif (command == "edge"):
			low_node = int(command_list[0].split("n")[1])
			high_node = int(command_list[1].split("n")[1])
			low_layer = findLayer(graph, low_node)
			high_layer = findLayer(graph, high_node)
			edge = Edge(low_node, low_layer,\
					 high_node, high_layer)
			edge_list.append(edge)
	edge_list = sortEdges(edge_list)
	edge_list = groupEdges(edge_list)
	#printEdges(edge_list)
	#print(total_nodes)
	#for edge in edge_list:
	#	print (edge.low_node + " " + edge.high_node)
	ret = Graph(graph, edge_list)
	#print(ret.edges)
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
		elif(list1[0].low_node <= list2[0].low_node):
			new_list.append(list1.pop(0))
		else:
			new_list.append(list2.pop(0))
#	for new in new_list:
#		print(new.low_node)
#	print ("")
	return new_list


"""
Finds what layer in the graph a node is in.
"""
def findLayer(graph = None, node = -1):
	if (graph == None or node == -1):
		return -1
	for i in range(0, len(graph)):
		for layer in graph[i]:
			if (layer == node):
				return i
	return -1 

"""
Add all the edges to the Graph and return the number of crossings

Return: The minimum number of crossings
"""
def compute(graph, edges):
	#print(edges)
	crossings = 0
	for i in range (0, len(graph)-1):
		for j in range(0,len(graph[i])):
			current_node = graph[i][j]
			if (current_node not in edges):
				continue
			else:
				current_edges = edges[current_node]
				#print (edges)
				for k in range(j+1, len(graph[i])):
					trav_node = graph[i][k]
					if (trav_node not in edges):
						continue
					else:
						trav_edges = edges[trav_node]
						crossings += getCrossings\
						(graph, current_edges,\
						 trav_edges)
	return crossings
def getCrossings(graph, n, m):
	crossings = 0
	for cur in n:
		for trav in m:
			cur_pos = getPosition1(graph, \
						cur.high_layer,cur.high_node)
			trav_pos = getPosition1(graph, \
						trav.high_layer, trav.high_node)			
			if (cur_pos > trav_pos):
				#print(graph)
				#print(cur_pos, cur.low_node, cur.high_node)
				#print(trav_pos,trav.low_node, trav.high_node)
				crossings += 1


	return crossings

def getPosition1(graph, layer = -1, node = -1):
	if (layer == -1 or node == None):
		return None
	layer_list = graph[layer]
	for i in range(0, len(layer_list)):
		if (layer_list[i] == node):
			return i
	print(-1)
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


