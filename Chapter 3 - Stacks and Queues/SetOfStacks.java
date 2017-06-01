/** 3.3 Stack of Plates
	
Implement a data structure SetOfStacks that is composed of several stacks and should create
a new stack once the previous one exceeds capacity. SetOfStacks.push() and .pop() should
behave identically to a single stack.

Follow up: Implement a function popAt(int index) which performs a pop operation on a 
specific sub-stack.

Thoughts:
- Stack of stacks, continuously push onto and pop from top stack
- Once top stack full, push new empty stack
- Once top stack empty, pop it
- popAt: pop into another stack until we reach desired substack, then pop back
**/
import java.util.EmptyStackException;

public class SetOfStacks<T> {
	Stack<Stack<T>> set = new Stack<Stack<T>>();
	int curr_size = 0;
	int capacity;
	
	public SetOfStacks(int c) {
		this.capacity = c;
	}

	public void push(T item) {
		// if first stack or need a new stack
		Stack<T> curr_stack = (curr_size == capacity || set.isEmpty()) ? new Stack<T>():set.pop();
		curr_stack.push(item);
		curr_size = (curr_size == capacity) ? 1: curr_size + 1;
		set.push(curr_stack);
	}

	public T pop() {
		if (set.isEmpty()) throw new EmptyStackException();
		Stack<T> top = set.pop();
		T item = top.pop();
		if (!top.isEmpty()) {
			set.push(top);
			curr_size--;
		} else {
			System.out.println("Back to previous stack");
			curr_size = capacity;
		}
		return item;
	}

	public T peek() {
		if (set.isEmpty()) throw new EmptyStackException();
		Stack<T> top = set.pop();
		T item = top.peek();
		set.push(top);
		return item;
	}

	public boolean isEmpty() {
		return set.isEmpty();
	}

	/** Follow-up:
		- need Stacks to keep track of their own size, decrement size of indexStack
		- Assume zero-based indexing
	**/
	// public T popAt(int index) {
	// 	Stack<Stack<T>> temp_stack = new Stack<Stack<T>>();
	// 	for (int i = 0; i <= index; i++) {
	// 		if (set.isEmpty()) throw new EmptyStackException();
	// 		temp_stack.push(set.pop());
	// 	}
	// 	Stack<T> indexStack = temp_stack.pop();
	// 	T item = indexStack.pop();
	// 	set.push(indexStack);
	// 	while (!temp_stack.isEmpty()) {
	// 		set.push(temp_stack.pop());
	// 	}
	// 	return item;
	// }

	public static void main(String args[]) {
		SetOfStacks<Integer> test = new SetOfStacks<Integer>(3);
		test.push(5);
		test.push(4);
		test.push(3);
		test.push(2);
		test.push(1);
		System.out.println(test.peek()); //1
		test.pop();
		System.out.println(test.peek()); //2
		test.pop(); // Back to previous stack
		System.out.println(test.peek()); //3
		System.out.println(test.isEmpty()); //false
		test.pop();
		test.pop();
		test.pop(); // Back to previous stack
		System.out.println(test.peek()); //EmptyStackException
	}
}