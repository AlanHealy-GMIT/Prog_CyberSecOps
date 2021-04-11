# ages.py
# This program plots a scatter plot of ages vs salaries.
# Author: Alan Healy
# Date Created: 11-APR-2021

import numpy as np
import matplotlib.pyplot as plt

# set variables
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

lowAge  = 21
highAge = 65

# make random number same each time for debugging
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(lowAge, highAge, size = numberOfEntries)

plt.scatter(ages,salaries, label = "Salaries")
#plt.show()

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints  # multiply each entry by itself

plt.plot(xpoints, ypoints, color = 'red', label="X Squared")

plt.title("Random Plot")
plt.xlabel("Age")
plt.ylabel("Salaries")
plt.legend()
#plt.show()

plt.savefig('prettier-plot.png')

