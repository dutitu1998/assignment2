import sympy as sp

# Define symbols
x, y, z, r, theta = sp.symbols('x y z r theta')

# Define vector field F = (2z, 3x, 5y)
F = sp.Matrix([2*z, 3*x, 5*y])

# Compute curl of F (∇ × F)
curl_F = sp.Matrix([
    sp.diff(F[2], y) - sp.diff(F[1], z),
    sp.diff(F[0], z) - sp.diff(F[2], x),
    sp.diff(F[1], x) - sp.diff(F[0], y)
])

print("Curl of F:", curl_F)

# Surface: z = 4 - x^2 - y^2
z_surface = 4 - x**2 - y**2

# Compute normal vector (gradient of f(x,y,z) = x^2 + y^2 + z - 4)
normal_vector = sp.Matrix([-2*x, -2*y, 1])

# dS magnitude
dS = sp.sqrt(4*x**2 + 4*y**2 + 1)

# Convert to polar coordinates
x_polar, y_polar = r * sp.cos(theta), r * sp.sin(theta)
normal_polar = normal_vector.subs({x: x_polar, y: y_polar})
dS_polar = dS.subs({x: x_polar, y: y_polar}) * r  # Include Jacobian factor

# Surface integral ∬ (∇ × F) ⋅ dS
dot_product = curl_F.dot(normal_polar)
surface_integral = sp.integrate(sp.integrate(dot_product * dS_polar, (r, 0, 2)), (theta, 0, 2*sp.pi))

print("Surface Integral:", surface_integral)

# Parameterization for boundary curve C (circle x^2 + y^2 = 4, z=0)
x_curve, y_curve, z_curve = 2 * sp.cos(theta), 2 * sp.sin(theta), 0

# Compute dr
dr = sp.Matrix([-2 * sp.sin(theta), 2 * sp.cos(theta), 0])

# Compute F along C
F_curve = F.subs({x: x_curve, y: y_curve, z: z_curve})

# Compute line integral ∮ F ⋅ dr
line_integral = sp.integrate(F_curve.dot(dr), (theta, 0, 2*sp.pi))

print("Line Integral:", line_integral)

# Verify Stokes' theorem
if sp.simplify(surface_integral - line_integral) == 0:
    print("Stokes' Theorem Verified ✅")
else:
    print("Stokes' Theorem NOT Verified ❌")
