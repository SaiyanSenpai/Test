# https://www.w3schools.com/python/trypython.asp?filename=demo_matplotlib_pie5
# A pie chart - parts of a whole
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.1, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
