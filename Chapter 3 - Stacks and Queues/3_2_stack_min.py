#3.2 Stack Min

#Design a stack which, in addition to push and pop, has a function min which returns
#the minimum element. Push, pop and min should all operate in O(1) time.

#Thoughts:
#	- Use linked list, push and pop in O(1) time by adding and removing from head
#	- Have each node store the minimum value from that node through the end

from node import Node
from stack import Stack

class MinStack(Stack):
	stack_min = None

	def push(self, val):
		stack_node = Node(val)
		if (not self.top or (self.top and val < self.top.min)):
			stack_node.min = val
		else:
			stack_node.min = self.top.min
		stack_node.nxt = self.top
		self.top = stack_node
		self.stack_min = self.top.min

	def pop(self):
		temp = self.top
		self.top = self.top.nxt
		if (self.top):
			self.stack_min = self.top.min
		return temp.data

if __name__ == "__main__":
	ms = MinStack()
	ms.push(5)
	print(ms.stack_min)
	ms.push(3)
	print(ms.stack_min)
	ms.push(1)
	print(ms.stack_min)
	ms.pop()
	print(ms.peek())
	print(ms.stack_min)
	ms.pop()
	print(ms.is_empty())
	ms.pop()
	print(ms.is_empty())


