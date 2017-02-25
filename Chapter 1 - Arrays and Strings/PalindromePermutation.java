//1.4: Palindrome Permutation

//Given a string, write a function to check if it is a 
//permuation of a palindrome.

//Input: "Tact Coa"
//Output: True ("taco cat", "atcocta")

//Idea: to be a palindrome, each char needs to either be the middle
//charor be repeated somewhere else in the string
public class PalindromePermutation {
	public static boolean isPalPerm(String s) {
		int ch, counter, i;
		int[] alphabet;
		alphabet = new int[128];

		// \\s = single whitespace, \\s+ refers to one or more whitespaces
		s = s.toLowerCase().replaceAll("\\s+","");
		for (ch = 0; ch < s.length(); ch ++) {
			int index = (int) s.charAt(ch);
			if (alphabet[index] == 0) alphabet[index] ++;
			//each time a matching char is found, we cancel it out
			else alphabet[index] --;
		}

		//All chars must be canceled out unless there is one middle char (odd length string)
		counter = i = 0;
		while (i < 128 && counter <= 1) {
			counter += alphabet[i];
			i++;
		}
		if (counter > 1) {
			return false;
		}
		return true;
	}

	public static void main(String args[]) {
		boolean result = isPalPerm(args[0]);
		System.out.println(result);
	}
}