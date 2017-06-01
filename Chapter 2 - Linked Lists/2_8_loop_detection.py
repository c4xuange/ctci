# 2.8 Loop Detection

# Given a circular linked list, return the node at the beginning of the loop

# Thoughts:
# - circular linked list never ends so if we have fast/slow runner, they will meet
# - when they meet, we find the front of the cycle by moving one runner to front and
# - incrementing until they meet again
# Source: http://umairsaeed.com/blog/2011/06/23/finding-the-start-of-a-loop-in-a-circular-linked-list/

from linked_list import LinkedList

def find_circular_head(lnklst):
	fast = slow = lnklst.head
	fast = fast.nxt.nxt
	slow = slow.nxt
	while fast != slow:
		fast = fast.nxt.nxt
		slow = slow.nxt
	slow = lnklst.head
	while slow != fast:
		slow, fast = slow.nxt, fast.nxt
	return slow

if __name__ == "__main__":
	vals = [1,2,3,4,5,5,6]
	lnklst = LinkedList(vals)
	curr = lnklst.head
	while curr.nxt != None:
		curr = curr.nxt
	cycle_head = lnklst.head.nxt.nxt.nxt
	print("expecting:" + str(cycle_head))
	curr.nxt = cycle_head
	print("actual: " + str(find_circular_head(lnklst)))

# Test cases:
# 1 -> 2 -> 3 -> 4 -> 5 -> 1 : 1
# 1 -> 2 -> 3 -> 4 -> 5 -> 3 : 3
# 1 -> 2 -> 3 -> 4 -> 5 -> 5 : 5
# 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 4 : 4
