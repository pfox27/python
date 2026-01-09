# This program imports a data set and then plots the resulting graphs.

#import simpleplot

import matplotlib.pyplot as plt
import numpy as np


dataset1 = [(1, 4), (1, 5), (2, 7), (4, 9)]
dataset2 = [(1, 2), (2, 7), (2, 5), (7, 6)]
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.set_xlabel('Time (s)')
ax.set_ylabel('Velocity (m/s)')
ax.plot([1,1,2,4],[4,5,7,9])
ax.plot([1,2,2,7], [2,7,5,6])
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

print("The maximum value in data set 1 is: " , max(dataset1));
		
#simpleplot.plot_lines("Sample", 400, 300, "x", "y", [dataset1, dataset2], True, ["Dataset 1", "Dataset 2"])




