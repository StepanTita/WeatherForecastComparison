from collections import deque
import math
import graph

def prim_algorithm(graph):
	graph.sort_adj()

	nodes_count = graph.get_count_nodes()

	min_edge = [math.inf] * nodes_count
	end_edge = [-1] * nodes_count
	min_edge[0] = 0

	q = deque()
	q.append((0, 0))

	for i in range(nodes_count):
		if len(q) == 0:
			print("NO MST") ########################################################################
			return
		v = q.pop()
		if end_edge[v] != -1:
			result_mst.append((v, end_edge[v]))
		
		edges = graph.get_edges(i)
		for j in range(len(edges)):
			to = edges[j][0]
			weight = edges[j][1]

			if weight < min_edge[to]:
				q.remove((min_edge[to], to))
				min_edge[to] = weight
				end_edge[to] = v
				q.append((min_edge[to], to))
			#endif
		#endfor
	#endfor
#endprim


def main():
	pass

if __name__ == '__main__':
	main()