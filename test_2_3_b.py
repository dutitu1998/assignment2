import sympy as sp

# Define variables
x, y = sp.symbols('x y')

# Define the function f(x, y)
f = y**2 * sp.cos(x*y)

# Compute first-order derivatives
f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

# Compute second-order derivatives
f_xx = sp.diff(f_x, x)
f_yy = sp.diff(f_y, y)

# Compute mixed partial derivatives
f_xy = sp.diff(f_x, y)
f_yx = sp.diff(f_y, x)

# Check Laplace’s equation (f_xx + f_yy)
laplace_eq = f_xx + f_yy

# Display results
print(f"First-order derivatives:\n f_x = {f_x}\n f_y = {f_y}\n")
print(f"Second-order derivatives:\n f_xx = {f_xx}\n f_yy = {f_yy}\n")
print(f"Mixed partial derivatives:\n f_xy = {f_xy}\n f_yx = {f_yx}\n")
print(f"Laplace equation result (should be 0 if satisfied): {sp.simplify(laplace_eq)}\n")

# Verify mixed partial derivative identity
print(f"Mixed Partial Derivative Identity holds: {f_xy == f_yx}")
