from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

		 
	def bfs(self, s):
		print self.graph
		visited = [False]*(len(self.graph))
		queue = []

		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop(0)
		 	print s
		 	for i in self.graph[s]:
		 		if visited[i] == False:
		 			queue.append(i)
		 			visited[i] = True

'''
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
'''
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,3)
g.addEdge(4,4)
g.addEdge(5,5)
g.addEdge(6,6)
print "Following is Breadth First Traversal (starting from vertex 2)"
g.bfs(0)