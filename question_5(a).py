import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Define the ellipsoid
def ellipsoid(x, y):
    # Ensure the argument of sqrt is non-negative
    z_squared = 18 - x**2 - 4*y**2
    z_squared = np.clip(z_squared, 0, None)  # Clip negative values to 0
    return np.sqrt(z_squared)

# Define the tangent plane
def tangent_plane(x, y):
    return (-2*x - 16*y + 36) / 2

# Define the normal line
def normal_line(t):
    x = 1 + 2*t
    y = 2 + 16*t
    z = 1 + 2*t
    return x, y, z

# Create a grid of points for the ellipsoid
x = np.linspace(-4, 4, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = ellipsoid(X, Y)

# Create a grid of points for the tangent plane
Z_plane = tangent_plane(X, Y)

# Create points for the normal line
t = np.linspace(-1, 1, 100)
x_line, y_line, z_line = normal_line(t)

# Calculate the angle between the tangent plane and the xy-plane
normal_tangent_plane = np.array([2, 16, 2])
normal_xy_plane = np.array([0, 0, 1])
cos_theta = np.dot(normal_tangent_plane, normal_xy_plane) / (np.linalg.norm(normal_tangent_plane) * np.linalg.norm(normal_xy_plane))
theta_rad = math.acos(cos_theta)
theta_deg = math.degrees(theta_rad)

# Print the results
print("i. Equation of the tangent plane:")
print("2x + 16y + 2z - 36 = 0")
print("\nii. Parametric equations of the normal line:")
print("x = 1 + 2t")
print("y = 2 + 16t")
print("z = 1 + 2t")
print("\niii. Acute angle between the tangent plane and the xy-plane:")
print(f"Theta = {theta_deg:.2f} degrees")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the ellipsoid (only valid Z values)
ax.plot_surface(X, Y, Z, color='b', alpha=0.5, label='Ellipsoid')
ax.plot_surface(X, Y, -Z, color='b', alpha=0.5)

# Plot the tangent plane
ax.plot_surface(X, Y, Z_plane, color='r', alpha=0.5, label='Tangent Plane')

# Plot the normal line
ax.plot(x_line, y_line, z_line, color='g', label='Normal Line')

# Plot the point of tangency
ax.scatter(1, 2, 1, color='k', label='Point (1, 2, 1)')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set limits
ax.set_xlim([-4, 4])
ax.set_ylim([-3, 3])
ax.set_zlim([-5, 5])

# Add a legend with a fixed location
ax.legend(loc='upper right')

# Show the plot
plt.show()