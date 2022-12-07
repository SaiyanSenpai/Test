# Styling our Plots
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html
# https://matplotlib.org/3.2.1/api/markers_api.html#module-matplotlib.markers
import matplotlib.pyplot as plt

numbers= [1,2,3,4,5]
squares = [1,4,9,16,25]
cubes = [1,8,27,64,125]

# print a list of figure styles
print(plt.style.available)
# use the style 'seaborn-darkgrid'
plt.style.use('classic')

fig,ax = plt.subplots()
# style the plot
ax.plot(numbers, squares, c='red',
        marker='o', markersize='7',
        linestyle='dashed', linewidth='1',
        label='squares')
ax.plot(numbers, cubes, c='blue',
        marker='s', markersize='7',
        linestyle='dashed', linewidth='1',
        label='cubes')

ax.set_title('Numbers Squared', fontsize=16)
ax.set_xlabel('Numbers', fontsize=12)
ax.set_ylabel('Squares', fontsize=12)

ax.tick_params(axis='both', labelsize=7)

ax.legend(loc='best')
plt.show()
