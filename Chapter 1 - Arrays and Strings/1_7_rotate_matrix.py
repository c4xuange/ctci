#1.7 Rotate Matrix

#Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
#write a method to rotate the image by 90 degrees. Can you do this in place?

#Thoughts:
# 1 2 3    6 4 1
# 4 x 5 => 7 x 2
# 6 7 8    8 5 3

# Number of layers (outer border) = N/2, treat each layer separately

def rotate_matrix(matrix):
	n = len(matrix); #number of rows
	for layer in range(0,n//2):
		first = layer
		last = n - layer - 1
		for i in range(first, last):
			offset = i - first
			# store top edge value in this layer
			temp = matrix[first][i]
			# left edge value to top edge
			matrix[first][i] = matrix[last-offset][first]
			# bottom to left
			matrix[last-offset][first] = matrix[last][last-offset]
			# right to bottom
			matrix[last][last-offset] = matrix[i][last]
			# temp to right
			matrix[i][last] = temp

if __name__ == "__main__":
	matrix = [[1,2],[3,4]]
	matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
	matrix2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
	rotate_matrix(matrix2)
	for row in range(0,len(matrix2)):
		for column in range(0,len(matrix2)):
			print(matrix2[row][column])