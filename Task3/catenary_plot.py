#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import cosh
import numpy as np
from matplotlib import pyplot as plt

x_values = list(range(-5, 6))
y_values = []
for x in x_values:
    y = cosh(x)
    y_values.append(y)

x_values_np = np.arange(-5, 6, 1)
y_values_np = np.cosh(x_values_np)


plt.plot(x_values, y_values, label="cosh(x)")
plt.plot(x_values_np, y_values_np, label="cosh(x) np")
plt.grid()
plt.title("Catenary", fontsize=15)
plt.xlabel("x", fontsize=15)
plt.ylabel("cosh(x)", fontsize=15)
plt.xticks(range(-5, 6, 1))
plt.yticks(range(0, 81, 10))
plt.legend()
plt.show()

