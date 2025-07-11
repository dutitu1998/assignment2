import numpy as np
import matplotlib.pyplot as plt

Z_values = [1, 4, 9, 16, 25, 36]

plt.figure(figsize=(12, 6))
# --- Subplot 1: Elliptic contours of f(x, y) = 4x^2 + y^2 ---
x1 = np.linspace(-5, 5, 400)
y1 = np.linspace(-7, 7, 400)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = 4 * X1**2 + Y1**2

plt.subplot(1, 2, 1)
contour1 = plt.contour(X1, Y1, Z1, levels=Z_values,cmap='viridis')
plt.clabel(contour1, inline=True,fontsize=8)
plt.title(r'Contour plot of $f(x, y) = 4x^2 + y^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')  # Optional for visual symmetry

# --- Subplot 2: Circular contours from f(x, y, z) = z^2 - x^2 - y^2 = 0 ---
x2 = np.linspace(-36, 36, 400)
y2 = np.linspace(-36, 36, 400)
X2, Y2 = np.meshgrid(x2, y2)

plt.subplot(1, 2, 2)
for z in Z_values:
    Z2 = z**2 - X2**2 - Y2**2
    contour2 = plt.contour(X2, Y2, Z2, levels=[0], cmap='viridis')
    plt.clabel(contour2, inline=True, fontsize=8, fmt={0: f'z={z}'})
plt.title(r'Level curves of $f(x, y, z) = z^2 - x^2 - y^2$ (where $f=0$)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')  # Ensure circular shape looks correct

plt.tight_layout()
plt.show()          