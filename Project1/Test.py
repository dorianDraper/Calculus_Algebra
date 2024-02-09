import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# we have two matrices
matrix1 = [[1,7,3],
 [ 4,5,2],
 [ 3,6,1]]

matrix2 = [[5,4,1],
 [ 1,2,3],
 [ 4,5,2]]
# using for loop input the two matrices of size n x m using dot product
result = [[0,0,0],
 [0,0,0],
 [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print(result)

# using numpy to add the matrices

print('-------------------')
# using numpy and dot product to multiply the matrices
result = np.dot(matrix1, matrix2)
print(result)  