import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the helix
t = np.linspace(0, 10, 1000)
x = np.cos(t)
y = np.sin(t)
z = t
# Final position
s = 10
t_final = s / np.sqrt(2)
x_final = np.cos(t_final)
y_final = np.sin(t_final)
z_final = t_final
# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Helix')
ax.scatter(x_final, y_final, z_final, color='red', label='Final Position (s=10)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()