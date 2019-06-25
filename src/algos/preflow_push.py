import math

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

def preflow_push(graph):
	count_nodes = self.get_count_nodes()
	capacities = graph.get_capacities()
	flows = [[0] * count_nodes for __ in range(count_nodes)]
	
	for i in range(1, count_nodes):
		flows[0][i] = capacities[0][i]
		flows[i][0] = -capacities[0][i]

	h = [0] * count_nodes
	h[0] = count_nodes

	excess = [0] * count_nodes
	for i in range(count_nodes):
		excess[i] = flows[0][i]

	while True:
		i = 1
		for k in range(1, count_nodes - 1):
			i = k
			if excess[k] > 0:
				break

		if i == count_nodes - 1:
			break

		j = 0
		for k in range(count_nodes):
			j = k
			if capacities[i][j] - flows[i][j] > 0 and h[i] == h[j] + 1:
				break
		if j < count_nodes:
			push(i, j, flows, excess, capacities)
		else:
			lift(i, h, flows, capacities)
	flow = 0
	for i in range(count_nodes):
		if c[0][i] != 0:
			flow += flows[0][i]
	return max(flow, 0)
