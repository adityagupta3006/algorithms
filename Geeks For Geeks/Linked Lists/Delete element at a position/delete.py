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

	def deleteNode(self, position):
		h = self.head
		if h == None:
			return 

		# remove head
		if position == 0:
			self.head = h.next
			h = None
			return

		count = 0
		curr = self.head
		while curr:
			if count == position:
				prev.next = curr.next
				return

			prev = curr
			curr = curr.next
			count += 1

		return


	def getLength(self):
		count = 0
		h = self.head
		while h:
			h = h.next
			count += 1

		return count

	def getLengthRec(self, node):
		if node is None:
			return 0
		else: 
			return 1 + self.getLengthRec(node.next)

	def search(self, node, element):
		if node is None:
			return False
		if node.data == element:
			return True
		return self.search(node.next, element)

	def swap(self, x, y):
		if x == y:
			return "same elements"
 
		prevX = None
		currX = self.head

		while currX:
			if currX.data == x:
				break
			prevX = currX
			currX = currX.next

		if currX is None:
			return "currX is none"

		
		prevY = None
		currY = self.head
		
		while currY:
			if currY.data == y:
				break
			prevY = currY
			currY = currY.next

		if currY is None:
			return "curry is none" 

		if prevX != None:
			prevX.next = currY
		else:
			#print "prevX is none"
			self.head = currY

		if prevY != None:
			#print "prevY is not none"
			prevY.next = currX
		else:
			self.head = currX

		temp = currX.next
		currX.next = currY.next
		currY.next = temp


llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

#llist.printList()
#llist.deleteNode(1)
#llist.printList()
#print llist.getLength()
#print llist.getLengthRec(llist.head)
llist.printList()
llist.swap(2, 3)
llist.printList()
