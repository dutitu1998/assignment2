import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
 
# Part (a) 
def plot_contours(): 
    # Create grid points 
    x = np.linspace(-10, 10, 100) 
    y = np.linspace(-10, 10, 100) 
    X, Y = np.meshgrid(x, y) 
     
    # Plot (i) f(x,y) = 4x^2 + y^2 
    Z1 = 4*X**2 + Y**2 
    plt.figure(figsize=(10, 5)) 
    plt.subplot(121) 
    plt.contour(X, Y, Z1, levels=[1,4,9,16,26,36]) 
    plt.title('f(x,y) = 4x² + y²') 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid(True) 
     
    # Plot (ii) f(x,y,z) = z^2 - x^2 - y^2 
    Z2 = X**2 + Y**2 
    plt.subplot(122) 
    plt.contour(X, Y, Z2, levels=[1,4,9,16,26,36]) 
    plt.title('f(x,y,z) = z² - x² - y²') 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid(True) 
    plt.show() 
 
# Part (b) 
def plot_3d_functions(): 
    # (i) f(x,y) = y^2 - 2y*cos(x) 
    x1 = np.linspace(1, 7, 100) 
    y1 = np.linspace(-5, 5, 100) 
    X1, Y1 = np.meshgrid(x1, y1) 
    Z1 = Y1**2 - 2*Y1*np.cos(X1) 
     
    fig = plt.figure(figsize=(15, 5)) 
    ax1 = fig.add_subplot(121, projection='3d') 
    ax1.plot_surface(X1, Y1, Z1, cmap='viridis') 
    ax1.set_title('f(x,y) = y² - 2y*cos(x)') 
     
    # (ii) f(x,y) = |sin(x)sin(y)| 
    x2 = np.linspace(0, 2*np.pi, 100) 
    y2 = np.linspace(0, 2*np.pi, 100) 
    X2, Y2 = np.meshgrid(x2, y2) 
    Z2 = np.abs(np.sin(X2) * np.sin(Y2)) 
     
    ax2 = fig.add_subplot(122, projection='3d') 
    ax2.plot_surface(X2, Y2, Z2, cmap='viridis') 
    ax2.set_title('f(x,y) = |sin(x)sin(y)|') 
    plt.show() 
 
# Part (c) 
def plot_functions_for_extrema(): 
    x = np.linspace(-3, 3, 100) 
    y = np.linspace(-3, 3, 100) 
    X, Y = np.meshgrid(x, y) 
     
    # (i) f(x,y) = 4xy - x^4 - y^4 
    Z1 = 4*X*Y - X**4 - Y**4 
     
    plt.figure(figsize=(10, 5)) 
    plt.subplot(121) 
    plt.contour(X, Y, Z1, 20) 
    plt.title('f(x,y) = 4xy - x⁴ - y⁴') 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid(True) 
     
    # (ii) f(x,y) = 4x²e^y - 2x⁴ - e^{4y} 
    Z2 = 4*(X**2)*np.exp(Y) - 2*(X**4) - np.exp(4*Y) 
     
    plt.subplot(122) 
    plt.contour(X, Y, Z2, 20) 
    plt.title('f(x,y) = 4x²e^y - 2x⁴ - e^{4y}') 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid(True) 
    plt.show() 
 
# Run all plots 
plot_contours() 
plot_3d_functions() 
plot_functions_for_extrema()
