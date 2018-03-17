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

	def printReverse(self, h):
		if h is None:
			return
		self.printReverse(h.next)
		print h.data,

ll1 = LinkedList()
ll1.push(1)
ll1.push(2)
ll1.push(3)
ll1.push(4)
#ll1.printList()

ll1.printReverse(ll1.head)