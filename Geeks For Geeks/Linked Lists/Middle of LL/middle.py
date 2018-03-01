class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def middle(self):
		first = self.head
		second = first.next
		if first == None:
			return

		while second!= None:
			first = first.next
			second = second.next.next

		return first.data

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)

print llist.middle()