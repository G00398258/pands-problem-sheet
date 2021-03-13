# Weekly Task for Week 08
# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Author: Gillian Kane-McLoughlin

# See README file for references

import numpy as np 
import matplotlib.pyplot as plt

# Setting names for each function & doing calculations
fOfX = np.array(range(0,4)) # I would say "f of x" for f(x)
gOfX = fOfX * fOfX # x squared
hOfX = gOfX * fOfX # x cubed

# From trial and error, I found I had to plot each function one by one (using a line chart)
plt.plot(fOfX, color = "r", label = "f(x)=x") # colour red
plt.plot(gOfX, color = "b", label = "g(x)=x2") # blue
plt.plot(hOfX, color = "g", label = "h(x)=x3") # green

# Making it look nicer!
plt.title("Plot of Functions: f(x), g(x) & h(x)")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()

plt.show()



