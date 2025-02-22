import numpy as np
from scipy.integrate import dblquad

# Define the integrand
def integrand(y, x):
    return 3 * (x**2 + y**2)

# Perform the double integral over the unit circle
result, _ = dblquad(integrand, -1, 1, lambda x: -np.sqrt(1 - x**2), lambda x: np.sqrt(1 - x**2))

print("Work done by the force field:", result)