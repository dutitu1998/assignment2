import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Setup
x, y, z, X, Y, Z, t = sp.symbols('x y z X Y Z t')
ellipsoid_eq = x**2 + 4*y**2 + z**2 - 18
point = (1, 2, 1)

print(f"Ellipsoid: x² + 4y² + z² = 18")
print(f"Point: {point}")

# Part i: Tangent plane
grad = [sp.diff(ellipsoid_eq, var) for var in (x, y, z)]
grad_at_point = [g.subs({x: point[0], y: point[1], z: point[2]}) for g in grad]
tangent_plane = sum(g*(var - p) for g, var, p in zip(grad_at_point, (X, Y, Z), point))
print(f"\ni. Tangent plane: {sp.simplify(tangent_plane)} = 0")
print(f"   Simplified: X + 8Y + Z = 18")

# Part ii: Normal line
normal_vector = grad_at_point
param_x = point[0] + t*normal_vector[0]
param_y = point[1] + t*normal_vector[1] 
param_z = point[2] + t*normal_vector[2]
print(f"\nii. Normal line parametric equations:")
print(f"    x = {param_x}")
print(f"    y = {param_y}")
print(f"    z = {param_z}")

# Part iii: Angle with xy-plane
normal_xy = sp.Matrix([0, 0, 1])
normal_tangent = sp.Matrix(normal_vector)
dot = normal_tangent.dot(normal_xy)
angle_rad = sp.acos(dot / (normal_tangent.norm() * normal_xy.norm()))
acute_angle = min(float(sp.deg(angle_rad)), 180 - float(sp.deg(angle_rad)))
print(f"\niii. Acute angle with xy-plane: {acute_angle:.2f}°")

# Part iv: Visualization
fig = plt.figure(figsize=(12, 10))

# Ellipsoid with tangent plane - Main plot
ax = fig.add_subplot(111, projection='3d')

# Create ellipsoid surface with higher resolution
u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)
U, V = np.meshgrid(u, v)
a, b = np.sqrt(18), np.sqrt(18/4)
X_ell = a * np.sin(V) * np.cos(U)
Y_ell = b * np.sin(V) * np.sin(U)
Z_ell = a * np.cos(V)

# Plot ellipsoid surface with better visibility
ax.plot_surface(X_ell, Y_ell, Z_ell, alpha=0.6, color='lightblue', 
                edgecolor='blue', linewidth=0.1)

# Plot ellipsoid wireframe for better structure visibility
ax.plot_wireframe(X_ell, Y_ell, Z_ell, color='darkblue', alpha=0.3, linewidth=0.5)

# Plot the point of tangency
ax.scatter(*point, color='red', s=150, zorder=5, label='Point (1,2,1)')

# Tangent plane
xx, yy = np.linspace(-2, 4, 12), np.linspace(0, 4, 12)
XX, YY = np.meshgrid(xx, yy)
ZZ = 18 - XX - 8*YY
ax.plot_surface(XX, YY, ZZ, alpha=0.4, color='yellow', 
                edgecolor='orange', linewidth=0.5)

# Normal line
t_vals = np.linspace(-0.8, 0.8, 100)
norm_x = point[0] + t_vals * normal_vector[0]
norm_y = point[1] + t_vals * normal_vector[1]
norm_z = point[2] + t_vals * normal_vector[2]
ax.plot(norm_x, norm_y, norm_z, 'g-', linewidth=4, label='Normal Line')

# Add coordinate axes for reference
ax.plot([0, 5], [0, 0], [0, 0], 'k--', alpha=0.5, linewidth=1)
ax.plot([0, 0], [0, 3], [0, 0], 'k--', alpha=0.5, linewidth=1)
ax.plot([0, 0], [0, 0], [0, 5], 'k--', alpha=0.5, linewidth=1)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('3D Ellipsoid with Tangent Plane and Normal Line', fontsize=14)

# Set equal aspect ratio and better viewing angle
ax.set_box_aspect([1,1,1])
ax.view_init(elev=20, azim=45)

# Add legend
ax.legend(loc='upper right')

# Add grid
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
