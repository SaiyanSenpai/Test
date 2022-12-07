#pandas dataframe
import plotly.express as px
import pandas as pd

# instantiate a pandas dataframe
df = pd.DataFrame({
    'names':['jim', 'tony', 'karen'],
    'gpa':[3.5, 3.8, 3.40],
})

# instantiate a plotly express bar chart from a panda dataframe
fig = px.bar( df, x=df.names, y=df.gpa )

# render an html file of the chart and open in default browser
fig.show()
