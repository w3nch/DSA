matrix = [
    [1, 2, 3],  # row 0
    [4, 5, 6],  # row 1
    [7, 8, 9],  # row 2
]

matrix_len = len(matrix)
matrix_row_sum = 0

"""Sum of a specific row (example: first row)"""
# matrix_row_sum = 0
# for i in range(matrix_len):
#     matrix_row_sum += matrix[0][i]  # sum of first row
# print(matrix_row_sum)  # Output: 6

"""Find the Main Diagonal Sum"""
# matrix_row_sum = 0
# for i in range(matrix_len):
#     matrix_row_sum += matrix[i][i]
# print(matrix_row_sum)  # Output: 15

"""Secondary Diagonal Sum"""
# matrix_row_sum = 0
# for i in range(matrix_len):
#     matrix_row_sum += matrix[i][matrix_len - 1 - i]
# print(matrix_row_sum)  # Output: 15

"""Sum of Border Elements"""
# matrix_row_sum = 0
# n = matrix_len
# # Sum first row
# matrix_row_sum += sum(matrix[0])
# # Sum last row
# matrix_row_sum += sum(matrix[n-1])
# # Sum first and last elements of middle rows
# for i in range(1, n-1):
#     matrix_row_sum += matrix[i][0] + matrix[i][n-1]
# print(matrix_row_sum)  # Output: 40

"""Transpose of a Matrix"""
# transpose = [[0]*matrix_len for _ in range(matrix_len)]
# for i in range(matrix_len):
#     for j in range(matrix_len):
#         transpose[j][i] = matrix[i][j]
# print(transpose)
# Output:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]