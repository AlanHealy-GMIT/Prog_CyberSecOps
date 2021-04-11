# counties.py
# This program makes a pie chart of counties.
# Author: Alan Healy
# Date Created: 11-APR-2021

import numpy as np
import matplotlib.pyplot as plt

# make array of counties
possibleCounties = ['Cork', 'Dublin', 'Kildare', 'Westmeath', 'Wicklow']

# pick 100 randomly from possible counties with frequency set in p
counties = np.random.choice(possibleCounties, p = [0.1, 0.3, 0.2, 0.12, 0.28], size = (100) )

# need number of occurrences of each county
# save this in unique tuple
unique, counts = np.unique(counties, return_counts = True)

# plot as pie chart
# plt.pie(counts, labels = unique)

plt.bar(unique, counts)

plt.show()