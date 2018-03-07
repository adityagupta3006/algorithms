class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

			
def BST(data, start, end):
	if(start > end):
		return None

	mid = (start + end)/2
	node = Node(data[mid])
	print data[mid],
	node.left = BST(data, start, mid-1)
	node.Right = BST(data,mid + 1, end)

	return node
			
def preOrder(node):
	if node == None:
		return
	preOrder(node.left)
	preOrder(node.right)

inp = [1, 2, 3, 4, 5, 6, 7]
l = len(inp)
root = BST(inp, 0, l-1)
preOrder(root)