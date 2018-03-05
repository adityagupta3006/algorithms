class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		h = self.head 
		while h:
			print h.data
			h = h.next
	
	def loop(self):
		h = self.head
		s = set()
		while h:
			if h.data in s:
				return h.data
			else:
				s.add(h.data)

			h = h.next

llist1 = LinkedList()
llist1.push(6)
llist1.push(7)
llist1.push(2)
llist1.push(6)

print llist1.loop()