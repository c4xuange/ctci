#1.9 - String Rotation

#Assume you have method isSubstring which checks if one word is a substring of another.
#Given two strings ,s1 and s2, write code to check if s2 is a rotation of s1 using only
#one call to isSubstring

#Example: "waterbottle" = rotation of "erbottlewat"

#Thoughts:
# - if rotation, must have same length
# - rotation iff original string is in concatentation of other string with itself
#	i.e. "waterbottle" is in "erbottlewaterbottlewat"

#Runtime: O(N), assuming is_substring runs in time O(A+B)
def is_substring(s1, s2):
	"""Checks if s1 is substring of s2"""
	return s1 in s2

def is_rotation(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		s2 += s2
		return isSubstring(s1, s2)

if __name__ == "__main__":
	import sys
	print(is_rotation(sys.argv[1], sys.argv[2]))
