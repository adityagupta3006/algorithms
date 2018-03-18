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
		if h is None or h.next is None:
			return

		while h:
			print h.data,
			h = h.next

		print "\n"

def intersection(h1, h2):
	ll3 = LinkedList()
	s = set()
	while h1:
		if h1.data in s:
			continue
		s.add(h1.data)
		h1 = h1.next

	while h2:
		print "h2.data is = ", h2.data
		print ll3.printList()
		if h2.data in s:
			ll3.push(h2.data)

		h2 = h2.next
		print '\n'
	
	return ll3

ll1 = LinkedList()
ll1.push(6)
ll1.push(4)
ll1.push(3)
ll1.push(2)
ll1.push(1)

ll2 = LinkedList()
ll2.push(8)
ll2.push(6)
ll2.push(4)
ll2.push(2)

ll3 = intersection(ll1.head, ll2.head)
ll3.printList()