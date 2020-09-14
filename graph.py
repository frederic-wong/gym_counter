import pandas as pd
import plotly.express as px

df = pd.read_csv('../gym_counter/logs/data.csv')

fig = px.line(df, x = 'Timestamp', y = 'People', title='Gym counter')
fig.show()
