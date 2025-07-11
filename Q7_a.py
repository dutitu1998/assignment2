from scipy.integrate import dblquad

# Define the temperature function as a lambda
T = lambda y, x: 10 - 8*x**2 - 2*y**2

# Perform the double integration
integral_value, error = dblquad(
    T,                     # function to integrate
    0,                     # x lower limit: 0                              
    1,                     # x upper limit: 1
    lambda x: 0,           # y lower limit: 0
    lambda x: 2            # y upper limit: 2
)

# Calculate average temperature
area = 2  # 1 × 2 rectangle
average_temp = integral_value / area

print(f"Integral: {integral_value:.10f}")
print(f"Average temperature: {average_temp:.10f}")
print(f"Exact value: {14/3:.10f}")