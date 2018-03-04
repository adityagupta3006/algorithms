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

def makeNum(head):
	h = head
	number = 0
	d = 1
	while h is not None:
		number = h.data*d + number
		d = d*10
		h = h.next  
	return number

def sumLists(head1, head2):
	s = makeNum(head1) + makeNum(head2)
	return s

llist1 = LinkedList()
llist1.push(6)
llist1.push(1)
llist1.push(7)

llist2 = LinkedList()
llist2.push(2)
llist2.push(9)
llist2.push(5)

print sumLists(llist1.head, llist2.head)