from node import Node

class Stack:
	top = None
	
	def push(self, val):
		item = Node(val)
		item.nxt = self.top
		self.top = item

	def pop(self):
		if (self.top):
			item = self.top.data
			self.top = self.top.nxt
			return item
	
	def peek(self):
		if (self.top):
			return self.top.data

	def is_empty(self):
		return (not self.top)