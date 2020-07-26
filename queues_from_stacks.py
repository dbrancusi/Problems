class Queue:
	def __init__(self):
		self.outstack = []
		self.instack = []

	def dequeue(self):
		if not self.outstack:
      		while self.instack:
        	self.queue1.append(self.append(self.instack.pop()))

    return self.outstack.pop()

	def enqueue(self, x):
		 self.instack.append(x)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
