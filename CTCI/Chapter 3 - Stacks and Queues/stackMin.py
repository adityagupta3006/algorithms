class Stack:
	def __init__(self):
		self.stack = [] 	
		self.min = None
		self.min_ar = []	

	def push(self, data):
		if self.min == None or self.min >= data:
			self.min = data
			self.mins.append(item)

		return self.stack.append(data)
	
	def pop(self):
		item = self.stack.pop()
		if item == self.min:
			self.min_ar.pop()
			self.min = seld.min_ar[-1]
		return self.stack.pop()

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[len(self.stack)-1]

	def min(self):
		return self.min
