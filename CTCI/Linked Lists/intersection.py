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

def intersection(head1, head2):
	h1 = head1
	h2 = head2
	s = set()

	while h1:
		if h1.data not in s:
			s.add(h1.data)
		h1 = h1.next

	while h2:
		if h2.data in s:
			return h2.data
		h2 = h2.next
	return False 	

llist1 = LinkedList()
llist1.push(6)
llist1.push(7)
llist1.push(2)

llist2 = LinkedList()
llist2.push(2)
llist2.push(1)
llist2.push(7)

print intersection(llist1.head, llist2.head)