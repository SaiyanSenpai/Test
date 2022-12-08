'''
    Use matploitlib.
'''


print("1)")
import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

all_packages_installed = True
for n in ["matplotlib","pandas","plotly",'requests']:
    if n in installed_packages:
        print(n+" is installed.")
        continue
    else:
        all_packages_installed = False
if all_packages_installed:
    print("The packages are installed.")
else:
    print("All packages are not installed.")


print("\n2)")
import matplotlib.pyplot as plt

# a Figure is the space upon which a graph can be placed
fig = plt.figure()                  # create an empty figure
fig = plt.figure(figsize=(9,6))    # create an empty figure which is 9 by by 6 inches
plt.show()

print("\n3)")
# A Line plot
#  
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [n**3 for n in x]
print(y)
fix,ax = plt.subplots()
ax.plot(x,y)                        # create a plot of x and y axis values
ax.set_title('Powers of Three')     # set a title
ax.set_xlabel('Numbers')            # name the x-axis
ax.set_ylabel('Cubes')            # name the y-axis
plt.show()

print("\n4)")
# https://www.w3schools.com/python/trypython.asp?filename=demo_matplotlib_pie5
# A pie chart - parts of a whole
import matplotlib.pyplot as plt
import numpy as np

y = np.array([28, 26, 25, 21])
mylabels = ["John", "Paul", "George", "Ringo"]
myexplode = [0.1, 0, 0, 0]

plt.pie(y, labels = mylabels,autopct="%2.1f%%", explode = myexplode, shadow = True)
plt.show()

print("\n5)")
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
