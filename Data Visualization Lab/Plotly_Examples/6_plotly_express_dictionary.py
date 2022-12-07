# bar chart
import plotly.express as px

data = {
    'numbers': [n for n in range(1, 21)],
    'squares': [n**2 for n in range(1, 21)],
}

# bar chart from a dictionary with nested lists
fig = px.bar( x=data['numbers'], y=data['squares'] )

# render an html file of the chart and open in default browser
fig.show()
