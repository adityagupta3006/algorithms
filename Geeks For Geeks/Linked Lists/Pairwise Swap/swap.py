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

	def swap(self):
		curr  = self.head
		while curr and curr.next:
			curr.data, curr.next.data = curr.next.data, curr.data
			curr = curr.next.next

ll1 = LinkedList()
#ll1.push(8)
#ll1.push(7)
ll1.push(6)
ll1.push(5)
ll1.push(4)
ll1.push(3)
ll1.push(2)
ll1.push(1)

ll1.printList()
ll1.swap()
print '\n'
ll1.printList()