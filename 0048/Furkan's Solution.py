class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):                                                        # For each row
            for j in range(i+1,n):                                                # For every pixel except middle diagonal pixels
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]           # Swap the top and bottom of the diagonal imaginary line
        
        for i in range(n):                                                        # For each row
            for j in range(n//2):                                                 # For half of matrix
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]   # Swap the left and right side of the middle vertical imaginary line
