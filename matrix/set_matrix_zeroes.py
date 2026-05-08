"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
response = [[0] * len(matrix[0])] * len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            print('changement')
            for k in range(len(matrix[i])):
                if matrix[i][k] != 0:
                    matrix[i][k] = 'a'
            for k in range(len(matrix)):
                if matrix[k][j] != 0:
                    matrix[k][j] = 'a'
            print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'a':
            matrix[i][j] = 0

print(matrix)