class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		h = self.head
		while h:
			print h.data,
			h = h.next

def identical(node1, node2):
	


ll1 = LinkedList()
#ll1.push(12)
ll1.push(1)
ll1.push(2)
ll1.push(3)


ll2 = LinkedList()
ll2.push(1)
ll2.push(2)
ll2.push(3)

print identical(ll1.head, ll2.head)