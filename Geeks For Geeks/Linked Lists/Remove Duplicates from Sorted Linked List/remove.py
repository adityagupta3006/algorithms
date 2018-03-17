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
		curr = self.head
		prev = None
		while curr:
			if prev is not None and curr.data == prev.data:	
				prev.next = curr.next
				curr = curr.next
				continue 
			prev = curr
			curr = curr.next

ll1 = LinkedList()
ll1.push(60)
ll1.push(43)
ll1.push(43)
ll1.push(21)
ll1.push(11)
ll1.push(11)
ll1.push(11)
ll1.printList()
ll1.removeDuplicates()
print "\n"
ll1.printList()