/** 2.7 Intersection

Given two singly linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value.

Thoughts:
- Find length (m) of shorter linked list and start from m-th last node in each. Check if they intersect.

Runtime: O(m + n)
Space Complexity: O(1)
**/

public class Intersection {
	
	public static boolean doesIntersect(SinglyLinkedList m, SinglyLinkedList n) {
		int mLength = m.getLength();
		int nLength = n.getLength();
		int diff = (mLength >= nLength) ? mLength - nLength : nLength - mLength;

		Node longer = (mLength >= nLength) ? m.head : n.head;
		Node shorter = (mLength >= nLength) ? n.head : m.head;

		while (diff > 0) {
			longer = longer.next;
			diff--;
		}

		while (longer != null) {
			if (longer == shorter) return true;
			longer = longer.next;
			shorter = shorter.next;
		}
		return false;
	}

	public static void main(String[] args) {
		int[] m = new int[]{0,1,2,3,4};
		int[] n = new int[]{7,8,9,10};
		SinglyLinkedList lnklst1 = new SinglyLinkedList(m);
		SinglyLinkedList lnklst2 = new SinglyLinkedList(n);
		Node curr = lnklst1.head;
		while (curr.next != null) {
			curr = curr.next;
		}
		curr.next = lnklst2.head;
		System.out.println(doesIntersect(lnklst1, lnklst2));
	}
}

/** Test Cases:
- empty linked lists
- same length linked list -> True
- same length linked list -> False
- different length linked list -> True
- different length linked list -> False
**/

