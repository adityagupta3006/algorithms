from collections import defaultdict

class Graph:

	# constructor
	def __init__(self):
		# default dictionary to store graph
		self.graph = defaultdict(list)

	# adding edge
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# printing BFS
	def bfs(self, s):

		visited = [False]*(len(self.graph))

		# creating queue for BFS
		queue = []

		# mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop(0)
			print s,
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is Breadth First Traversal (starting from vertex 2)"
g.bfs(2)