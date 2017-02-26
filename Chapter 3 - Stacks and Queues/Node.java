public class Node<T> {
	T data;
	Node<T> nxt = null;

	public Node(T val) {
		this.data = val;
	}

	// public void print() {
	// 	Node curr = this;
	// 	while (curr != null) {
	// 		System.out.println(curr.data.toString());
	// 		curr = curr.nxt;
	// 	}
	// }

}

