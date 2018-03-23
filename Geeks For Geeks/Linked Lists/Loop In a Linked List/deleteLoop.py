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
		prev = None
		while h:
			if h.data in s:
				prev.next = None
				return
			else:
				s.add(h.data)
				prev = h
				h = h.next
		return

ll1 = LinkedList()
ll1.push(60)
ll1.push(43)
ll1.push(40)
ll1.push(04)
ll1.push(21)
ll1.push(43)
ll1.printList()
ll1.delLoop()
print '\n'
ll1.printList()