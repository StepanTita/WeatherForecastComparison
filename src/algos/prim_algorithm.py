from collections import deque
import math
import graph as gr
from sortedcontainers import SortedSet

def prim_algorithm(graph, vis=None):
	adj_matr = graph.get_adj_matrix()

	if vis is not None:
		vis.clear_snapshots()

	nodes_count = graph.get_count_nodes()

	min_edge = [math.inf] * nodes_count
	end_edge = [-1] * nodes_count
	used = [False] * nodes_count
	min_edge[0] = 0
	result_mst = []

	for i in range(nodes_count):
		v = -1
		
		for j in range(nodes_count):
			if not used[j] and (v == -1 or min_edge[j] < min_edge[v]):
				v = j
		#endfor
		
		if min_edge[v] == math.inf:
			print("NO MST")
			return None
		
		used[v] = True
		if end_edge[v] != -1:
			result_mst.append((v, end_edge[v]))
			#print(result_mst)
			if vis is not None:
				vis.create_snapshot(result_mst)
		
		for to in range(nodes_count):
			if adj_matr[v][to] < min_edge[to]:
				min_edge[to] = adj_matr[v][to]
				end_edge[to] = v
		#endfor
	#endfor
	#print(result_mst)
	return result_mst
#endprim


def main():
	my_gr = gr.GraphWeighted([
		(0, 1, 2),
      	(1, 2, 3),
      	(2, 3, 2),

      	(0, 2, 5),
      	(0, 3, 4),
      	(1, 4, 7)
		], 5)
	prim_algorithm(my_gr)

if __name__ == '__main__':
	main()