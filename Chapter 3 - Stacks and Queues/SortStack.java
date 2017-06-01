/** 3.5 Sort Stack

Write a program to sort a stack such that the smallest items are on the top.
The stack supports the following operations: push, pop, peek, and isEmpty.

Idea:
If the item being pushed is not the smallest item, pop items into a temp stack
until we find the place where the item belongs. Then push everything from temp
stack back onto main stack, maintaining decreasing order of nodes.

**/
public class SortStack {

	public static Stack<Integer> sortStack(Stack<Integer> st) {
		Stack<Integer> secondaryStack = new Stack<Integer>();
		int counter = 0;

		while (!st.isEmpty()) {
			Integer toInsert = st.pop();
			while (!secondaryStack.isEmpty() && secondaryStack.peek() < toInsert) {
				st.push(secondaryStack.pop());
				counter++;
			}
			secondaryStack.push(toInsert);
			while (counter > 0) {
				secondaryStack.push(st.pop());
				counter--;
			}
		}
		return secondaryStack;
		
	}

	public static void main(String[] args) {
		Stack<Integer> inputStack = new Stack<Integer>();
		inputStack.push(2);
		inputStack.push(3);
		inputStack.push(1);
		inputStack.push(4);
		inputStack.push(5);
		Stack<Integer> st = sortStack(inputStack);
		System.out.println(st.pop()); //1
		System.out.println(st.pop()); //2
		System.out.println(st.pop()); //3
		System.out.println(st.pop()); //4
		System.out.println(st.pop()); //5
		System.out.println(st.pop()); //Exception
	}
}