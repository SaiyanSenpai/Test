# Plotly Express -very concise sytax
import plotly.express as px

numbers = [n for n in range(1, 21)]
squares = [n**2 for n in range(1, 21)]

# instantiate a plotly express line chart from list comprehensions
fig = px.line( x=numbers, y=squares, labels={'x':'numbers', 'y':'squares'}, title="The Powers of 2" )

# render an html file of the chart and open in default browser
fig.show()
