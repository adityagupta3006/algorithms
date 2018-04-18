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
			print h.data,
			h = h.next

def add(head1, head2):
	ct = 0
	num = 0
	while head1:
		val = head1.data + head2.data
		num = num + val*(10**ct)
		ct = ct+1
		head1 = head1.next
		head2 = head2.next
	return makeList(num)


def makeList(data):
	llistSum = LinkedList()
	for a in str(data):
		llistSum.push(a)
	return llistSum.head

llist = LinkedList()
llist.push(3)
llist.push(2)
llist.push(1)

llist1 = LinkedList()
llist1.push(6)
llist1.push(5)
llist1.push(4)
#llist.printList()
print '\n'
#llist1.printList()

h =  add(llist.head, llist1.head)
while h:
	print h.data
	h = h.next