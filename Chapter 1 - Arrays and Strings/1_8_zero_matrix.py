#1.8 Zero Matrix

#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

#Thoughts:
# - Can't change on spot otherwise added 0's will affect other rows and columns
# - Keep track of which rows and columns have 0's in them and change them after iterating through matrix

#Runtime: O(MN)
#Space Complexity: O(M+N)
# - Space can be reduced to O(1) if we keep track of which rows to be set by putting zeros in the first column 
#	of the matrix, and which columns to be set using the first row of the matrix

def zero_matrix(matrix):
	rows_to_set = set()
	cols_to_set = set()
	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[0])):
			if matrix[row][col] == 0:
				rows_to_set.add(row)
				cols_to_set.add(col)
	for row in range(0, len(matrix)):
		if row in rows_to_set:
			matrix[row] = [0]*len(matrix[0])
		else:
			for col in cols_to_set:
				matrix[row][col] = 0
	print_matrix(matrix)

def print_matrix(matrix):
	for row in range(0,len(matrix)):
		for column in range(0,len(matrix)):
			print(matrix[row][column])

if __name__ == "__main__":
	matrix = [[1,0],[3,4]]
	matrix1 = [[1,2,3], [4,0,5], [6,7,8]]
	zero_matrix(matrix1)

