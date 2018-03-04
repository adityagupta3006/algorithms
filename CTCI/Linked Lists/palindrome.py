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
	
	def palindrome(self):
		h = self.head
		s = []
		count = 0
		while h:
			s.append(h.data)
			h = h.next
			count += 1
		print s
		
		h = self.head

		for i in range(count/2):
			if h.data != s.pop():
				return False
			h = h.next
		return True
			

	def printList(self):
		h = self.head 
		while h:
			print h.data
			h = h.next
	
llist1 = LinkedList()
llist1.push(6)
llist1.push(1)
llist1.push(7)
llist1.push(7)
llist1.push(1)
llist1.push(6)
#llist1.push(2)
#llist1.printList()
print llist1.palindrome()