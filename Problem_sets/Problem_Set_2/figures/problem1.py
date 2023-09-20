import matplotlib.pyplot as plt
import numpy as np

# Constants
q = 1.6e-19  # Charge of an electron in Coulombs
mu_n = 1350  # Electron mobility for Si in cm^2/V-s
mu_p = 450  # Hole mobility for Si in cm^2/V-s
ni = 1.5e10  # Approximate intrinsic carrier concentration for Si in cm^-3

# Function to calculate total conductivity
def total_sigma(tilde_n, tilde_p, ni, q, mu_n, mu_p):
    return q * ni * (tilde_n * mu_n + tilde_p * mu_p)

# Generate a range of tilde_n and tilde_p values from 0 to 10
tilde_values = np.linspace(0, 10, 500)

# Assuming tilde_n = tilde_p for intrinsic or equally doped cases
sigma_values = total_sigma(tilde_values, tilde_values, ni, q, mu_n, mu_p)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(tilde_values, sigma_values)
plt.title("Total Conductivity vs Normalized Carrier Concentration")
plt.xlabel("$\\tilde{n}$ or $\\tilde{p}$")
plt.ylabel("$\\sigma$ (S/cm)")
plt.grid(True)
plt.show()
