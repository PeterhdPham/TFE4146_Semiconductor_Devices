import numpy as np
import matplotlib.pyplot as plt

# Assuming constant values
q = 1.6e-19  # Elementary charge in Coulombs
epsilon = 8.85e-12  # Permittivity of free space in Farad/meter
k = 1e21  # An arbitrary constant for dopant profile gradient
x_0 = 0.0  # Midpoint of the depletion region
W = 1e-6  # Width of the depletion region

# Define the function E(x)
def E(x):
    return (q * k / (2 * epsilon)) * ((x - x_0)**2 - (W/2)**2)

# Generate x values for plotting
x_values = np.linspace(- W/2, W/2, 1000)
y_values = E(x_values)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r'$E(x)$', color='blue')
plt.axvline(x=x_0, color='red', linestyle='--', label=r'$x_0$')  # Marking x_0
plt.title(r'Plot of $E(x)$')
plt.xlabel('x')
plt.ylabel(r'$E(x)$')
plt.legend()
plt.grid(True)
plt.show()
