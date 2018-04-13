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

	def printReverse(self, node):
		if node == None:
			return

		self.printReverse(node.next)

		print(node.data),

	def insertAfter(self, prevNode, new_data):
		if prevNode is None:
			return
		new_node = Node(new_data)
		new_node.next = prevNode.next
		prevNode.next = new_node
		
	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return
		t = self.head
		while(t.next):
			t = t.next
		t.next = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next

if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.push(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.push(4)
    llist.printList()
    
    llist.printReverse(llist.head)