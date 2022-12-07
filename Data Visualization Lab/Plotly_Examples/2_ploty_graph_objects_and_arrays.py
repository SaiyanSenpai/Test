# bar graph
# numpy arrays are similar to python lists
import numpy as np
import plotly.graph_objects as go

# numpy one dimensional arrays
numbers = np.arange(1,21)
numbers = [n for n in range(1,21)]
cubes = np.linspace(1,21, 21)**3
cubes = [n**3 for n in range(1,21)]
fig = go.Figure(
    data=[go.Bar( x=numbers,y=cubes)],
    layout=go.Layout(
        title = go.layout.Title(text='Numbers vs Cubes'),
        xaxis = go.layout.XAxis(title='Numbers'),
        yaxis = go.layout.YAxis(title='Cubes')
    )
)
# renderer the display to the browser (the default renderer)
fig.show()
