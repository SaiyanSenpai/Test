# Pandas dataframes
# https://www.w3schools.com/python/pandas/pandas_dataframes.asp
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame(
    dict(
        names=['jim', 'tony', 'karen', 'leia', 'simmon'],
        final_exam_grade=[90,75,86,83,92],
        gpa=[97.5, 88.2, 76.6, 89.3, 82.8]
    )
)

fig = go.Figure(
    data=[
        go.Scatter( x=df.names,
                    y=df.final_exam_grade,
                    mode='markers',
                    marker_color=df.final_exam_grade,
                    marker_size=15,
                    name='final_exam_grade'
        ),
        go.Scatter( x=df.names,
                    y=df.gpa,
                    mode='markers',
                    marker_color='green',
                    marker_size=20,
                    name='gpa'
        )
    ],
    layout=go.Layout(
        title = go.layout.Title(text='People'),
        xaxis = go.layout.XAxis(title='Names'),
        yaxis = go.layout.YAxis(title='Grades')
    )
)

# renderer the display to the browser (the default renderer)
fig.show()
