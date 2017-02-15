import itertools

def permWrapper2(g=Graph()):
	permutate2(g, 400000)

def permutate2(g=Graph(), minimum = 4000):
	if(layer == -1):
		return None
	graph = g.graph
	permutation_list= []
	for layer in graph:
		p = itertools.permutations(layer)
		permutation_list.append(p)
	printPerms(permutation_list):
printPerms(







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


