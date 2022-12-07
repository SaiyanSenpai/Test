# Pie chart styling
#
# plotly pie charts:
# https://plotly.com/python/pie-charts/
# https://plotly.com/python/reference/#pie
#
# https://plotly.com/python/colorscales/
# https://plotly.com/python/builtin-colorscales/#builtin-sequential-color-scales
import plotly.express as px
import pandas as pd

# instantiate a pandas dataframe with a dictionary
df = pd.DataFrame(
    dict(
        area_of_interest=['Computer Programming',
                          'Cybersecurity',
                          'Web Development',
                          'Electronics',
                          'Engineering',
                          'Other'

        ],
        interest_percentages=[37.5, 31.3, 4.7, 10.9, 7.8, 7.8],
    )
)
# instantiate a plotly express pie chart using the dataframe
fig = px.pie( df, values=df.interest_percentages,
                  names=df.area_of_interest,
                  color=df.area_of_interest,
                  color_discrete_map={
                        'Computer Programming': 'crimson',
                        'Cybersecurity': 'forestgreen',
                        'Web Development': 'khaki',
                        'Electronics': 'darksalmon',
                        'Engineering': 'orange',
                        'Other': 'darkblue',
                  },
                  title='ET575 Student Majors',
)

# style the pie chart
fig.update_traces(
        pull=[0,0,0,0,0,.2],
        textposition='inside',
        textinfo='percent',
        textfont_size=20,
        insidetextorientation='radial',
        rotation=-90
)

# render an html file of the chart and open in default browser
fig.show()
