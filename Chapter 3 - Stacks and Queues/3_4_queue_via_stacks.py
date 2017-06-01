#3.4 Queue via Stacks

#Implement a MyQueue class which implements a queue using two stacks

#Thoughts:
# - Queue is FIFO, so push all elements onto one stack, invert into other then pop

#Illustration:
# If we add a,b,c,d to queue:
# entry: d->c->b->a => transfer => exit: a->b->c->d

from stack import Stack

class MyQueue:
	entry = Stack()
	exit = Stack()

	def add(self, val):
		self.entry.push(val)

	def remove(self):
		if self.is_empty():
			return
		if self.exit.is_empty():
			self.transfer()
		return self.exit.pop()

	def peek(self):
		if self.is_empty():
			return
		if self.exit.is_empty():
			self.transfer()
		return self.exit.top.data

	def is_empty(self):
		return self.entry.is_empty() and self.exit.is_empty()

	def transfer(self):
		while not self.entry.is_empty() :
			self.exit.push(self.entry.pop())

if __name__ == "__main__":
	mq = MyQueue()
	mq.add(5)
	mq.add(4)
	mq.add(3)
	mq.add(2)
	mq.add(1)
	print(mq.remove())
	print(mq.remove())
	print(mq.remove())
	print(mq.remove())
	print(mq.remove())
		

