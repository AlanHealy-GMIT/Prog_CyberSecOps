# histogramSalaries.py
# This program plots a historgram of salaries.
# Author: Alan Healy
# Date Created: 11-APR-2021

import numpy as np
import matplotlib.pyplot as plt

# set variables
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# make random number same each time for debugging
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()
