#2.2 Return Kth to Last

#Implement an algorithm to find the kth to last element in a singly linked list

#Plan: if length of linkedlist is n, the desired node is at position n-k
#	- have two pointers, one at position k and one at beginning
#	- when pointer at pos k reaches end, second pointer reaches position n-k

#Recursive option: base case -> 0, each layer -> 1 + result from recursive call until we get k

#Runtime: O(N)

from linked_list import LinkedList

#only one iteration required
def find_kth_last(lnklst, k):
	p1 = lnklst.head
	for i in range(1, k):
		if p1.nxt == None:
			return None
		else:
			p1 = p1.nxt
	p2 = lnklst.head
	while p1.nxt != None:
		p1, p2 = p1.nxt, p2.nxt
	return p2

#original implementation
def find_kth_last_alternate(lnklst, k):
	if k <= 0:
		return None
	counter = 0
	curr = lnklst.head
	while curr != None:
		counter += 1
		curr = curr.nxt
	if k > counter:
		return None
	kth_last_distance = counter - k
	curr = lnklst.head
	while kth_last_distance > 0:
		curr = curr.nxt
		kth_last_distance -= 1
	return curr

if __name__ == "__main__":
	lnklst = LinkedList([1,2,3,4,5,6])
	node = find_kth_last(lnklst, 3)
	print(node)



