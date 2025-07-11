import numpy as np
from scipy.integrate import quad

# Parametric equations of the helix
# x = cos(t), y = sin(t), z = t, 0 <= t <= pi

def integrand(t):
    x = np.cos(t)
    y = np.sin(t)
    z = t
    return (x * y + z**3) * np.sqrt(2)  # ds = |r'(t)| dt = sqrt(2) dt

# Integration limits
t_start = 0
t_end = np.pi

# Perform the integral
result, error = quad(integrand, t_start, t_end)

print(f"Line integral result: {result:.6f}")