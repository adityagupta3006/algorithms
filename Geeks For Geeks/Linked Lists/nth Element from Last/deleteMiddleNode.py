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

	def delete(self, node):
		node.data = node.next.data
		node.next = node.next.next
	
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.printList()
llist.delete(llist.head.next)
print '\n'
llist.printList()

