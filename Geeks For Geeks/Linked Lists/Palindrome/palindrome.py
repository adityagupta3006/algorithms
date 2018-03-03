class Node(object):
	def __init__(self, data):
		self. data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node

	def printList(self):
		head = self.head
		while(head):
			print head.data
			head = head.next

	def palindrome(self):
		stack = []
		h = self.head
		length = 0
		while h!= None:
			stack.append(h.data)
			h = h.next
			length += 1
		h = self.head
		for i in range(length/2):
			p = stack.pop()
			if p != h.data:
				return False
			h = h.next
		return True
		

# Driver Function
if __name__ == "__main__":
	# create one list
	llist1 = LinkedList()
	llist1.push(9)
	llist1.push(6)
	llist1.push(3)
	llist1.push(1)
	llist1.push(4)
	llist1.push(1)
	llist1.push(3)
	llist1.push(6)
	llist1.push(9)
	print llist1.palindrome()