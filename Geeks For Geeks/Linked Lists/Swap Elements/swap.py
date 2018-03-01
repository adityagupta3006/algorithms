class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None;

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def swap(self, x, y):
		#1->2->3->4->5
		if x==y:
			return
		prevX = None
		currX = self.head
		while(currX or currX.data != x):
			prevX = currX
			currX = currX.next

		prevY = None
		currY = self.head
		while(currY or currY.data != y):
			prevY = currY
			currY = currY.next		

		if currX==None or currY== None:
			return

		# if x is not the head 
		if prevX != None:
			prevX.next = currY
		else:
			self.head = currY

		if prevY != None:
			prevY.next = currX
		else:
			self.head = currX

		t = currX.next
		currX.next = currY.next
		currY.next = t

		

	def printList(self):
		h = self.head

		while(h):
			print h.data
			h = h.next
# Python program to swap two given nodes of a linked list
class LinkedList(object):
    def __init__(self):
        self.head = None
 
    # head of list
    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None
 
    # Function to swap Nodes x and y in linked list by
    # changing links
    def swapNodes(self, x, y):
 
        # Nothing to do if x and y are same
        if x == y:
            return
 
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
 
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
 
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else: #make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else: # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
 
    # Function to add Node at beginning of list.
    def push(self, new_data):
 
        # 1. alloc the Node and put the data
        new_Node = self.Node(new_data)
 
        # 2. Make next of new Node as head
        new_Node.next = self.head
 
        # 3. Move the head to point to new Node
        self.head = new_Node
 
    # This function prints contents of linked list starting
    # from the given Node
    def printList(self):
        tNode = self.head
        while tNode != None:
            print tNode.data,
            tNode = tNode.next
 
# Driver program to test above function
llist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print "Linked list before calling swapNodes() "
llist.printList()
llist.swapNodes(4, 3)
print "\nLinked list after calling swapNodes() "
llist.printList()