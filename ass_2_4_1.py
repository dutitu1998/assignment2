import numpy as np
import matplotlib.pyplot as plt

# Define the grid for x and y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# (i) f(x, y) = 4x^2 + y^2
Z1 = 4 * X**2 + Y**2

# (ii) f(x, y, z) = z^2 - x^2 - y^2
# For contour plots, we set z = sqrt(x^2 + y^2 + k) or z = -sqrt(x^2 + y^2 + k)
# However, since we are plotting in 2D, we consider z as a function of x and y for fixed k.
# For simplicity, we plot the level curves for z^2 - x^2 - y^2 = k, which implies z = sqrt(x^2 + y^2 + k) or z = -sqrt(x^2 + y^2 + k).
# But since we are in 2D, we plot x^2 + y^2 = z^2 - k, which are circles for z^2 > k.
Z2 = X**2 + Y**2

# Define the levels for the contour plots
levels = [1, 4, 9, 16, 25, 36]

# Plot for f(x, y) = 4x^2 + y^2
plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z1, levels=levels, colors='blue')
plt.title('Contour Plot of $f(x, y) = 4x^2 + y^2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.axis('equal')
plt.show()

# Plot for f(x, y, z) = z^2 - x^2 - y^2
plt.figure(figsize=(8, 6))
for k in levels:
    plt.contour(X, Y, Z2, levels=[k], colors='red', linestyles='dashed')
plt.title('Contour Plot of $f(x, y, z) = z^2 - x^2 - y^2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.axis('equal')
plt.show()