import pandas as pd
import plotly.express as px
dfb = pd.read_csv("MOCK_DATA.csv")

df = px.data.tips()
fig = px.pie(dfb, values=dfb.value_counts().values, names='Status', title='Current Status Percentage')
fig.show()