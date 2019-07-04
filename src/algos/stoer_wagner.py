import math

def mincut(graph, vis):
	vis.clear_snapshots()
	count_nodes = graph.get_count_nodes()
	shrinked = [[i] for i in range(count_nodes)]

	adj_matrix = graph.get_adj_matrix(0)

	best_cost = math.inf
	best_cut = []
	exist = [True] * count_nodes
	for ph in range(count_nodes - 1):
		print(best_cut)
		in_a = [False] * count_nodes
		w = [0] * count_nodes
		prev = -1
		for it in range(count_nodes - ph):
			max_cost = -1
			for i in range(count_nodes):
				if exist[i] and not in_a[i] and (max_cost == -1 or w[i] > w[max_cost]):
					max_cost = i
			if it == count_nodes - ph - 1:
				if w[max_cost] < best_cost:
					best_cost = w[max_cost]
					best_cut = shrinked[max_cost]
					print(best_cut)
					vis.create_snapshot_nodes(best_cut)
				shrinked[prev] += shrinked[max_cost]
				for i in range(count_nodes):
					adj_matrix[i][prev] += adj_matrix[max_cost][i]
					adj_matrix[prev][i] = adj_matrix[i][prev]
				exist[max_cost] = False
			else:
				in_a[max_cost] = True
				for i in range(count_nodes):
					w[i] += adj_matrix[max_cost][i]
				prev = max_cost
			#endif it
		#endfor it
	#endfor ph
#end_mincut