# plotly pie charts:
# https://plotly.com/python/pie-charts/
# https://plotly.com/python/reference/#pie
#
# html color names:
# https://www.rapidtables.com/web/color/html-color-codes.html
# https://www.w3schools.com/cssref/css_colors.asp
#
# plotly color:
# https://plotly.com/python/colorscales/
# https://plotly.com/python/builtin-colorscales/#builtin-sequential-color-scales
import plotly.express as px
import pandas as pd
import os

# set current working directory path and filename variables
path = os.getcwd()
out_file = 'interests.csv'

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
                  color_discrete_sequence=px.colors.sequential.Jet,
                  title='ET574 Student Majors',
)

# style the pie chart
fig.update_traces(
        hole=.5,
        hoverinfo='label',
        hovertext='value',
        textinfo='percent',
        textfont_size=20,
        marker=dict(
            line=dict(
                color='white', width=10
            )
        )
)

# render an html file of the chart and open in default browser
fig.show()

# export dataframe to file
df.to_csv(path+"/data/"+out_file, index=False)
