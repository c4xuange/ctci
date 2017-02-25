#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//1.2: Is Permutation

//Given two strings, determine if they are permutations of each other

//Alternate solution: sort both strings (O(nlogn)) and compare

//Runtime: O(N + M)
//Check each letter in str1 (N) and str2 (M)
//Checking alphabet runs in constant time
int is_permutation(char str1[], char str2[]) {
	if (strlen(str1) != strlen(str2)) return 0;
	int len = strlen(str1);
	int alphabet[26] = {0};
	for (int i = 0; i < len; i++) {
		int ch = str1[i] - 'a';
		alphabet[ch]++;
	}
	for (int j = 0; j < len; j++) {
		int ch = str2[j] - 'a';
		alphabet[ch]--;
	}

	for (int k = 0; k < 26; k++) {
		if (alphabet[k] != 0) return 0;
	}
	return 1;
}

int main(int argc, char* argv[]) {
	char* s1 = argv[1];
	char* s2 = argv[2];
	int is_perm;
	if ((is_perm = is_permutation(s1,s2)) == 0) {
		printf("No\n");
	} else printf("Yes\n");
	
	return 0;
}