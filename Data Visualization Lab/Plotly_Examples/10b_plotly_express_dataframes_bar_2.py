# tidy data:
# https://pandas.pydata.org/docs/reference/api/pandas.melt.html
# https://plotly.com/python/px-arguments/
#
# plotly bar charts:
# https://plotly.com/python/bar-charts/
#
# plotly color:
# https://plotly.com/python/colorscales/
# https://plotly.com/python/builtin-colorscales/#builtin-sequential-color-scales
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
        exam1_average=[89.7, 63.4, 72.6, 96.3, 69.2],
        exam2_average=[82.5, 56.8, 69.2, 86.9, 54.2],
        final_average=[91.2, 68.2, 79.3, 91.1, 75.7],
    )
)

# pandas conversion of the original dataframe into a tidy dataframe
tidy_df = df.melt(id_vars=['major_names'],
                  value_vars=['exam1_average', 'exam2_average', 'final_average'],
                  var_name='exam_type',
                  value_name='exam_grade')

# instantiate a plotly express bar chart using the tidy dataframe
fig = px.bar( tidy_df, x='major_names',
                       y='exam_grade',
                       title='Exam Grades by Major',
                       color='exam_type',
                       color_discrete_sequence=px.colors.sequential.Sunsetdark,

)

# style the pie chart
fig.update_layout(
    barmode='group',
)

# render an html file of the chart and open in default browser
fig.show()
