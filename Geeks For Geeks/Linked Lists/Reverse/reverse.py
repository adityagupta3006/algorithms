class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LnkedList(object):
	"""docstring for LnkedList"""
	def __init__(self):
		self.head = None
		
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		h = self.head
		if h is None:
			return
		 while h:
		 	h.next.next = 