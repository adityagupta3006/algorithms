class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		if len(self.stack) == 0:
			return True



	def peek(self):
		return self.stack[len(self.stack)-1]
			
	def push(self, item):
		self.stack.append(item)
	
	def pop(self):
		if self.isEmpty():
			return
		return self.stack.pop()

	def pr(self):
		return self.stack

	def sort(self):
		sortStack = Stack()
		while self.stack:
			x = self.pop()
			while (sortStack.isEmpty() != True) and sortStack.peek() > x:
				self.push(sortStack.pop())
			sortStack.push(x)
		return sortStack
  
s = Stack()
s.push(10)
s.push(21)
s.push(12)
s.push(13)
s.push(2)
a =  s.sort()
while not a.isEmpty():
	print a.pop(),