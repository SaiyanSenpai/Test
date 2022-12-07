# 4 sample Plots on a figure
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# https://matplotlib.org/3.2.1/tutorials/introductory/sample_plots.html
import matplotlib.pyplot as plt
import numpy as np

numbers= [1,2,3,4,5]
squares = [1,4,9,16,25]
cubes = [1,8,27,64,125]

rand_data = np.random.randn(1000) # numpy random ndarray generator
n_bins = 50

plt.style.use('seaborn-whitegrid')

fix,ax = plt.subplots(2,2)  # create a figure with two rows of axes

# implement a linegraph in top left corner
ax[0,0].plot(numbers, cubes, c='darkblue', linewidth=3)

# implement a scatter plot in bottom right corner
ax[1,0].scatter(numbers, squares, s=15, c='red')

# implement a line with markers in top right corner
ax[0,1].barh(numbers, squares, .5, align='center')

# implement a histogram in bottom right corner
ax[1,1].hist(rand_data, n_bins)

# save the figure to a file
plt.savefig('myGraph.png')

# display the figure
plt.show()
