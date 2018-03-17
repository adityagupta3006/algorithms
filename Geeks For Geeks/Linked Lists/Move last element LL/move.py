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
		if h is None or h.next is None:
			return

		while h:
			print h.data,
			h = h.next

		print "\n"

	def move(self):
		h = self.head
		#prev = self.head

		while h.next:
			prev = h
			h = h.next

		prev.next = None
		h.next = self.head
		self.head = h

ll1 = LinkedList()
#ll1.push(12)
ll1.push(1)
ll1.push(2)
ll1.push(3)
ll1.push(4)

ll1.printList()

ll1.move()
 
ll1.printList()