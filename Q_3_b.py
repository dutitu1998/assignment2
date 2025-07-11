import sympy as sp

x, y = sp.symbols('x y', real=True)
f = y**2 * sp.cos(x - y)

# Compute partial derivatives
f_xx = f.diff(x, 2)
f_yy = f.diff(y, 2)
laplace_eq = f_xx + f_yy

# Check Laplace equation
if laplace_eq == 0:
    print('Laplace equation satisfied')
else:
    print('Laplace equation not satisfied')

# Extract real and imaginary parts (f is real, so v=0)
u = sp.re(f)
v = sp.im(f)

# Check Cauchy-Riemann conditions
if u.diff(x) == v.diff(y) and u.diff(y) == -v.diff(x):
    print('Cauchy-Riemann conditions satisfied')
else:
    print('Cauchy-Riemann conditions not satisfied')

# Check equality of mixed partial derivatives
if f.diff(x, y) == f.diff(y, x):
    print('fxy = fyx')
else:
    print('fxy != fyx')
