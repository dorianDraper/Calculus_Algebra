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
