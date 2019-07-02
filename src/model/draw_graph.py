import model.create_figure as cf
import model.create_graph as cg
import view.custom_objects as view_objs
import algos.prim_algorithm as prim

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
		self.snapshots.append(self._create_figure(new_bold_edges))
	
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
		fig = cf.create_figure(figure_data, cf.create_layout(annot=view_objs.custom_layout()))
		return fig

	def get_snapshot(self, ind):
		if ind < len(self.snapshots) and ind >= 0:
			self.current_snapshot = ind
			return self.snapshots[self.current_snapshot]

	def count_snapshots(self):
		return len(self.snapshots)

	def apply_prim(self):
		prim.prim_algorithm(self.graph, self)