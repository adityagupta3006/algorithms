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
		s = set()
		while curr:
			if curr.data in s:
				prev.next = curr.next
				curr = curr.next
				continue
			s.add(curr.data)
			prev = curr
			curr = curr.next


ll1 = LinkedList()
ll1.push(21)
ll1.push(43)
ll1.push(41)
ll1.push(21)
ll1.push(12)
ll1.push(11)
ll1.push(12)
ll1.printList()
print "\n"
ll1.removeDuplicates()
ll1.printList()

#12->11->12->21->41->43->21 