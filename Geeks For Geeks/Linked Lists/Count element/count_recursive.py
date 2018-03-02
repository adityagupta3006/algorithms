class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""docstring for Node"""
	def __init__(self):
		self.head = None
		self.frequency = 0

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def count(self, h, n):
		#print h.data
		if h == None:
			return self.frequency

		if h.data == n:
			self.frequency += 1
		
		count(h.next, n) 

		

# Driver program
llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1) 
# Check for the count function
print llist.count(llist.head, 1)