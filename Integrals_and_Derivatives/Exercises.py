import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Consider the function f(x) = x + 1  and g(x) x**2 + 1
# def f(x):
#     return x + 1

# def g(x):  
#     return x**2 + 1

# x = np.linspace(-2, 2, 100)

# plt.plot(x, f(x), label='f(x) = x + 1')
# plt.plot(x, g(x), label='g(x) = x**2 + 1')
# plt.plot(0,f(0), 'ro') # plot the point (0, f(0))
# plt.plot(1,g(1), 'ro') # plot the point (1, g(1))
# plt.legend()
# plt.show()

# # Consider function f(x)=x**2 + 3 
# def f(x):
#     return x**2 + 3

# # what is the slope between (1,4) and (3,12) with the function f(x) = x**2 + 3
# x1 = 1
# x2 = 3
# y1 = f(x1)
# y2 = f(x2)
# slope = (y2 - y1) / (x2 - x1)
# print(slope)

# # plot the above function and the line between (1,4) and (3,12)
# x = np.linspace(-2, 4, 100)
# plt.plot(x, f(x), label='f(x) = x**2 + 3')
# plt.plot([x1, x2], [y1, y2], 'ro-') # plot the line between (1,4) and (3,12)
# plt.legend()
# plt.show()

# Consider the function f(x) = x**2 - 2*x + 1, get the derivative of the function
# def f(x):
#     return x**2 - 2*x + 1 # (x - 1)**2

# # get the derivative of the function
# def df(x):
#     return 2*x - 2

# # plot the function and its derivative
# x = np.linspace(-2, 4, 100)
# plt.plot(x, f(x), label='f(x) = x**2 - 2*x + 1')
# plt.plot(x, df(x), label="f'(x) = 2*x - 2")
# plt.legend()
# plt.show()