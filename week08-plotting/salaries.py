# salaries.py
# This program makes a list of salaries and uses plots.
# Author: Alan Healy
# Date Created: 11-APR-2021

import numpy as np

# set variables
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print (salaries)

salariesPlus = salaries + 5000
print (salariesPlus)

salariesMult = salaries * 1.05
print(salariesMult)

newSalaries = salariesMult.astype(int)
print(newSalaries)
