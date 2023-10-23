import numpy as np
import matplotlib.pyplot as plt

# Constants
Is = 1e-12  # Reverse bias saturation current in A
n = 1        # Ideality factor
k = 1.38e-23 # Boltzmann's constant in J/K
T = 300      # Temperature in K
q = 1.6e-19  # Charge of an electron in C

VT = k*T/q  # Thermal voltage in V

# Voltage range for the plot
V = np.linspace(-10, 1, 400)

# Shockley diode equation
I = Is * (np.exp(V/(n*VT)) - 1)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(V, I, label="Diode I/V curve")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title("I/V Curve of a Diode")
plt.xlabel("Voltage, V (V)")
plt.ylabel("Current, I (A)")
plt.legend()
plt.yscale("symlog", linthresh=1e-9)
plt.xscale("linear")
plt.ylim([-1e-6, 1e-6])
plt.xlim([-10, 10])
plt.show()
