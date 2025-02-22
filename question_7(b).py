import numpy as np
from scipy.integrate import quad

def integrand(t):
    xy = (np.cos(t) * np.sin(t))  # xy = (cos t)(sin t) = (1/2) sin(2t)
    z3 = t**3                    # z^3 = t^3
    f_t = xy + z3
    ds_dt = np.sqrt(2)           # ds = sqrt(2) dt
    return f_t * ds_dt

# Define integration limits
t0, t1 = 0, np.pi

# Compute the integral
result, error = quad(integrand, t0, t1)

print(f"The value of the line integral is: {result}")
