"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
output: [1,2,3,6,9,8,7,4,5]
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def spiral_order(matrix):
    top, right, left, bottom = 0, 0, 0, 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    result = []
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top+=1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        
        right -= 1
        if bottom >= top:
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result
          
# spiral_order(matrix)
print(spiral_order([[4,3,2,1]]))
print('hey')
print(spiral_order([[1],[2],[3],[4]]))
print(spiral_order(matrix))