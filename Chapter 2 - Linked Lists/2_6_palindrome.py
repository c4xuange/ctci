#2.6 Palindrome

#Implement a function to check if a linked list is a palindrome

#Thoughts:
# - Can use a stack, after we get to the middle node, pop and check if it matches next node
# - How to find middle node? -> can use two pointers, when one gets to end, other is at middle

# Ex: a -> b -> c -> b -> a

# Runtime: O(n)
# Space complexity: O(1)

from stack import Stack
from linked_list import LinkedList

def is_palindrome_ll(linked_list):
	st = Stack()
	front = back = linked_list.head
	while back != None and back.nxt != None:
		st.push(front.data)
		front = front.nxt
		back = back.nxt.nxt
	# now either we are on None (even number of nodes)
	# or on the last object (odd number of nodes) -> then we have a middle node we don't need
	curr = front if back == None else front.nxt
	while curr != None:
		if curr.data != st.pop():
			return False
		curr = curr.nxt
	return True

if __name__ == "__main__":
	node_vals = [1,2,3,2,1,2,1]
	lnklst = LinkedList(node_vals)
	print(is_palindrome_ll(lnklst))

# Test Cases:
# - empty linked list
# - lnklst has one node -> True
# - lnklst has odd # of nodes, > 1 -> True
# - lnklst has odd # of nodes, > 1 -> False
# - lnklst has even # of nodes, > 0 -> True
# - lnklst has even # of nodes, > 0 -> False
