import numpy as np
# First curve
print('For the first curve, the parametric equation:')
t1 = 2
x1, y1, z1 = np.log(t1), np.exp(-t1), t1**3
dx1,dy1,dz1=1/t1,-np.exp(-t1),3*t1**2
print(f'x = {x1} + {dx1} * t')
print(f'y = {y1} + {dy1} * t')
print(f'z = {z1} + {dz1} * t')
# Second curve
print('\nFor the second curve, the parametric equation:')
t1 = 1 / 3
x1, y1, z1 = 2 * np.cos(np.pi * t1), 2 * np.sin(np.pi * t1), 3 * t1
dx1, dy1, dz1 = -2 * np.pi * np.sin(np.pi * t1), 2 * np.pi * np.cos(np.pi * t1), 3

print(f'x = {x1} + {dx1} * t')
print(f'y = {y1} + {dy1} * t')
print(f'z = {z1} + {dz1} * t')

import numpy as np  
# Define the normal vectors of the planes 
normal_vector1 = np.array([3, -6, -2]) 
normal_vector2 = np.array([2, 1, -2]) 
 
# Find the cross product of the normal vectors 
parallel_vector = np.cross(normal_vector1, normal_vector2) 
 
print(f"Vector parallel to the line of intersection: {parallel_vector}") 
 
import sympy as sp 
 
# Define the parameter t 
t = sp.symbols('t') 
 
# Define the parametric equations for r(t) 
r_t = sp.Matrix([3*t, sp.sin(t), t**2]) 
 
# Find the velocity as the first derivative of r(t) 
velocity = sp.diff(r_t, t) 
 
# Find the acceleration as the second derivative of r(t) 
acceleration = sp.diff(velocity, t) 
 
print(f"Velocity vector: {velocity}") 
print(f"Acceleration vector: {acceleration}") 
 
# Plot the graph of theta(t) versus t (assuming theta(t) is the angle in the xy-plane) 
import matplotlib.pyplot as plt 
import numpy as np 
 
theta = sp.atan2(velocity[1], velocity[0]) 
theta_func = sp.lambdify(t, theta, 'numpy') 
t_vals = np.linspace(0, 10, 400) 
theta_vals = theta_func(t_vals) 
 
plt.plot(t_vals, theta_vals) 
plt.xlabel('t') 
plt.ylabel('θ(t)') 
plt.title('θ(t) vs t') 
plt.grid(True) 
plt.show()