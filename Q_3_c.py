import numpy as np
def compute_dw_dtheta(theta):
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.tan(theta)
    
    dw_dx = x / np.sqrt(x**2 + y**2 + z**2)
    dw_dy = y / np.sqrt(x**2 + y**2 + z**2)
    dw_dz = z / np.sqrt(x**2 + y**2 + z**2)
    
    dx_dtheta = -np.sin(theta)
    dy_dtheta = np.cos(theta)
    dz_dtheta = 1 / (np.cos(theta)**2)
    
    return dw_dx * dx_dtheta + dw_dy * dy_dtheta + dw_dz * dz_dtheta
print(f"the value is",compute_dw_dtheta(np.pi/4))