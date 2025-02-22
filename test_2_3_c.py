import sympy as sp

# Define the variable
theta = sp.symbols('theta')

# Define x, y, z in terms of theta
x = sp.sin(theta)
y = sp.cos(theta)
z = sp.tan(theta)

# Define w
w = sp.sqrt(x**2 + y**2 + z**2)

# Compute dw/dθ using chain rule
dw_dtheta = sp.diff(w, theta)

# Evaluate at θ = π/4
theta_val = sp.pi / 4
result = dw_dtheta.subs(theta, theta_val)

# Print results
print(f"dw/dtheta: {dw_dtheta}")
print(f"dw/dtheta at θ = π/4: {result.evalf()}")
