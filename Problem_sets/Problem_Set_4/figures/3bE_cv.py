import matplotlib.pyplot as plt
import numpy as np

# Constants
a = 2  # The value of a is assumed for this sketch. You might have a different value.
Eg = 1.1  # Example bandgap energy, assumed for silicon. Adjust as needed.
E0 = 1  # Example, adjust as per your needs.

# Define x range
x = np.linspace(-a, a, 400)

# Potential functions from the text above, note that these should be adjusted if your V(x) differs.
def V_i(x, a, E0):
    cond1 = x < -a/2
    cond2 = (x >= -a/2) & (x <= 0)
    cond3 = (x > 0) & (x <= a/2)
    cond4 = x > a/2
    
    return np.where(cond1, -a/4*E0,
            np.where(cond2, -a/4*E0*(1-(1+2/a*x)**2),
            np.where(cond3, -a/4*E0*((1-2/a*x)**2-1),
            a/4*E0)))

def V_ii(x, a, E0):
    cond1 = x < 0
    cond2 = (x >= 0) & (x <= a/2)
    cond3 = x > a/2
    
    return np.where(cond1, 0,
            np.where(cond2, -a/2*E0*((1-2/a*x)**2-1),
            a/2*E0))

def V_iii(x, a, E0):
    cond1 = x < -a/2
    cond2 = (x >= -a/2) & (x <= a/2)
    cond3 = x > a/2
    
    return np.where(cond1, -a/4*E0,
            np.where(cond2, x/2*E0,
            a/4*E0))

# Plot figures
fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# (i)
axs[0].plot(x, V_i(x, a, E0), label=r"$V(x)$")
axs[0].plot(x, V_i(x, a, E0)-Eg, linestyle='--', label=r"$E_v(x)$")
axs[0].plot(x, V_i(x, a, E0)+Eg, linestyle='--', label=r"$E_c(x)$")
axs[0].legend()
axs[0].set_title(r"(i)")

# (ii)
axs[1].plot(x, V_ii(x, a, E0), label=r"$V(x)$")
axs[1].plot(x, V_ii(x, a, E0)-Eg, linestyle='--', label=r"$E_v(x)$")
axs[1].plot(x, V_ii(x, a, E0)+Eg, linestyle='--', label=r"$E_c(x)$")
axs[1].legend()
axs[1].set_title(r"(ii)")

# (iii)
axs[2].plot(x, V_iii(x, a, E0), label=r"$V(x)$")
axs[2].plot(x, V_iii(x, a, E0)-Eg, linestyle='--', label=r"$E_v(x)$")
axs[2].plot(x, V_iii(x, a, E0)+Eg, linestyle='--', label=r"$E_c(x)$")
axs[2].legend()
axs[2].set_title(r"(iii)")

# Additional plot settings
for ax in axs:
    ax.axvline(x=-a/2, color='k', linestyle=':')
    ax.axvline(x=a/2, color='k', linestyle=':')
    ax.axhline(y=0, color='k', linestyle='-')
    ax.grid(True)
    ax.set_ylabel(r"$Energy (eV)$")
    
axs[2].set_xlabel(r"$x$")

plt.tight_layout()
plt.show()
