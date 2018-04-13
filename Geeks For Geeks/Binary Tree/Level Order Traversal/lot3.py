class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def lot(self, root):
		q = []
		q.append(root)
		while q:
			for i in q:
				print i.data,
			print ''
			
			t = []
			for a in q:
				t.extend([a.left, a.right])
			q = [a for a in t if a]

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.right = Node(7)
root.lot(root)