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

	def nLast(self, n):
		length = 0
		h = self.head
		while h:
			h = h.next
			length += 1

		if length<n:
			return
		h = self.head

		for i in range(length-n):
			h = h.next
		return h.data

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)

#print llist.nLast(4)

