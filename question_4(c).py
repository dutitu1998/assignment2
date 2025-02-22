import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define the function
f1 = 4*x*y - x**4 - y**4

# Compute second derivatives
fxx = sp.diff(f1, x, x)  # Second derivative wrt x
fyy = sp.diff(f1, y, y)  # Second derivative wrt y
fxy = sp.diff(f1, x, y)  # Mixed partial derivative

# Find critical points by solving first derivatives = 0
critical_points = sp.solve([sp.diff(f1, x), sp.diff(f1, y)], (x, y))

# Filter only real solutions
real_critical_points = [point for point in critical_points if all(coord.is_real for coord in point)]

# Analyze each critical point
for point in real_critical_points:
    x_val, y_val = point  # Extract critical point values
    D = fxx * fyy - fxy**2  # Hessian determinant

    # Substitute critical point into second derivatives
    D_val = D.subs({x: x_val, y: y_val})
    fxx_val = fxx.subs({x: x_val, y: y_val})

    if D_val.is_real:
        if D_val > 0:
            if fxx_val > 0:
                print(f"Local minimum at {point}")
            else:
                print(f"Local maximum at {point}")
        elif D_val < 0:
            print(f"Saddle point at {point}")
        else:
            print(f"Inconclusive at {point}")
