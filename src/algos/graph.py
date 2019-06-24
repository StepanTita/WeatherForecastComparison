class Edge(object):
	"""docstring for Edge"""
	def __init__(self, node_fr, node_to, weight):
		super(Edge, self).__init__()
		self.weight = weight
		self.node_fr = node_fr
		self.node_to = node_to

	def get_from(self):
		return self.node_fr

	def get_to(self):
		return self.node_to

class Node(object):
	"""docstring for Node"""
	def __init__(self, data=None):
		super(Node, self).__init__()
		self.data = data

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

	def sort_adj(self):
		for edges in adj_list:
			edges.sort(key=lambda x: x[1])

	def get_edges(self, v):
		return adj_list[v]