import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function (i): f(x, y) = y^2 - 2y cos(x), 1 <= x <= 7
def f1(x, y):
    return y**2 - 2 * y * np.cos(x)

# Function (ii): f(x, y) = |sin(x) sin(y)|, 0 <= x <= 2π, 0 <= y <= 2π
def f2(x, y):
    return np.abs(np.sin(x) * np.sin(y))

# Create a grid for x and y
x1 = np.linspace(1, 7, 100)
y1 = np.linspace(-5, 5, 100)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = f1(X1, Y1)

x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.linspace(0, 2 * np.pi, 100)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = f2(X2, Y2)

# Plot for function (i)
fig1 = plt.figure(figsize=(10, 5))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(X1, Y1, Z1, cmap='viridis')
ax1.set_title('3D Plot of $f(x, y) = y^2 - 2y \cos(x)$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_zlabel('$f(x, y)$')
plt.show()

# Plot for function (ii)
fig2 = plt.figure(figsize=(10, 5))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X2, Y2, Z2, cmap='plasma')
ax2.set_title('3D Plot of $f(x, y) = |\sin(x) \sin(y)|$')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.set_zlabel('$f(x, y)$')
plt.show()