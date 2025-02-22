import numpy as np

# Monte Carlo integration to verify the result
def monte_carlo_flux(num_samples=1000000):
    # Define the region bounds
    r_max = 3
    z_min, z_max = 0, 2
    theta_min, theta_max = 0, 2 * np.pi
    
    # Generate random points in cylindrical coordinates
    r = np.random.uniform(0, r_max, num_samples)
    theta = np.random.uniform(theta_min, theta_max, num_samples)
    z = np.random.uniform(z_min, z_max, num_samples)
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Compute the divergence
    divergence = 3 * x**2 + 3 * y**2 + 2 * z
    
    # Volume of the region
    volume = np.pi * r_max**2 * (z_max - z_min)
    
    # Average divergence
    average_divergence = np.mean(divergence)
    
    # Flux is average divergence multiplied by volume
    flux = average_divergence * volume
    return flux

# Compute the flux
result = monte_carlo_flux()
print("Numerical approximation of the outward flux:", result)