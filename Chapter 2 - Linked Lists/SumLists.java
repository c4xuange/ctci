/** 2.5 Sum Lists

You have two numbers each represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order. Write a function that adds the two numbers and returns
the sum as a linked list.

INPUT:(7 -> 1 -> 6) + (5 -> 9 -> 2), i.e. 617 + 295
OUTPUT: (2 -> 1 -> 9), i.e. 912
**/
import java.util.List;
import java.util.ArrayList;
import static java.lang.Math.*;

public class SumLists {
	public static Node sumLists(Node l1, Node l2) {
		int carry = 0;
		int sum, digit;
		// dummy node
		Node head = new Node(0);
		Node curr_sum = head;
		while (l1 != null && l2 != null) {
			sum = l1.data + l2.data + carry;
			digit = (sum >= 10) ? sum % 10: sum;
			carry = (sum >= 10) ? 1:0;
			Node curr_node = new Node(digit);
			curr_sum.next = curr_node;
			curr_sum = curr_node;
			l1 = l1.next;
			l2 = l2.next;
		}

		Node curr = (l1 == null) ? l2:l1;
		while (curr != null) {
			sum = curr.data + carry;
			digit = (sum >= 10) ? sum % 10: sum;
			carry = (sum >= 10) ? 1:0;
			Node curr_node = new Node(digit);
			curr_sum.next = curr_node;
			curr_sum = curr_node;
			curr = curr.next;
		}
		if (carry == 1) {
			Node last_node = new Node(1);
			curr_sum.next = last_node;
		}

		return head.next;
	}

	public static int[] convertInteger(int num) {
		// can't take log of 0
		int max_place = (num == 0) ? 0:(int) log10(num)/1;
		max_place++;
		int place = 0;
		int digit;
		int[] converted = new int[max_place];
		while (place < max_place) {
			digit = num % 10;
			converted[place] = digit;
			num = num/10;
			place ++;
		}
		return converted;

	}

	public static void main(String[] args) {
		int num1 = Integer.parseInt(args[0]);
		int num2 = Integer.parseInt(args[1]);
		SinglyLinkedList l1 = new SinglyLinkedList(convertInteger(num1));
		SinglyLinkedList l2 = new SinglyLinkedList(convertInteger(num2));
		Node curr = sumLists(l1.head, l2.head);
		while (curr != null) {
			System.out.println(curr.data.toString());
			curr = curr.next;
		}
	}
}
