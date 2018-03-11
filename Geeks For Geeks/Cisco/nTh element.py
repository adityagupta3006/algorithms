class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
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
		print "\n"
		
	def calc(self, node, e):
		if node is None :
			return 0
		if node.data == e:
			return 1 + self.calc(node.next, e)
		else:
			return self.calc(node.next, e)


llist = LinkedList()
llist.push(5)
llist.push(1)
llist.push(4)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(1)
llist.push(5)
print llist.calc(llist.head, 1)