class MyQueue(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self, data):
		self.stack1.append(data)

	def dequeue(self):
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()

	def size(self):
		len(self.queue)
		
array = [1,2,3]
queue = MyQueue()
for i in array:
	queue.enqueue(i)

print queue.dequeue()