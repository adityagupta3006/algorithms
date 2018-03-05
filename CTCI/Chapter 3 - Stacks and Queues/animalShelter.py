class Queue:
	def __init__(self):
		self.queue = []
		self.pqueue = []

	def enqueue(self, data):
		self.queue.insert(0, data)

	def dequeue(self):
		return self.queue.pop()

	def dequeueCat(self):
		p = self.queue.pop()
		while p!= "cat":
			self.pqueue.insert(0,p)
			p = self.queue.pop()
		while self.pqueue:
			self.queue.append(self.pqueue.pop())
		self.pqueue = []
		return p


	def dequeueDog(self):
		p = self.queue.pop()
		while p!= "dog":
			self.pqueue.insert(0,p)
			p = self.queue.pop()
		while self.pqueue:
			self.queue.append(self.pqueue.pop())
		self.pqueue = []
		return p


q = Queue()
q.enqueue("dog")
q.enqueue("dog")
q.enqueue("cat")
q.enqueue("dog")
q.enqueue("cat")
print "initial queue = ", list(q.queue)
#print q.dequeueDog()
print "take a cat = ", list(q.queue)