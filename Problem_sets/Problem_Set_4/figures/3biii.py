import matplotlib.pyplot as plt
import numpy as np

# Parameters
a = 2  # Example value
E0 = 1  # Example value

# Define the function V(x)
def V(x, a, E0):
    if x < -a/2:
        return -(a/4) * E0
    elif -a/2 <= x <= a/2:
        return (x/2) * E0
    else:  # x > a/2
        return (a/4) * E0

# Vectorize the function to apply it element-wise on an array
V_vec = np.vectorize(V)

# Generate x values
x = np.linspace(-a, a, 4000)

# Generate y values
y = V_vec(x, a, E0)

# Plotting
plt.plot(x, y, label=r'$V(x)$')
plt.axvline(x=-a/2, linestyle='--', color='grey', label=r'$x=-a/2$')
plt.axvline(x=a/2, linestyle='--', color='grey', label=r'$x=a/2$')
plt.xlabel(r'$x$')
plt.ylabel(r'$V(x)$')
plt.title(r'Plot of $V(x)$')
plt.legend()
plt.grid(True)
plt.show()
