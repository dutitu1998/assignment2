import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables
x, y = sp.symbols('x y', real=True)

def analyze_critical_points(f, title):
    print(f"\n{title}")
    print("="*50)
    
    # Find critical points
    fx= sp.diff(f, x)
    fy=sp.diff(f, y)
    critical_points = sp.solve([fx, fy], [x, y])
    
    # Calculate Hessian
    fxx= sp.diff(fx, x)
    fyy=sp.diff(fy, y)
    fxy=sp.diff(fx, y)
    
    # Classify each critical point
    for point in critical_points:
        x_val, y_val = point
        H_xx = fxx.subs([(x, x_val), (y, y_val)])
        H_yy = fyy.subs([(x, x_val), (y, y_val)])
        H_xy = fxy.subs([(x, x_val), (y, y_val)])
        det_H = H_xx * H_yy - H_xy**2
        
        if det_H > 0:
            classification = "Local Maximum" if H_xx < 0 else "Local Minimum"
        elif det_H < 0:
            classification = "Saddle Point"
        else:
            classification = "Inconclusive"
        
        f_val = f.subs([(x, x_val), (y, y_val)])
        print(f"({x_val}, {y_val}): {classification}, f = {f_val}")
    
    return critical_points, f

# Function (i): f(x,y) = 4xy - x^4 - y^4
f1 = 4*x*y - x**4 - y**4
cp1, f1_func = analyze_critical_points(f1, "Function (i): f(x,y) = 4xy - x⁴ - y⁴")

# Function (ii): f(x,y) = 4x²e^y - 2x^4 - e^(4y)
f2 = 4*x**2*sp.exp(y) - 2*x**4 - sp.exp(4*y)
cp2, f2_func = analyze_critical_points(f2, "Function (ii): f(x,y) = 4x²eʸ - 2x⁴ - e⁴ʸ")

# Create 3D plots
fig = plt.figure(figsize=(12, 5))

# Plot function (i)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
x_range = np.linspace(-2, 2, 100)
y_range = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_range, y_range)
Z1 = 4*X*Y - X**4 - Y**4
ax1.plot_surface(X, Y, Z1, alpha=0.7, cmap='viridis')
ax1.set_title('f(x,y) = 4xy - x⁴ - y⁴')

# Mark critical points
for point in cp1:
    x_val, y_val = float(point[0]), float(point[1])
    z_val = float(f1_func.subs([(x, x_val), (y, y_val)]))
    ax1.scatter([x_val], [y_val], [z_val], color='red', s=100)

# Plot function (ii)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
x_range2 = np.linspace(-2, 2, 100)
y_range2 = np.linspace(-1, 1, 100)
X2, Y2 = np.meshgrid(x_range2, y_range2)
Z2 = 4*X2**2*np.exp(Y2) - 2*X2**4 - np.exp(4*Y2)
ax2.plot_surface(X2, Y2, Z2, alpha=0.7, cmap='plasma')
ax2.set_title('f(x,y) = 4x²eʸ - 2x⁴ - e⁴ʸ')

# Mark critical points
for point in cp2:
    x_val, y_val = float(point[0]), float(point[1])
    z_val = float(f2_func.subs([(x, x_val), (y, y_val)]))
    ax2.scatter([x_val], [y_val], [z_val], color='red', s=100)

plt.tight_layout()
plt.show()