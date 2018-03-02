class Node(object):
	"""docstring for node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""docstring for node"""
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		h = self.head
		while(h):
			print h.data
			h = h.next

	def delete(self):
		self.head = None

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print "Given Linked List"
llist.printList()
llist.delete()
print  "After deletion:"
llist.printList()