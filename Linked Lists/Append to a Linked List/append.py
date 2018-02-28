def append(self, new_data):
	new_node = node(new_data)
	if self.head is none:
		self.head = Node(new_node)
		return
	last = self.head
	while(last):
		last = last.next
	last.next = new_node
	new_node.next = null 