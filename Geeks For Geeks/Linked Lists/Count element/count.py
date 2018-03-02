class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""docstring for Node"""
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def count(self, n):
		count = 0
		h = self.head
		while(h):
			if h.data == n:
				count+=1
			h = h.next
		return count

	def printList(self):
		h = self.head
		while h:
			print h.data
			h = h.next


# Driver program
llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)
 
# Check for the count function
print "count of 1 is %d" %(llist.count(1))