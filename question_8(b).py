import numpy as np

# Monte Carlo integration to verify the result
def monte_carlo_surface_integral(num_samples=1000000):
    # Generate random points on the unit sphere
    theta = np.random.uniform(0, 2 * np.pi, num_samples)
    phi = np.arccos(np.random.uniform(-1, 1, num_samples))
    
    # Compute x^2
    x = np.sin(phi) * np.cos(theta)
    x_squared = x**2
    
    # Surface area of the unit sphere is 4π
    surface_area = 4 * np.pi
    
    # Average value of x^2 over the sphere
    average_x_squared = np.mean(x_squared)
    
    # Integral is average value multiplied by surface area
    integral = average_x_squared * surface_area
    return integral

# Compute the integral
result = monte_carlo_surface_integral()
print("Numerical approximation of the surface integral:", result)