# 2.4 Partition

# Partition a linked list around a value x, such that all nodes < x come before all 
# nodes >= x. If x is contained within the list, the values of x only need to be
# after the elements < x. The partition element x can appear anywhere in the "right
# partition"; it doesn't need to appear betwen the left and right partitions.

#INPUT: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, partition = 5
#OUTPUT: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

#Idea: Each node with value < x gets moved to the head of the linked list

from linked_list import LinkedList
import sys

def partition(lnklst, val):
	curr = lnklst.head
	while curr.nxt != None:
		if curr.nxt.data < val:
			next = curr.nxt.nxt
			curr.nxt.nxt = lnklst.head
			lnklst.head = curr.nxt
			curr.nxt = next
		else:
			curr = curr.nxt

if __name__ == "__main__":
	lnklst = LinkedList([3,5,8,5,10,2,1])
	val = int(sys.argv[1])
	partition(lnklst, val)
	print(lnklst)