# https://leetcode.com/problems/rotate-image/
# 48. Rotate Image 

"""
First transpose the matrix (note how inner j loop starts from i),
then reverse the rows. 

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                tmp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp 

        for i in range(len(matrix)):
            l, r = 0, len(matrix) -1
            while (l <= r):
                matrix[i][l], matrix[i][r] =  matrix[i][r], matrix[i][l] 
                l += 1
                r -= 1
