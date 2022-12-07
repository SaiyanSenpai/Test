# We can think of a figure as an empty canvas
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt

# a Figure is the space upon which a graph can be placed
fig = plt.figure()                  # create an empty figure
fig = plt.figure(figsize=(10,5))    # create an empty figure which is 10 by by 5 inches
plt.show()                          # show the figure
