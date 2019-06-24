class DSU(object):
	"""docstring for DSU"""
	def __init__(self, size):
		super(DSU, self).__init__()
		self.size = size
		self.parents = [i for i in range(size)]
		self.rank = [0] * size

	def find(self, a):
		if self.parents[a] != a:
			self.parents[a] = find(self.parents[a])
		return self.parents[a]
	
	def union(self, a: int, b: int):
		a = find(a)
		b = find(b)
		if a == b:
			return
		if ranks[a] == ranks[b]:
			ranks[a] += 1

		# подвешиваем одно дерево к другому:
		if ranks[a] < ranks[b]:
			parents[a] = b
		else:
			parents[b] = a
