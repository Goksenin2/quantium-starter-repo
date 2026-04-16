from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# 1. Load the squished data you made in the last step
df = pd.read_csv('formatted_daily_sales.csv')

# 2. Sort the data by date (so the line chart goes in order)
df = df.sort_values(by='date')

# 3. Create the line chart using Plotly
fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time')

# 4. Initialize the Dash web application
app = Dash(__name__)

# 5. Design the layout of the website
app.layout = html.Div(children=[
    html.H1(children='Soul Foods: Pink Morsel Sales Visualizer', style={'textAlign': 'center'}),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 6. Turn on the server! (Using the new, updated command)
if __name__ == '__main__':
    app.run(debug=True)
