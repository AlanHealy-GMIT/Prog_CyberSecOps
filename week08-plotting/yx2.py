# yx2.py
# This program plots the function y = x^2.
# Author: Alan Healy
# Date Created: 11-APR-2021

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints  # multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
