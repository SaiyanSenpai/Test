# plotly pie charts: 1 pie, many sectors.
# https://plotly.com/python/pie-charts/
import plotly.express as px
import pandas as pd

# instantiate a pandas dataframe with a dictionary
df = pd.DataFrame(
    dict(
        major_names=['Computer Science and Information Security',
                     'Internet and Information Technology',
                     'Computer Engineering Technology',
                     'Engineering Science',
                     'Other'],
        major_enrollment=[64.1, 12.5, 10.9, 9.9, 2.6],
    )
)

# instantiate a plotly express pie chart using the dataframe
fig = px.pie( df, values=df.major_enrollment,
                  names=df.major_names,
                  color=df.major_names,
                  title='ET575 Student Majors',
)

# render an html file of the chart and open in default browser
fig.show()
