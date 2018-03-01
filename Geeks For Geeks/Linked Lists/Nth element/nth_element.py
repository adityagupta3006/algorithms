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

	def nElement(self, n):
		count = 0
		h = self.head
		while h:
			if count == n:
				return h.data

			count += 1
			h = h.next 
		return False

if __name__=='__main__':
 
    llist = LinkedList()
 
    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1);
    llist.push(4);
    llist.push(1);
    llist.push(12);
    llist.push(1);
 
    n = 3
    print ("Element at index 3 is :", llist.nElement(n))