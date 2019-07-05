import model.create_figure as cf
import model.create_graph as cg
import view.custom_objects as view_objs
import algos.prim_algorithm as prim
import algos.stoer_wagner as stw
import algos.preflow_push as pfp
import math

def print_matr(lst):
	for idx, n1 in enumerate(lst):
		print(idx, end="")
		for n2, w in enumerate(lst[idx]):
			print(" --> (" + str(n2) + ", " + str(w) + ")", end=" ")
		print("")

class GraphVisual(object):
	"""docstring for GraphVisual"""
	def __init__(self, graph):
		super(GraphVisual, self).__init__()
		self.current_snapshot = 0
		self.graph = graph
		self.snapshots = [self._create_figure()]

	def create_snapshot(self, edges):
		new_bold_edges = self._create_bold(len(self.graph.get_adj_list()))
		for e in edges:
			new_bold_edges[e[0]][e[1]] = True
			new_bold_edges[e[1]][e[0]] = True
		#print(new_bold_edges)
		self.snapshots.append(self._create_figure(new_bold_edges))

	def create_snapshot_nodes(self, nodes):
		adj_list = self.graph.get_adj_list()
		new_bold_edges = self._create_bold(len(adj_list))
		for n in nodes:
			for adj, w in adj_list[n]:
				if adj in nodes:
					new_bold_edges[n][adj] = True
					new_bold_edges[adj][n] = True
		print_matr(new_bold_edges)
		self.snapshots.append(self._create_figure(new_bold_edges))

	def create_snapshot_flow(self, flows):
		max_flow = math.inf
		for i in flows:
			max_flow = max(i)
		self.snapshots.append(self._create_figure_flows(flows, max_flow))
	
	def _create_bold(self, size):
		return [[False] * size for __ in range(size)]

	def next_snapshot(self):
		nxt = self.current_snapshot + 1
		if nxt > len(self.snapshots):
			return
		self.current_snapshot = nxt;
		return self.snapshots[self.current_snapshot]

	def prev_snapshot(self):
		prev = self.current_snapshot - 1
		if prev < 0:
			return
		self.current_snapshot = prev
		return self.snapshots[prev]

	def _create_figure(self, bold_edges=None):
		data = self.graph.get_data()
		data['bold'] = bold_edges
		graph = cg.create_graph(data)
		figure_data = cf.create_data(graph, data)
		fig = cf.create_figure(figure_data, cf.create_layout(axis=view_objs.custom_axis()), view_objs.get_bold_traces)
		return fig

	def _create_figure_flows(self, flows, max_flow):
		data = self.graph.get_data()
		data['scale'] = [[(i / (max_flow + 1)) * 3 for i in __] for __ in flows]
		graph = cg.create_graph(data)
		figure_data = cf.create_data(graph, data)
		fig = cf.create_figure(figure_data, cf.create_layout(axis=view_objs.custom_axis()), view_objs.get_scale_traces)
		return fig

	def get_snapshot(self, ind):
		#print(self.snapshots)
		if ind < len(self.snapshots) and ind >= 0:
			self.current_snapshot = ind
			return self.snapshots[self.current_snapshot]

	def count_snapshots(self):
		return len(self.snapshots)

	def apply_prim(self):
		prim.prim_algorithm(self.graph, self)

	def apply_stoer_wagner(self):
		stw.mincut(self.graph, self)

	def apply_preflow(self):
		pfp.preflow_push(self.graph, self)

	def clear_snapshots(self):
		self.snapshots.clear()

	def get_frames(self):
		return self.snapshots