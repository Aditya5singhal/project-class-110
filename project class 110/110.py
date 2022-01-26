import pandas as pd
import plotly.figure_factory as px
import csv
import statistics
import random
df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()

fig=px.create_distplot([data],['reading_time'],show_hist=False)
fig.show()
mean1=statistics.mean(data)
stdiv=statistics.stdev(data)
print("The mean is: - ",mean1)
print(stdiv)


dataset=[]
for i in range(0,100):
    randomnos=random.randint(0,len(data))
    value=data[randomnos]
    dataset.append(value)
mean1=statistics.mean(dataset)
print(mean1)
stdiv=statistics.stdev(dataset)
print(stdiv)
fig=px.create_distplot([dataset],['dataset'],show_hist=False)
fig.show()


