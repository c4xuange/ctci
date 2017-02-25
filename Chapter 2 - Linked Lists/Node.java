public class Node {
	Node next = null;
	Integer data;

	public Node(int d) {
		data = new Integer(d);
	}

	// void appendToTail(int d) {
	// 	Node end = new Node(d);
	// 	Node curr = this;
	// 	while (curr.next != null) {
	// 		curr = curr.next;
	// 	}
	// 	curr.next = end;
	// }
}
