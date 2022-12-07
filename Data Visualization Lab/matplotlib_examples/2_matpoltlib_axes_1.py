# Figures contain one or more axes
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt

# create a figure and axes using the subplot function to place the axes
fig1 = plt.figure()
ax = fig1.add_subplot(111)      # subplot grid: 1 row, 1 col, position 1

# create a figure and axes using the subplot function to place the axes
fig2 = plt.figure()
# num_rows, num_cols, position (left to right, then down)
ax1 = fig2.add_subplot(211)     # subplot grid: 2 rows, 1 cols, position 1
ax2 = fig2.add_subplot(223)     # subplot grid: 2 rows, 2 cols, position 3
ax3 = fig2.add_subplot(224)     # subplot grid: 2 rows, 2 cols, position 4
plt.show()
