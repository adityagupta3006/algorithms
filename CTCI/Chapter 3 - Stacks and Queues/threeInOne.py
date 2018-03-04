class Stack:
	def __init__(self):
		self.stack = [] 		

	def push(self, data):
		return self.stack.append(data)
	
	def pop(self):
		return self.stack.pop()

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[len(self.stack)-1]

def makeStackCal(array, a, b):
	new_stack = Stack()
	for i in range(a, b):
		new_stack.push(array[i])
	return new_stack

def makeStack(array):
	l = len(array)
	return makeStackCal(array, 0, l/3),	makeStackCal(array, l/3, 2*l/3), makeStackCal(array, 2*l/3, l)
	
array = [1, 2, 3, 4, 5]
a, b, c = makeStack(array)