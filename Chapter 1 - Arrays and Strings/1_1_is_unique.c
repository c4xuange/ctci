#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//1.1: Is Unique

//Determine if a string has all unique characters

//Runtime: O(n^2)
//Space-complexity: O(1)
int is_unique_brute(char* s) {
	int length = strlen(s);
	for (int i = 0; i < length - 1; i ++) {
		for (int j = i+1; j < length; j++) {
			if (s[i] == s[j]) return 0;
		}
	}
	return 1;
}

//Use hashtable
//Consider mixed cases -> convert to lowercase
//Runtime: O(n)
//Space-complexity: O(1)
int is_unique(char * s) {
	int ascii[122] = {0};
	int length = strlen(s);

	for (int i = 0; i < length; i++) {
		//check for uppercases
		if (s[i] < 97) {
			s[i] = s[i] + 32;
		}
		if (ascii[s[i]] == 1) return 0;
		else ascii[s[i]] = 1;
	}
	return 1;
}

//NOTE: if no data structures allowed, consider sorting before checking

int main(int argc, char* argv[]) {
	char* s = argv[1];
	if (is_unique(s)) printf("Unique");
	else printf("Not unique");
}