import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y = sp.symbols('x y', real=True)
T = 3 * x**2 * y

grad_T_expr = sp.Matrix([T.diff(x), T.diff(y)])

# Define the point
x_val = -1
y_val = 3/2
grad_T_at_point = grad_T_expr.subs([(x, x_val), (y, y_val)])

# Define the direction
direction_vector = sp.Matrix([-1, -1/2])
unit_direction = direction_vector / direction_vector.norm()

# Directional derivative =V.(nebla(F(P)))
directional_derivative_expr = grad_T_expr.dot(unit_direction)
directional_derivative_at_point = directional_derivative_expr.subs([(x, x_val), (y, y_val)])

print(f"Gradient of T(x, y) at ({x_val}, {y_val}) is: {grad_T_at_point.T}")
print(f"Directional derivative at ({x_val}, {y_val}) is: {directional_derivative_at_point}")

# Define the correct region for x and y
x_vals = np.linspace(-2, 0, 100)     # from -2 to 0
y_vals = np.linspace(0, 2, 100)      # from 0 to 2
X, Y = np.meshgrid(x_vals, y_vals)   # Create a grid over the domain

# Evaluate directional derivative over the grid

D_func = sp.lambdify((x, y), directional_derivative_expr, 'numpy')
Z_D = D_func(X, Y)

# Plot the directional derivative surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z_D, cmap='viridis', edgecolor='none')

plt.show()
