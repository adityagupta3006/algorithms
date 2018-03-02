class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""docstring for LnkedList"""
	def __init__(self):
		self.head = None
		
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		# 1>2>3>4
		# 4>3>2>1
		prev = None
		current = self.head
		if current is None:
			return
		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		self.head = prev
	
	def printList(self):
		h = self.head
		while(h):
			print h.data
			h = h.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print "Given Linked List"
llist.printList()
llist.reverse()
print "\nReversed Linked List"
llist.printList()