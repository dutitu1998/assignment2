import scipy.integrate as spi
import numpy as np

# Define the function for surface area element
def f(x,y):
    return 2 / np.sqrt(4 - x**2)

# Integration limits
x_lower, x_upper = 0, 1
y_lower, y_upper = 0, 4

# Compute the integral
result, error = spi.dblquad(f, y_lower, y_upper, lambda y: x_lower, lambda y: x_upper)

print("Surface Area:", result)
