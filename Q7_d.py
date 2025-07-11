import sympy as sp
from sympy import symbols, exp, diff, integrate

# Define symbolic variables
x, y = symbols('x y')

u = exp(y)        # x-component
v = x * exp(y)    # y-component

print("Force Field: F(x,y) = e^y î + xe^y ĵ")
print("=" * 50)

# Part (i): Verify that the force field is conservative
print("\nPart (i): Checking if the force field is conservative")
du_dy = diff(u, y)
dv_dx = diff(v, x)

print(f"∂u/∂y = {du_dy}")
print(f"∂v/∂x = {dv_dx}")

is_conservative = du_dy.equals(dv_dx)
print(f"\nIs conservative? {is_conservative}")

print("=" * 50)

# Part (ii): Find the potential function φ
print("\nPart (ii): Finding the potential function φ")

# ∂φ/∂x = -u = -e^y
# Integrate with respect to x
phi_from_x = integrate(-u, x)
print(f"Integrating ∂φ/∂x = -e^y: φ(x,y) = {phi_from_x} + g(y)")

# Proposed potential function
phi = -exp(y) - x*exp(y)

# Verify gradients
grad_phi_x = diff(phi, x)
grad_phi_y = diff(phi, y)

print(f"∂φ/∂x = {grad_phi_x}")
print(f"∂φ/∂y = {grad_phi_y}")

print("=" * 50)

# Part (iii): Work done along semicircular path
print("\nPart (iii): Work done from (1,0) to (-1,0) along semicircular path")

phi_initial = phi.subs({x:1, y:0})
phi_final = phi.subs({x:-1, y:0})

work = phi_final - phi_initial

print(f"φ(1,0) = {phi_initial}")
print(f"φ(-1,0) = {phi_final}")
print(f"Work done = φ(-1,0) - φ(1,0) = {work} = {work.evalf()}")

print("=" * 50)
