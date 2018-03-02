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

def merge(head1, head2):
	
	if head1 is None:
		return head2

	if head2 is None:
		return head1

	temp = None
	if(head1.data <= head2.data):
		temp = head1
#		head1 = head1.next
		temp.next = merge(head1.next, head2)
	else:
		temp = head2
#		head2 = head2.next
		temp.next = merge(head1, head2.next)
	return temp 
		

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
	llist2.push(4)
	llist2.push(2)
	llist2.push(0)

	
	llist3 = LinkedList() 
	llist3.head = merge(llist1.head,llist2.head)
	print "list 3: "
	llist3.printList()