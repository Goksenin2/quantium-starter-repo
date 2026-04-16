from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# 1. Load the squished data
df = pd.read_csv('formatted_daily_sales.csv')
df = df.sort_values(by='date')

# 2. Initialize the Dash web application
app = Dash(__name__)

# 3. Define our Custom Styling (The "CSS" part)
colors = {
    'background': '#F2F2F2', # Light gray background
    'text': '#333333',       # Dark gray text
    'accent': '#E91E63'      # Pink Morsel Pink!
}

# 4. Design the layout: Header, Radio Buttons, and Chart
app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding': '40px', 'fontFamily': 'Helvetica, Arial, sans-serif'}, children=[
    
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer', 
        style={'textAlign': 'center', 'color': colors['text']}
    ),
    
    # The new Radio Button picker
    html.Div([
        dcc.RadioItems(
            id='region-picker',
            options=['north', 'east', 'south', 'west', 'all'],
            value='all', # This is what it selects by default
            inline=True,
            style={'fontSize': '20px', 'color': colors['accent'], 'textAlign': 'center', 'marginBottom': '20px'}
        )
    ]),

    # The Graph (We leave the figure blank here because the callback will fill it)
    dcc.Graph(id='sales-line-chart')
])

# 5. The Callback (The machinery that makes the radio buttons work)
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    # Filter the data based on the button clicked
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
        
    # Redraw the line chart
    fig = px.line(filtered_df, x='date', y='sales', title=f'Sales for Region: {selected_region.capitalize()}')
    
    # Add our custom colors to the chart itself
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    
    return fig

# 6. Turn on the server!
if __name__ == '__main__':
    app.run(debug=True)
