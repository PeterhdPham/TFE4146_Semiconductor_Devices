import matplotlib.pyplot as plt
import numpy as np

# Parameters
a = 2  # Example value
E0 = 1  # Example value

# Define the function V(x)
def V(x, a, E0):
    if x < 0:
        return 0
    elif 0 <= x <= a/2:
        return -(a/2) * E0 * ((1 - 2*x/a)**2 - 1)
    else:  # x > a/2
        return (a/2) * E0

# Vectorize the function to apply it element-wise on an array
V_vec = np.vectorize(V)

# Generate x values
x = np.linspace(-a, a, 400)

# Generate y values
y = V_vec(x, a, E0)

# Plotting
plt.plot(x, y, label=r'$V(x)$')
plt.axvline(x=0, linestyle='--', color='grey', label=r'$x=0$')
plt.axvline(x=a/2, linestyle='--', color='grey', label=r'$x=a/2$')
plt.xlabel(r'$x$')
plt.ylabel(r'$V(x)$')
plt.title(r'Plot of $V(x)$')
plt.legend()
plt.grid(True)
plt.show()
