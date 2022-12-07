# bar chart
#
# plotly bar charts:
# https://plotly.com/python/bar-charts/
#
# html color names:
# https://www.rapidtables.com/web/color/html-color-codes.html
#
# plotly color:
# https://plotly.com/python/colorscales/
# hhttps://plotly.com/python/discrete-color/#discrete-color-concepts
import plotly.express as px
import pandas as pd

# instantiate a pandas dataframe with a dictionary
# major_names=keys, major_percentages=values
df = pd.DataFrame(
    dict(
        major_names=['Computer Science and Information Security',
                     'Internet and Information Technology',
                     'Computer Engineering Technology',
                     'Engineering Science',
                     'Other'],
        major_percentages=[64.1, 12.5, 10.9, 10.9, 1.6]
    )
)

# instantiate a plotly express bar chart using dataframe input data
fig = px.bar( df, x=df.major_names,
                  y=df.major_percentages,
                  color=df.major_names,
                  title='ET575 Student Majors',
                  color_discrete_sequence=['darkblue',
                                           'royalblue',
                                           'dodgerblue',
                                           'deepskyblue',
                                           'cyan']
)

# render an html file of the chart and open in default browser
fig.show()
