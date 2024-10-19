import numpy as np

# Create/Define single dimension / multi-dimension arrays, and arrays with specific values like array of all ones, all zeros, array with random values within a range, or a diagonal matrix.
# Single Dimensional
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Multi Dimensional
arr_4d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#Array of ones
arr_ones = np.ones((3, 3))
# Arrays of zeros
arr_zeros = np.zeros((3, 3))
# Array with random values arr_rand = np.random.rand(3, 3)
# Diagonal Matrix
arr_diag = np.diag([1, 2, 3, 4])
print(arr_1d)
print(arr_4d)
print(arr_ones)
print(arr_diag)
