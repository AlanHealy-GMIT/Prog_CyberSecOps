# lines.py
# This program takes a list of points and prints out
#    distance to the origin for each
# Author: Alan Healy
# Date Created: 13-FEB-2021

# import the math module
import math

points = [(1, 2), (3, 3), (4, 3)]

for x, y in points:
    dist = math.sqrt((x**2) + (y**2))
    print('Point ({},{}) is {:.2f} from the origin.'.format(x, y, dist))
