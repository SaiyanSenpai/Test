# with Numpy arrays
import numpy as np
import plotly.express as px

numbers = np.arange(1,21)
cubes = np.linspace(1,20, 20)**3

# instantiate a plotly express scatter plot chart from numpy arrays
fig = px.scatter( x=numbers, y=cubes, labels={'x':'numbers', 'y':'cubes'})

# render an html file of the chart and open in default browser
fig.show()
