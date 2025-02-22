import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
t=sp.symbols('t')
r=sp.Matrix([3*t,sp.sin(t),t**2])
v=sp.diff(r)
a=sp.diff(v)
dot_product=v.dot(a)
magnitude_a=a.dot(a)
magnitude_v=v.dot(v)
cos_theta=dot_product/(magnitude_a*magnitude_v)
angle=sp.acos(cos_theta)
theta_func=sp.lambdify(t,angle,"numpy")
# Generate numerical values for plotting
t_vals = np.linspace(0.1, 10, 500)  # Avoid t=0
theta_vals = theta_func(t_vals)

# Plot theta(t) vs. t
plt.figure(figsize=(8, 5))
plt.plot(t_vals, theta_vals, label=r'$\theta(t)$', color='blue')
plt.title(r'Graph of $\theta(t)$ versus $t$', fontsize=14)
plt.xlabel(r'$t$', fontsize=12)
plt.ylabel(r'$\theta(t)$ (radians)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

# Print symbolic expressions for verification
print("Velocity vector v(t):")
sp.pprint(v)
print("\nAcceleration vector a(t):")
sp.pprint(a)
