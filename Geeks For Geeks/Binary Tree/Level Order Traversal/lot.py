class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printLevel(root, i)

def printLevel(root, level):
	
	if root == None:
		return
	if level == 1:
		print root.data
	else:
		printLevel(root.left, level-1)
		printLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
	
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printLevelOrder(root)