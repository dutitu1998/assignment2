import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')

r1 = sp.Matrix([2*sp.cos(t), 3*sp.sin(t), 0])
dr = r1.diff(t)
T = dr / sp.sqrt(dr.dot(dr))
dT = T.diff(t)
N = dT / sp.sqrt(dT.dot(dT))
B = T.cross(N)
K = dT.norm() / sp.sqrt(dr.dot(dr))

# Create values for plotting
t_vals = np.linspace(0, 2*np.pi, 100)
K_func = sp.lambdify(t, K, modules='numpy')
K_vals = K_func(t_vals)

# Plot curvature
plt.figure(figsize=(8, 6))
plt.plot(t_vals, K_vals)    
plt.title('Curvature vs Parameter t')
plt.xlabel('t')
plt.ylabel('Curvature K')
plt.grid(True)
plt.show()

# Laplace equation and cauchy
x, y = sp.symbols(['x','y'])
f = (y**2)*sp.cos(x-y)
if f.diff(x,2) + f.diff(y,2) == 0:
    print('Laplace Equation is satisfied')
else:
    print('Laplace Equation is not satisfied')

# Mixed partial derivatives
f_xy = f.diff(x).diff(y)
f_yx = f.diff(y).diff(x)

mixed_partials_equal = sp.simplify(f_xy - f_yx) == 0
print(f"Are the mixed partial derivatives equal? {mixed_partials_equal}")

# chain rule
t = sp.symbols('t')
x, y, z , w= sp.symbols(['x', 'y', 'z', 'w'], cls=sp.Function)
x = sp.cos(t)
y = sp.sin(t)
z = sp.tan(t)
w = sp.sqrt(x**2 + y**2 + z**2)

dw_dt = w.diff(t)
print(f"Using the chain rule, the answer at theta = pi/4 is : {dw_dt.subs(t, sp.pi/4).evalf()}")

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the temperature function
def temperature(x, y):
    return 3*x**2 + 2*y**2

# Define the gradient function
def gradient(x, y):
    return np.array([6*x, 4*y])

# Given point
point = np.array([-1, 2])

# Calculate gradient at the point (-1, 2)
grad_at_point = gradient(point[0], point[1])
print(f"Gradient at point (-1, 2): {grad_at_point}")

# Direction vector
direction = np.array([-1, -np.sqrt(2)])
# Normalize the direction vector
direction_norm = direction / np.linalg.norm(direction)

# Calculate directional derivative
directional_derivative = np.dot(grad_at_point, direction_norm)
print(f"Directional derivative in the direction (-1, -√2): {directional_derivative}")

# Create grid for plotting
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calculate directional derivative field
dir_deriv_field = (-6*X - 4*np.sqrt(2)*Y) / np.sqrt(3)

# Create figure with two subplots
fig = plt.figure(figsize=(15, 6))

# 2D Contour Plot
ax1 = fig.add_subplot(121)
contour = ax1.contourf(X, Y, dir_deriv_field, levels=50, cmap='viridis')
plt.colorbar(contour, ax=ax1)
ax1.set_title('Directional Derivative Field (Contour)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Mark the point and direction
ax1.plot(point[0], point[1], 'ro', label='Point (-1, 2)')
ax1.arrow(point[0], point[1], 
          direction_norm[0]*0.5, direction_norm[1]*0.5,
          head_width=0.1, head_length=0.1, fc='r', ec='r')
ax1.legend()

# 3D Surface Plot
ax2 = fig.add_subplot(122, projection='3d')
surface = ax2.plot_surface(X, Y, dir_deriv_field, cmap='viridis')
ax2.set_title('Directional Derivative Field (Surface)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('Directional Derivative')
plt.colorbar(surface, ax=ax2)

plt.tight_layout()
plt.show()

# Optional: Plot the temperature function itself
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
Z = temperature(X, Y)
surface = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Temperature Distribution T(x,y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Temperature')
plt.colorbar(surface)
plt.show()