import scipy.integrate as spi
import numpy as np

# Define the volume integrand
def f(r, theta):
    return (3 - r**2 - 2*r*np.cos(theta)) * r

# Integration limits
r_lower, r_upper = 0, 1
theta_lower, theta_upper = 0, 2*np.pi

# Compute the double integral
result, error = spi.dblquad(f, theta_lower, theta_upper, lambda theta: r_lower, lambda theta: r_upper)

# Print result
print("Volume of the solid:", result)
