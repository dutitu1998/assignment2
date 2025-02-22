import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable and the vector function
t = sp.symbols('t')
r = sp.Matrix([3 * t, sp.sin(t), t**2])

# Compute the velocity and acceleration
v = r.diff(t)  # Velocity
a = v.diff(t)  # Acceleration

# Compute theta(t), the angle between v(t) and a(t)
dot_product = v.dot(a)
magnitude_v = sp.sqrt(v.dot(v))
magnitude_a = sp.sqrt(a.dot(a))
cos_theta = dot_product / (magnitude_v * magnitude_a)
theta = sp.acos(cos_theta)

# Convert theta(t) to a numerical function for plotting
theta_func = sp.lambdify(t, theta, "numpy")

# Generate data for plotting
t_vals = np.linspace(0.1, 10, 500)  # Avoid t=0 to prevent division by zero
theta_vals = theta_func(t_vals)

# Plot theta(t) versus t
plt.figure(figsize=(8, 5))
plt.plot(t_vals, theta_vals, label=r'$\theta(t)$', color='blue')
plt.title(r'Graph of $\theta(t)$ versus $t$', fontsize=14)
plt.xlabel(r'$t$', fontsize=12)
plt.ylabel(r'$\theta(t)$ (radians)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
print(a)
print(v)