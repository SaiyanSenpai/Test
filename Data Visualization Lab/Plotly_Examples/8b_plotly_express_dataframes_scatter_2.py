# plotting from csv data
#
# plotly scatter plot charts:
# https://plotly.com/python/line-and-scatter/
import plotly.express as px
import pandas as pd
import os

# set current working directory path and filename variables
path = os.getcwd()
out_file = 'students.csv'

# instantiate a pandas dataframe with a dictionary
df = pd.DataFrame(
    dict(
        names=['jim', 'tony', 'karen', 'lisa', 'lars', 'sven', 'joan', 'mark', 'sara', 'rob'],
        gpa=[3.53, 2.82, 3.40, 2.11, 3.21, 2.25, 3.83, 2.49, 1.16, 3.10],
        age=[18, 19, 17, 19, 20, 65, 24, 17, 20, 20],
        semester=[1, 4, 3, 8, 5, 2, 4, 6, 8, 7]
    )
)

# instantiate a plotly express scatter plot using the dataframe input data
fig = px.scatter( df, x='names',
                      y='semester',
                      color='gpa',
                      size='age',
                      title='Students'
)

# render an html file of the chart and open in default browser
fig.show()


# export tidy data version
df.to_csv(path+"/data/"+out_file, index=False)
