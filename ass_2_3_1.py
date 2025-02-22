import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function
f = y**2 * sp.cos(x - y)

# Compute first-order partial derivatives
f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

# Compute second-order partial derivatives
f_xx = sp.diff(f_x, x)
f_yy = sp.diff(f_y, y)
f_xy = sp.diff(f_x, y)
f_yx = sp.diff(f_y, x)

# Check Laplace's equation
laplace = f_xx + f_yy
print(f"Laplace's equation: ∇²f = {laplace}")
if laplace == 0:
    print("The function satisfies Laplace's equation.")
else:
    print("The function does not satisfy Laplace's equation.")

# Check the identity f_xy = f_yx
if f_xy == f_yx:
    print("The identity f_xy = f_yx holds.")
else:
    print("The identity f_xy = f_yx does not hold.")

# Output the partial derivatives
print("\nPartial derivatives:")
print(f"f_x = {f_x}")
print(f"f_y = {f_y}")
print(f"f_xx = {f_xx}")
print(f"f_yy = {f_yy}")
print(f"f_xy = {f_xy}")
print(f"f_yx = {f_yx}")