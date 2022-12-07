# A Line plot
#  
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

fix,ax = plt.subplots()
ax.plot(x,y)                        # create a plot of x and y axis values
ax.set_title('Numbers Squared')     # set a title
ax.set_xlabel('Numbers')            # name the x-axis
ax.set_ylabel('Squares')            # name the y-axis
plt.show()
