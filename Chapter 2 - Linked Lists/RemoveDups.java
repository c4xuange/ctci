/** 2.1 Remove Dups

Write code to remove duplicates from a unsorted linked list.
Follow up: How would you solve this problem if a temporary buffer is not allowed?

Input: 1 -> 1 -> 2 -> 3 -> 2 -> null
Output: 1 -> 2 -> 3 -> null
**/

import java.util.Hashtable;

public class RemoveDups {
	public static void removeDups(Node head) {
		Hashtable<Integer,Boolean> seen = new Hashtable<Integer,Boolean>();
		Node curr = head;
		seen.put(curr.data, true);
		while (curr.next != null && curr.next.next != null) {
			if (seen.containsKey(curr.next.data)) {
				curr.next = curr.next.next;
			} else {
				curr = curr.next;
				seen.put(curr.data, true);
			}
		} if (curr.next == null) {
			//only one node in the linked list, no duplicates
		} else {
			//on second last node
			if (seen.containsKey(curr.next.data)) {
				curr.next = null;
			}
		}
	}

	public static void main(String args[]) {
		int[] values = {6,7,2,5,1,6,2,2,5,5,3,3,1,4,9,0,8};
		SinglyLinkedList lnklst = new SinglyLinkedList(values);
		removeDups(lnklst.head);
		lnklst.printLinkedList();
	}
}