import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Define gauss function

def gauss(x, A, x0, sigma, z0):
   return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

# Users input

A = float(input("Enter A: "))
x0 = float(input("Enter x0: "))
sigma = float(input("Enter sigma: "))
z0 = float(input("Enter z0: "))
a = float(input("Enter lower bound for integral: "))
b = float(input("Enter upper bound for integral: "))

# Compute area

area = integrate.quad(gauss, a, b, args=(A, x0, sigma, z0))[0]

# Compute reasonable linspace

xmin_plot = min(a, x0 - 5*sigma)
xmax_plot = max(b, x0 + 5*sigma)
x_plot = np.linspace(xmin_plot, xmax_plot, 400)

# Plot everything

plt.plot(x_plot, gauss(x_plot, A, x0, sigma, z0), label = 'Gaussian curve')
plt.fill_between(x_plot, gauss(x_plot, A, x0, sigma, z0), 0, where=(x_plot >= a) & (x_plot <= b), alpha=0.5, label = f'area = {area:.2f}')
plt.xlabel('x')
plt.ylim(0, None)
plt.ylabel('y')
plt.legend()
plt.show()