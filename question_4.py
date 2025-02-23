
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables
x, y = sp.symbols('x y')

# Function 1: f(x, y) = 4xy - x^4 - y^4
f1 = 4*x*y - x**4 - y**4

# Compute partial derivatives
f1_x = sp.diff(f1, x)  # 4y - 4x^3
f1_y = sp.diff(f1, y)  # 4x - 4y^3

# Find critical points by solving f1_x = 0 and f1_y = 0
critical_points1 = sp.solve([f1_x, f1_y], (x, y))

# Compute second partial derivatives for the second derivative test
f1_xx = sp.diff(f1_x, x)  # -12x^2
f1_yy = sp.diff(f1_y, y)  # -12y^2
f1_xy = sp.diff(f1_x, y)  # 4

# Classify critical points
print("Analysis for f(x, y) = 4xy - x^4 - y^4:")
maxima1, minima1, saddles1 = [], [], []
for cp in critical_points1:
    # Ensure the critical point has real coordinates
    if not (cp[0].is_real and cp[1].is_real):
        continue
    x_val, y_val = float(cp[0]), float(cp[1])
    # Evaluate the discriminant D = f_xx * f_yy - (f_xy)^2
    D = (f1_xx.subs({x: x_val, y: y_val}) * f1_yy.subs({x: x_val, y: y_val}) - 
         f1_xy.subs({x: x_val, y: y_val})**2)
    fxx_val = f1_xx.subs({x: x_val, y: y_val})
    if D > 0:
        if fxx_val < 0:
            maxima1.append((x_val, y_val))
            print(f"Relative maximum at ({x_val}, {y_val})")
        elif fxx_val > 0:
            minima1.append((x_val, y_val))
            print(f"Relative minimum at ({x_val}, {y_val})")
    elif D < 0:
        saddles1.append((x_val, y_val))
        print(f"Saddle point at ({x_val}, {y_val})")

# Function 2: f(x, y) = 4x^2 e^(-y) - 2x^4 - e^(4y)
f2 = 4*x*2 * sp.exp(-y) - 2*x**4 - sp.exp(4*y)

# Compute partial derivatives
f2_x = sp.diff(f2, x)  # 8x e^(-y) - 8x^3
f2_y = sp.diff(f2, y)  # -4x^2 e^(-y) - 4e^(4y)

# Find critical points
critical_points2 = sp.solve([f2_x, f2_y], (x, y))

# Classify critical points (if any)
print("\nAnalysis for f(x, y) = 4x^2 e^(-y) - 2x^4 - e^(4y):")
maxima2, minima2, saddles2 = [], [], []
if not critical_points2:
    print("No critical points exist.")
else:
    f2_xx = sp.diff(f2_x, x)
    f2_yy = sp.diff(f2_y, y)
    f2_xy = sp.diff(f2_x, y)
    for cp in critical_points2:
        if not (cp[0].is_real and cp[1].is_real):
            continue
        x_val, y_val = float(cp[0]), float(cp[1])
        D = (f2_xx.subs({x: x_val, y: y_val}) * f2_yy.subs({x: x_val, y: y_val}) - 
             f2_xy.subs({x: x_val, y: y_val})**2)
        fxx_val = f2_xx.subs({x: x_val, y: y_val})
        if D > 0:
            if fxx_val < 0:
                maxima2.append((x_val, y_val))
                print(f"Relative maximum at ({x_val}, {y_val})")
            elif fxx_val > 0:
                minima2.append((x_val, y_val))
                print(f"Relative minimum at ({x_val}, {y_val})")
        elif D < 0:
            saddles2.append((x_val, y_val))
            print(f"Saddle point at ({x_val}, {y_val})")

# Plotting Function 1
def f1_num(X, Y):
    return 4*X*Y - X**4 - Y**4

X = np.linspace(-2, 2, 100)
Y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(X, Y)
Z1 = f1_num(X, Y)

fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis', alpha=0.8)

# Mark maxima (red)
for pt in maxima1:
    ax1.scatter(pt[0], pt[1], f1_num(pt[0], pt[1]), color='red', s=100, label='Maxima' if pt == maxima1[0] else "")
# Mark minima (green) - none expected, but included for completeness
for pt in minima1:
    ax1.scatter(pt[0], pt[1], f1_num(pt[0], pt[1]), color='green', s=100, label='Minima' if pt == minima1[0] else "")
# Mark saddle points (blue)
for pt in saddles1:
    ax1.scatter(pt[0], pt[1], f1_num(pt[0], pt[1]), color='blue', s=100, label='Saddle' if pt == saddles1[0] else "")

ax1.set_title('f(x, y) = 4xy - x^4 - y^4')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')
ax1.legend()
plt.show()

# Plotting Function 2
def f2_num(X, Y):
    return 4*X**2 * np.exp(-Y) - 2*X**4 - np.exp(4*Y)

# Adjust range to avoid overflow and visualize behavior
X = np.linspace(-2, 2, 100)
Y = np.linspace(-1, 1, 100)  # Limited y-range due to exponential terms
X, Y = np.meshgrid(X, Y)
Z2 = f2_num(X, Y)

fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis', alpha=0.8)

# No critical points to mark, but included for consistency
ax2.set_title('f(x, y) = 4x^2 e^(-y) - 2x^4 - e^(4y)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x, y)')
plt.show()