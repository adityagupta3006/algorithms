# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP 
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

	def printList(self):
		h = self.head 
		while h:
			print h.data
			h = h.next

def remDup(head):
	s = set()
	prev = None
	while head is not None:
		if head.data not in s:
			s.add(head.data)
		else:
			prev.next = head.next
			head = head.next
			continue
		prev = head
		head = head.next 

llist = LinkedList()
llist.push('P')
llist.push('U')
llist.push(' ')
llist.push('W')
llist.push('O')
llist.push('L')
llist.push('L')
llist.push('O')
llist.push('F')
#llist.printList()
remDup(llist.head)
llist.printList()