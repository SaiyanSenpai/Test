print("Q1)")
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
result = [n**2 for n in squares]

fig, ax = plt.subplots()
ax.plot(result, linewidth=2)

ax.set_title("Square Numbers")

ax.tick_params(axis='both')
plt.show()


print("\nQ2)")
import plotly.express as px
import pandas as pd

# instantiate a pandas dataframe
df = pd.DataFrame({
    'Sales Associates':['Mark', 'Ada', 'Khan', 'Xie', 'Zoe'],
    'April 2021':[285, 190, 395, 370, 295],
})

# instantiate a plotly express bar chart from a panda dataframe
fig = px.bar( df, x=df["April 2021"], y=df["Sales Associates"],title="Monthly Sales in Thousands of $")

# render an html file of the chart and open in default browser
fig.show()



print("\nQ3)")

import matplotlib.pyplot as plt
car_age = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
car_price = [40,37,37,35,33,32,34,30,29,29,28,27,27,26,25,25,24,23,22,20]

plt.scatter(car_age, car_price)
plt.gca().update(dict(title='Car Age in Years', xlabel='Toyota Camry Price Decline with Age', ylabel='Price in $k', s=30, alpha = .5, ylim=(0,10)))

plt.show()