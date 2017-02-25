/**1.5 One Away

There are three types of edits that can be performed on a string: insert, remove, or replace a character
Given two strings, write a function to check if they are one (or zero) edits away.

Thoughts:
- lengths of strings can differ by at most one
- inserting character from one string <=> removing character from other string, so we only need to check for two types of edits:
1) If replace, length must be the same
2) Given s1 & s2, of delete from s2, then s2 must have length s1 + 1

Runtime:
O(n) - where n is the length of the shorter string
 - if we have to iterate through both strings, their lengths are only one apart
 - if one string is significantly longer, then we terminate in O(1) time
**/

public class OneEditAway{
	public static boolean isOneAway(String s1, String s2) {
		int counter = 0;
		int i = 0;
		String longer, shorter;
		if (s1.length() == s2.length()) {
			//Check for replace edit
			while (i < s1.length() && counter <= 1) {
				if (s1.charAt(i) != s2.charAt(i)) counter++;
				i++;
			}
			if (counter > 1) return false;
			return true;
		} else if (s1.length() - s2.length() == 1 || s2.length() - s1.length() == 1) {
			int j = 0;
			
			// if (s1.length() > s2.length()) {
			// 	longer = s1;
			// 	shorter = s2;
			// } else {
			// 	longer = s2;
			// 	shorter = s1;
			// }
			longer = s1.length() > s2.length() ? s1 : s2;
			shorter = s1.length() > s2.length() ? s2 : s1;

			while (i < shorter.length() && counter <= 1) {
				if (longer.charAt(i+counter) != shorter.charAt(i)) counter ++;
				else i++;
			}
			if (counter > 1) return false;
			return true;
		} else {
			//lengths of strings differ by more than one
			return false;
		}
	}

	public static void main(String[] args) {
		boolean result = isOneAway(args[0], args[1]);
		System.out.println(result);
	}
}