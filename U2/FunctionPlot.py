# This program imports a data set and then plots the resulting graphs.

#import simpleplot

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-12, 12, 100) # 100 evenly spaced points between -10 and 10
#x = x[x >= 0] 
y = np.sqrt(x)
g = np.sqrt(x + 4) - 1
h = np.sqrt(0.5*x + 3) + 2

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.set_xlabel('Time (s)')
ax.set_ylabel('Velocity (m/s)')
ax.plot(x,y)
ax.plot(x,g)
ax.plot(x,h)

plt.show()                           # Show the figure.


		





