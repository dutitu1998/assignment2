import numpy as np
import matplotlib.pyplot as plt

# Define the curve
t = np.linspace(0, 2 * np.pi, 100)
x = 5 * np.cos(t)
y = 4 * np.sin(t)

# Points of interest
t1 = np.pi / 4
t2 = np.pi

# Position vectors
r_t1 = np.array([5 * np.cos(t1), 4 * np.sin(t1)])
r_t2 = np.array([5 * np.cos(t2), 4 * np.sin(t2)])

# Tangent vectors
dr_t1 = np.array([-5 * np.sin(t1), 4 * np.cos(t1)])
dr_t2 = np.array([-5 * np.sin(t2), 4 * np.cos(t2)])

# Plot the curve
plt.figure(figsize=(3, 4))
plt.plot(x, y, label='Curve C')

# Plot position vectors
plt.quiver(0, 0, r_t1[0], r_t1[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'$r(\\pi/4)$')
plt.quiver(0, 0, r_t2[0], r_t2[1], angles='xy', scale_units='xy', scale=1, color='b', label=f'$r(\\pi)$')

# Plot tangent vectors
plt.quiver(r_t1[0], r_t1[1], dr_t1[0], dr_t1[1], angles='xy', scale_units='xy', scale=1, color='g', label=f"$r'(\\pi/4)$")
plt.quiver(r_t2[0], r_t2[1], dr_t2[0], dr_t2[1], angles='xy', scale_units='xy', scale=1, color='m', label=f"$r'(\\pi)$")

# Add labels and legend
plt.xlabel('x')
plt.ylabel('$y$')
#plt.axhline(0, color='black', linewidth=5)
#plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title('Curve C with Position and Tangent Vectors')
plt.axis('equal')
plt.show()