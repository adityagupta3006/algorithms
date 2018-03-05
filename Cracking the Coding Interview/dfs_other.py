from collections import defaultdict
class Graph:
	visited = []
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)
		return self.graph


	def dfs(self, s):
		if s not in self.visited:
			self.visited.append(s)
			for i in self.graph[s]:
				self.dfs(i)
		return self.visited	

g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
print g.dfs(1)
'''
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print g.dfs(2)
'''