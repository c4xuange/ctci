public class SinglyLinkedList {
	Node head;

	public SinglyLinkedList(int[] values) {
		int i;
		head = new Node(values[0]);
		Node curr = head;
		for (i=1; i < values.length; i++) {
			curr.next = new Node(values[i]);
			curr = curr.next;
		}
	}

	public void printLinkedList() {
		Node curr = head;
		while (curr != null) {
			System.out.println(curr.data);
			curr = curr.next;
		}
	}
}