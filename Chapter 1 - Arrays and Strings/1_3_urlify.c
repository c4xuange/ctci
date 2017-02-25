#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//1.3: URLify

//Replace all spaces in a string with '%20'
//Assume string has sufficient space to hold the additional characters
//and you are gien the "true" length of the string

//Input: "Mr John Smith    ", 13
//Output:"Mr%20John%20Smith"

void urlify(char *S, int true_len) {
	printf("%s", S);
	int i = strlen(S) - 1;
	int j = true_len - 1;
	while (i >= 0) {
		if (S[j] != ' ') {
			S[i] = S[j];
			i--;j--;
		} else {
			S[i] = '0';
			S[i-1] = '2';
			S[i-2] = '%';
			// strcpy(&S[i-2], "%20");
			i = i-3;
			j--;
		}
	}
}

int main(int argc, char* argv[]) {
	char* s = argv[2];
	char S[strlen(s)];
	// for (int i =0; i < strlen(s); i++) {
	// 	S[i] = s[i];
	// }
	// S[strlen(s)] = '\0';
	strcpy(S, s);
	// char S[] = "Lady Mary Crawley    ";
	int len = atoi(argv[1]);
	urlify(S, len);
	printf("%s\n", S);
	return 0;
}