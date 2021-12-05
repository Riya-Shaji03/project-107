import pandas as pd
import csv
import plotly_express as pe
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
mean = df.groupby(['student_id','level'], as_index = False)['attempt'].mean()


scatter = pe.scatter( mean, 
x = 'student_id', 
y = 'level',
size = 'attempt',
color = 'attempt')
scatter.show()




