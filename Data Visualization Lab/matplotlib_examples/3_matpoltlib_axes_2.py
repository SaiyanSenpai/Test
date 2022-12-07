# Axes examples
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt

# an Axes is a plot which is placed into a figure
fig, ax1 = plt.subplots()         # a figure with a single axes
fig, ax2 = plt.subplots(2, 1)     # a figure with 2x1 axes
fig, ax3 = plt.subplots(2, 2)     # a figure with 2x2 axes
plt.show()
