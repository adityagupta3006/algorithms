class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def printLevelOrder(root):
	if root == None:
		return
	q = []
	q.append(root)
	while q:
		n = q.pop(0)
		if n.left:
			q.append(n.left)
		if n.right:
			q.append(n.right)
		print n.data

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printLevelOrder(root)