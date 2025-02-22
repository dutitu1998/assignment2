import scipy.integrate as spi
import numpy as np

# Define the function to integrate
def f(x, y, z):
    return x * np.exp(-y) * np.cos(z)

# Define integration limits
x_lower, x_upper = 0, 1
def y_lower(x): return 0
def y_upper(x): return 1 - x**2
def z_lower(x, y): return 3
def z_upper(x, y): return 4 - x**2 - y**2

# Perform triple integration
result, error = spi.tplquad(f, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper)

print("Triple Integral Result:", result)
#6(a)(ii)
import scipy.integrate as spi
import numpy as np

# Define the function to integrate
def f(x,y):  # scipy expects inner variable first
    return (x * y) / np.sqrt(x**2 + y**2 + 1)

# Integration limits
x_lower, x_upper = 0, 1
y_lower, y_upper = 0, 1

# Compute the integral
result, error = spi.dblquad(f, x_lower, x_upper, lambda x: y_lower, lambda x: y_upper)

print("Double Integral Result:", result)

