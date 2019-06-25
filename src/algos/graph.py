import math

class Edge(object):
	"""docstring for Edge"""
	def __init__(self, node_fr, node_to, cap, cost, e_id):
		super(Edge, self).__init__()
		self.capacity = cap
		self.node_fr = node_fr
		self.node_to = node_to
		self.cost = cost
		self.flow = 0
		self.e_id = e_id

	def get_from(self):
		return self.node_fr

	def get_to(self):
		return self.node_to

class GraphWeighted(object):
	"""docstring for GraphWeighted"""
	def __init__(self, count_nodes, count_edges):
		super(Graph, self).__init__()
		self.count_edges = count_edges
		self.adj_list = [list()] * count_nodes
		
	def add_edge_undirected(self, node_fr, node_to, weight):
		self.adj_list[node_fr].append((node_to, weight))
		self.adj_list[node_to].append((node_fr, weight))

	def get_count_nodes(self):
		return len(self.adj_list)

	def sort_adj_list(self):
		for edges in adj_list:
			edges.sort(key=lambda x: x[1])

	def get_edges(self, v):
		return adj_list[v]

	def get_adj_matrix(self):
		count_nodes = self.get_count_nodes()
		adj_matrix = [[0] * count_nodes for __ in range(count_nodes)]
		for i in range(count_nodes):
			for j, w in self.adj_list[i]:
				adj_matrix[i][j] = w
		return adj_matrix

	def get_capacities(self):
		count_nodes = self.get_count_nodes()
		cap = [[0] * count_nodes for __ in range(count_nodes)]
		for i in range(count_nodes):
			for j, w in self.adj_list[i]:
				cap[i][j] += w
		return cap

class GraphNetwork(object):
	"""docstring for GraphNetwork"""
	def __init__(self, count_nodes):
		super(GraphNetwork, self).__init__()
		self.count_nodes = count_nodes
		self.dist = [math.inf] * count_nodes
		self.used_edge = [-1] * count_nodes
		self.edges = []
		self.connects = [None] * count_nodes

	def add_edge(self, fr, to, cap, cost, e_id):
		e1 = Edge(fr, to, cap, cost, e_id)
		edges.append(e1)

		e2 = Edge(to, fr, 0, -cost, e_id)
		edges.append(e2)

		self.connects[fr.append(e1)]

	def find_delta_flow(self, fr, to):
		v = to
		curr_b = math.inf
		while v != fr:
			curr_b = min(curr_b, edges[used_edge[v]].capacity)
			v = edges[used_edge[v]].node_fr
		return curr_b

	def add_flow(self, fr, to, flow):
		v = to
		delta_cost = 0
		while v != fr:
			edges[used_edge[v]].flow += flow
			edges[used_edge[v] ^ 1].flow -= flow

			delta_cost += flow * edges[used_edge[v]].cost
			v = edges[used_edge[v]].node_fr
		return curr_b

	def ford_bellman(self):
		for ph in range(self.count_nodes - 1):
			to_upd = False
			for idx, e in enumerate(edges):
				fr = e.node_fr
				to = e.node_to

				if e.flow >= e.capacity || self.dist[fr] == math.inf:
					continue

				if self.dist[to] > self.dist[fr] + e.cost:
					used_edge[to] = idx
					to_upd = True
			if !to_upd:
				break


	def is_path(self, fr, to):
		self.dist = [math.inf] * count_nodes
		self.used_edge = [-1] * count_nodes

		self.dist[0] = 0
		ford_bellman()
		return self.dist[to] != math.inf

	def find_min_cost_flow(self, fr, to, target=math.inf):
		cost = 0
		flow = 0

		while flow < target and is_path(fr, to):
			delta_flow = find_delta_flow(fr, to)
			cost += add_flow(fr, to, delta_flow)
			flow += delta_flow
		return (cost, flow)

