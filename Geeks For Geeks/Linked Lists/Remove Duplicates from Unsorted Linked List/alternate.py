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

	def removeDuplicates(self):
		h = self.head
		s = set()
		prev = None
		while h and h.next:
			if h.data in s:
				prev.next = h.next
				h = h.next
				continue
			
			if h.data not in s:
				s.add(h.data)
			
			prev = h
			h = h.next

ll1 = LinkedList()
ll1.push(21)
ll1.push(43)
ll1.push(11)
ll1.push(43)
ll1.push(11)
ll1.push(60)
ll1.push(11)
ll1.printList() 
print '\n'
ll1.removeDuplicates()

ll1.printList()