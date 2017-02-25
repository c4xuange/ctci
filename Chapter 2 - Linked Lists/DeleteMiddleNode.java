/** 2.3 Delete Middle Node

Delete a node in the middle (i.e. not first or last) of a singly linked list
given only access to that node

Example:
INPUT: a -> b -> c -> d -> e -> f
RESULT: nothing returned, but linked list is now a -> b -> d -> e -> f

Thoughts:
- replace each node's value with the value of the next node

Runtime: O(1)
**/

class DeleteMiddleNode {
	public static void deleteMiddleNode(Node node) {
		Node curr = node;
		if (curr == null || curr.next == null) return;
		/** Original implementation, has to copy each node over
			while (curr.next != null) {
				curr.data = curr.next.data;
				if (curr.next.next != null)
					curr = curr.next;
				else curr.next = null;
			}
		**/

		//Another idea: simply replace current node with next and delete next
		Node next = curr.next;
		curr.data = next.data;
		curr.next = next.next;
	}

	public static void main(String[] args) {
		int[] values = {1,2,3,4,5,6};
		SinglyLinkedList lnklst = new SinglyLinkedList(values);
		int val = Integer.parseInt(args[0]);
		Node curr = lnklst.head;
		while (curr.data != val) {
			curr = curr.next;
		}
		deleteMiddleNode(curr);
		lnklst.printLinkedList();
	}
}