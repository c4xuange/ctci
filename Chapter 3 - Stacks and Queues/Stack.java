import java.util.EmptyStackException;

public class Stack<T> {
	private Node<T> top;

	public T pop() {
		if (top == null) throw new EmptyStackException();
		else {
			T temp = top.data;
			top = top.nxt;
			return temp;
		}
	}

	public void push(T item) {
		Node<T> node = new Node<T>(item);
		node.nxt = top;
		top = node;
	}

	public T peek() {
		if (top == null) throw new EmptyStackException();
		return top.data;
	}

	public boolean isEmpty() {
		return (top == null);
	}
}