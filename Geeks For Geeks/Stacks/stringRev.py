class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		if len(self.stack) == 0:
			return True

	def push(self, item):
		self.stack.append(item)

	def pop(self):
	    if self.isEmpty():
	    	return
	    return self.stack.pop()

def rev(strin):
	s = Stack()

	for i in strin:
		s.push(i)
	
	a = ''
	while not s.isEmpty():
		a = a + s.pop()

	return a

strin = "GeeksQuiz"

print rev(strin)