import sympy as sp

# Define the variables
x, y, z, λ = sp.symbols('x y z λ')

# Define the temperature function and the constraint
T = 8*x**2 + 4*y*z - 16*z + 600
g = 4*x**2 + y**2 + 4*z**2 - 16

# Compute the gradients
grad_T = [sp.diff(T, var) for var in (x, y, z)]
grad_g = [sp.diff(g, var) for var in (x, y, z)]

# Set up the Lagrange multiplier equations
equations = [grad_T[i] - λ * grad_g[i] for i in range(3)] + [g]

# Solve the system of equations
solutions = sp.solve(equations, (x, y, z, λ), dict=True)

# Evaluate the temperature at the critical points
for sol in solutions:
    print(f"Critical point: (x, y, z) = ({sol[x]}, {sol[y]}, {sol[z]})")
    print(f"Temperature: {T.subs(sol)}")