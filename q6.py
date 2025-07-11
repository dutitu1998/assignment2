import numpy as np
from scipy.integrate import tplquad, dblquad

print("--- Part (a)(i) ---")

def f_a1(z, y, x):
    return x * np.exp(-y) * np.cos(z)

 #f_a1 function calling 
result_a1, error_a1 = tplquad( f_a1,0,1,lambda x:0,lambda x: 1 - x**2,lambda x,y: 3,lambda x,y: 4 - x**2 - y**2)

print(f"Result of the triple integral: {result_a1:.6f}")
print(f"Estimated error: {error_a1:.2e}\n")

print("--- Part (a)(ii) ---")

def f_a2(y, x):
    return (x * y) / np.sqrt(x**2 + y**2 + 1)
#calling function
result_a2, error_a2 = dblquad(f_a2, 0, 1, 0, 1) 

print(f"Result of the double integral over R: {result_a2:.6f}")
print(f"Estimated error: {error_a2:.2e}\n")

print("--- Part (b) ---")

def f_b(y, x):
    # Add a small epsilon to avoid division by zero at x=2, though our limit is 1.
    epsilon = 1e-9
    return 2 / np.sqrt(4 - x**2 + epsilon)

# The integral is over the rectangle R: 0 <= x <= 1, 0 <= y <= 4.
result_b, error_b = dblquad(f_b, 0, 1, 0, 4)

print(f"Surface area: {result_b:.6f}")
print(f"Estimated error: {error_b:.2e}\n")

print("--- Part (c) ---")

def f_c(r, theta):
    return (3 - 2 * r * np.cos(theta) - r**2) * r

result_c, error_c = dblquad(f_c, 0, 2 * np.pi, 0, 1)

print(f"Volume of the solid: {result_c:.6f}")
print(f"Estimated error: {error_c:.2e}\n")