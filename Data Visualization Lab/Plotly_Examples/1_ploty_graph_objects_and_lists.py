'''
https://plotly.com/python/graph-objects/
Plotly is an interactive, open-source plotting
library that supports over 40 unique chart types:
statistical, financial, geographic, scientific and more...
'''
import plotly.graph_objects as go

# list comprehensions
numbers = [n for n in range(1, 21)]
squares = [n**2 for n in range(1, 21)]
#go scatter renders a line
fig = go.Figure(
    data=[
        go.Scatter( x=numbers,
                    y=squares,
        )
    ],
    layout=go.Layout(
        title = go.layout.Title(text='Numbers vs Squares'),
        xaxis = go.layout.XAxis(title='Numbers'),
        yaxis = go.layout.YAxis(title='Squares')
    )
)

# renderer the display to the browser (the default renderer)
# Demo: Save web page as (html+JS)
# Demo: Save png (not interactive)
# scatter, by default, connects the dots with lines
fig.show()
