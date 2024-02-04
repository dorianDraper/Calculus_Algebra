import numpy as np

# vector of 10 ones
a1 = np.ones(10)
print(a1)
# Vector of 10 numbers that have the same distance from each other, starting with 3 and ending with 15
a2 = np.linspace(3, 15, 10)
print(a2)
# Vector of 10 random numbers between [0, 1]
a3 = np.random.rand(10)
print(a3)
# Vector of 10 random numbers between [0, 10]
a4 = np.random.randint(0, 10, size=10)
print(a4)
print(' ')
print('*'*30)
# Matrices
# 5x5 identity matrix
m1 = np.eye(5)
print(m1)
# 3x2 matrix of random numbers between [0, 1]
m2 = np.random.rand(3, 2)
print(m2)
# 7x5 matrix of random numbers between [5, 19]
m3 = np.random.randint(5, 19, size=(7, 5))
print(m3)
# Vectors
# Scalar operations
# add scalar and a vector (add 2 to each element of the vector)
a1 = np.array([1, 2, 3, 4, 5])
print(a1 + 2)
# subtract scalar from a vector (subtract 1 from each element of the vector)
print(a1 - 1)
# multiply scalar and a vector (multiply each element of the vector by 10)
print(a1 * 10)
# divide vector by a scalar (divide each element of the vector by 5)
print(a1 / 5)
# vector multiplication
# dot product of two vectors
a1 = np.array([1, 2, 3, 4])
a2 = np.linspace(0, 20, 4)
print(np.dot(a1, a2))
# hadamard product of two vectors
a1 = np.array([1, 2, 3, 4])
a2 = np.array([10, 10, 10, 10])
print(a1 * a2)
# Matrices
# Add a scalar and a matrix (in this case of 2 rows and 4 columns)
m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(m1 + 10)
# Subtract a scalar and a matrix
print(m1 - 5)
# Multiplying a scalar and a matrix
print(m1 * 3)
# Divide a matrix by a scalar
print(m1 / 2)
print(' ')
print('*'*30)
m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
m2 = np.array([[2, 4, 6, 8], [-1, -2, -3, -4]])
# add two matrices
print(m1 + m2) # elements of first matrix are added to the elements of the second matrix together
# subtract two matrices
print(m1 - m2) 
# divide two matrices
print(m1 / m2)
print(' ')
print('*'*30)
# matrix multiplication
m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
m2 = np.array([[2, 4], [6, 8], [-1, -2], [-3, -4]])
print(m1)
print(m2)
print(np.dot(m1, m2)) # or m1.dot(m2)
print(' ')
print('*'*30)
# hadamard product of two matrices
m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
m2 = np.array([[2, 4, 6, 8], [-1, -2, -3, -4]])
print(m1 * m2)
print(' ')
print('*'*30)
# Transpose of a matrix 
m1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(m1)
print(m1.T) # or np.transpose(m1)


