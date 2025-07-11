import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

# Symbolic part
r, theta, z, h, R = smp.symbols('r theta z h R', real=True)
rho = r**2
dV = r  # In cylindrical coordinates, dV = r dr dθ dz
mass_integral = smp.integrate(rho * dV, (r, 0, R), (theta, 0, 2*smp.pi), (z, 0, h)).doit().simplify()
print(f'The mass of the cylinder is: {mass_integral}\n')  # Should be π h R⁴

#This is bonus part
# Numeric visualization
h_val = 2
r_val = 1
theta_vals = np.linspace(0, 2 * np.pi, 100)
x = r_val * np.cos(theta_vals)
y = r_val * np.sin(theta_vals)
Z1 = np.linspace(0, h_val, 100) # Generates 100 circular rings at different z-heights

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

for z in Z1:
    ax.plot(x, y, z, color='cyan', alpha=0.5) #Draws a hollow cylinder frame layer-by-layer — visually appealing and lightweight.

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Vertical Cylinder: Radius = 1, Height = 2")
plt.show()
