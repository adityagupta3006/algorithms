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

def common(head1, head2):
	nodeset = set()
	while head1:
		if head1.data in nodeset:
			head1 = head1.next
			continue
		else:
			nodeset.add(head1.data)
			head1 = head1.next

	while head2:
		if head2.data in nodeset:
			return head2.data
		head2 = head2.next

	return None


# Driver Function
if __name__ == "__main__":
	# create one list
	llist1 = LinkedList()
	llist1.push(9)
	llist1.push(6)
	llist1.push(3)
	llist1.push(1)

	# create second list
	llist2 = LinkedList()
	llist2.push(7)
	llist2.push(3)
	llist2.push(2)
	llist2.push(0)

	
	n = common(llist1.head, llist2.head)
	print n