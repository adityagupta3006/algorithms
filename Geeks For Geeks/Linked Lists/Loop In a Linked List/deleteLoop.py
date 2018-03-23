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

	def delLoop(self):
		h = self.head
		s = set()
		while h:
			if h.data in s:
				return
			else:
				s.add(h.data)

		return

ll1 = LinkedList()
ll1.push(60)
ll1.push(43)
ll1.push(43)
ll1.push(21)