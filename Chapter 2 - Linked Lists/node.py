class Node:
	def __init__(self, value):
		self.data = value
		self.nxt = None

	def __str__(self):
		return str(self.data)

	# def __eq__(self, other):
	# 	return self.data == other.data