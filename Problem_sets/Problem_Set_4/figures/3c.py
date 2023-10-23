import matplotlib.pyplot as plt
import numpy as np

# Given values
a = 2
E0 = 1  # assuming a value for E0
epsilon = 1  # assuming a value for epsilon
Delta = 0.2  # assuming a value for Delta, such that Delta << a

x = np.linspace(-a-2*Delta, a+2*Delta, 1000)  # x range from -a-2*Delta to a+2*Delta

# (i)
rho_i = np.piecewise(x, 
                    [x < -a/2, (-a/2 <= x) & (x <= 0), (0 < x) & (x <= a/2), x > a/2],
                    [0, -2/a*epsilon*E0, 2/a*epsilon*E0, 0])

# (ii)
rho_ii = np.piecewise(x, 
                     [x < 0, (0 <= x) & (x <= a/2), x > a/2], 
                     [0, 4*epsilon/a*E0, 0])

# (iii)
rho_iii = np.piecewise(x, 
                      [x < -(a + 2*Delta)/2, (-(a + 2*Delta)/2 <= x) & (x < -a/2), 
                       (-a/2 <= x) & (x <= a/2), (a/2 < x) & (x <= (a + 2*Delta)/2), x > (a + 2*Delta)/2],
                      [0, -epsilon/(2*Delta)*E0, 0, epsilon/(2*Delta)*E0, 0])

# Plotting
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(x, rho_i, label=r'$\rho_i(x)$')
plt.title(r'$\rho_i(x)$')
plt.xlabel('x')
plt.ylabel(r'$\rho(x)$')
plt.grid(True)
plt.axvline(x=-a/2, color='r', linestyle='--')
plt.axvline(x=a/2, color='r', linestyle='--')

plt.subplot(1,3,2)
plt.plot(x, rho_ii, label=r'$\rho_{ii}(x)$')
plt.title(r'$\rho_{ii}(x)$')
plt.xlabel('x')
plt.ylabel(r'$\rho(x)$')
plt.grid(True)
plt.axvline(x=0, color='r', linestyle='--')
plt.axvline(x=a/2, color='r', linestyle='--')

plt.subplot(1,3,3)
plt.plot(x, rho_iii, label=r'$\rho_{iii}(x)$')
plt.title(r'$\rho_{iii}(x)$')
plt.xlabel('x')
plt.ylabel(r'$\rho(x)$')
plt.grid(True)
plt.axvline(x=-(a + 2*Delta)/2, color='r', linestyle='--')
plt.axvline(x=-a/2, color='r', linestyle='--')
plt.axvline(x=a/2, color='r', linestyle='--')
plt.axvline(x=(a + 2*Delta)/2, color='r', linestyle='--')

plt.tight_layout()
plt.show()
