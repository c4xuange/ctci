/** 1.6 String Compression

Implement a method to perform basic string compression using the counts of repeated characters.
If the "compressed" string would not become smaller than the original string, return the original string.
Assume the string has only uppercase and lowercase letters (a-z).

Input: aabcccccaaa
Output: a2b1c5a3
**/

public class StringCompression{
	public static String compressString(String s) {
		Integer counter = 1;
		int i;
		String new_str = "";
		char curr = s.charAt(0);
		for (i = 1; i < s.length(); i++) {
			if (s.charAt(i) == curr) counter++;
			else {
				new_str += curr + counter.toString();
				curr = s.charAt(i);
				counter = 1;
			}
		}
		new_str += curr + counter.toString();

		return new_str.length() >= s.length() ? s:new_str;
	}

	public static void main(String[] args) {
		String result = compressString(args[0]);
		System.out.println(result);
	}
}