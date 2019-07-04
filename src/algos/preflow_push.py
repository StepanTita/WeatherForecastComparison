import math
import graph as gr

def push(u, v, flows, excess, capacities):
	d = min (excess[u], capacities[u][v] - flows[u][v])
	flows[u][v] += d
	flows[v][u] = - flows[u][v]
	excess[u] -= d
	excess[v] += d

def lift(u, h, flows, capacities):
	d = math.inf
	for i in range(len(flows)):
		if capacities[u][i] - flows[u][i] > 0:
			d = min(d, h[i])
	if d == math.inf:
		return
	h[u] = d + 1

def preflow_push(graph, vis):
	if vis is not None:
		vis.clear_snapshots()

	count_nodes = graph.get_count_nodes()
	cap = graph.get_capacities()
	flows = [[0] * count_nodes for __ in range(count_nodes)]
	
	for i in range(1, count_nodes):
		flows[0][i] = cap[0][i]
		flows[i][0] = -cap[0][i]
	h = [0] * count_nodes
	h[0] = count_nodes

	excess = [0] * count_nodes
	for i in range(1, count_nodes):
		excess[i] = flows[0][i]

	while True:
		i = 1
		for k in range(1, count_nodes):
			i = k
			if excess[k] > 0:
				break

		if i == count_nodes - 1:
			break

		j = 0
		for k in range(count_nodes + 1):
			j = k
			if j < count_nodes and cap[i][j] - flows[i][j] > 0 and h[i] == h[j] + 1:
				break
		if j < count_nodes:
			push(i, j, flows, excess, cap)
		else:
			lift(i, h, flows, cap)
		if vis is not None:
			vis.create_snapshot_flow(flows)

	flow = 0
	for i in range(count_nodes):
		if cap[0][i] != 0:
			flow += flows[0][i]

	print("---------------------------------")
	print_matr(flows)
	return max(flow, 0)

def print_matr(lst):
	for idx, n1 in enumerate(lst):
		print(idx, end="")
		for n2, w in enumerate(lst[idx]):
			print(" --> (" + str(n2) + ", " + str(w) + ")", end=" ")
		print("")

def main():
	my_gr = gr.GraphWeighted([
		(0, 1, 2),
      	(1, 2, 3),
      	(2, 3, 2),

      	(0, 2, 5),
      	(0, 3, 4),
      	(1, 4, 7)
		], 5)
	preflow_push(my_gr, None)

if __name__ == '__main__':
	main()