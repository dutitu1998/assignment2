import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Symbol
t = sp.symbols('t', real=True)

# ----------- Curve 1 -----------
r1 = sp.Matrix([sp.exp(t), sp.exp(t)*sp.cos(t), sp.exp(t)*sp.sin(t)])
r1_prime = r1.diff(t)  #1st derivation
r1_prime2 = r1.diff(t, 2) #2nd derivation
r1_prime3 = r1.diff(t, 3)  #3rd derivation

# ----------- Curve 2 -----------
r2 = sp.Matrix([2*sp.cos(t), 3*sp.sin(t), 0])
r2_prime = r2.diff(t) #1st derivation
r2_prime2 = r2.diff(t, 2) #2nd derivation
r2_prime3 = r2.diff(t, 3) #3rd derivation

# ----------- Frenet Functions -----------
def Tangent(vec, tval):
    T = vec / vec.norm()
    return T.subs(t, tval).evalf()

def Normal(vec, tval):
    T = vec / vec.norm()
    N = T.diff(t)
    N = N / N.norm()
    return N.subs(t, tval).evalf()

def Binormal(vec, tval):
    T = vec / vec.norm()
    N = T.diff(t)
    N = N / N.norm()
    B = T.cross(N)
    return B.subs(t, tval).evalf()

def curvature(v1, v2, tval):
    κ = (v1.cross(v2)).norm() / (v1.norm()**3)
    return κ.subs(t, tval).evalf()

def torsion(v1, v2, v3, tval):
    τ = v1.dot(v2.cross(v3)) / (v1.cross(v2)).norm()**2
    return τ.subs(t, tval).evalf()

# ----------- Evaluations for r1 at t=0 -----------
print("Curve r1(t) = e^t, e^t cos t, e^t sin t")
print(f"Tangent at t=0: {Tangent(r1_prime, 0)}\n")
print(f"Normal at t=0: {Normal(r1_prime, 0)}\n")
print(f"Binormal at t=0: {Binormal(r1_prime, 0)}\n")
print(f"Curvature at t=0: {curvature(r1_prime, r1_prime2, 0)}\n")
print(f"Torsion at t=0: {torsion(r1_prime, r1_prime2, r1_prime3, 0)}\n")

# ----------- Evaluations for r2 at t = 0 and 2π -----------
print("Curve r2(t) = 2cos t, 3sin t, 0\n")

for t_check in [0, 2*sp.pi]:
    print(f"--- t = {t_check} ---")
    print(f"Tangent: {Tangent(r2_prime, t_check)}")
    print(f"Normal: {Normal(r2_prime, t_check)}")
    print(f"Binormal: {Binormal(r2_prime, t_check)}")
    print(f"Curvature: {curvature(r2_prime, r2_prime2, t_check)}")
    print(f"Torsion: {torsion(r2_prime, r2_prime2, r2_prime3, t_check)}\n")

# ----------- Plotting Curvatures -----------
t_values = np.linspace(0, 2 * np.pi, 400)

kappa1_values = [curvature(r1_prime, r1_prime2, t_val) for t_val in t_values]
kappa2_values = [curvature(r2_prime, r2_prime2, t_val) for t_val in t_values]

plt.figure(figsize=(10, 6))
plt.plot(t_values, kappa1_values, label='Curvature of r1(t)', color='blue')
plt.plot(t_values, kappa2_values, label='Curvature of r2(t)', color='orange')
plt.xlabel('t')
plt.ylabel('Curvature κ(t)')
plt.title('Curvature Comparison of Two Curves')
plt.legend()
plt.grid(True)
plt.show()
