import igraph as ig
from load_data import load_data

def create_graph(data):
	nodes_count = len(data['nodes'])
	edges_count = len(data['links'])

	Edges=[(data['links'][i]['source'], data['links'][i]['target']) for i in range(edges_count)]

	return ig.Graph(Edges, directed=False)

if __name__ == "__main__":
	print(create_graph(load_data()))