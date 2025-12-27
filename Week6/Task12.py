# Install dash if not installed
# pip install dash plotly pandas

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [150, 200, 250, 300, 220],
    'Profit': [50, 70, 90, 120, 100],
    'Expenses': [80, 120, 130, 160, 140]
})

# Create charts
fig1 = px.bar(data, x='Month', y='Sales', hover_data=['Profit'], title="Monthly Sales")
fig2 = px.line(data, x='Month', y='Profit', hover_data=['Sales'], title="Monthly Profit Trend")
fig3 = px.area(data, x='Month', y='Expenses', hover_data=['Sales'], title="Monthly Expenses")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout: combine multiple charts
app.layout = html.Div([
    html.H1("Company Dashboard"),
    html.Div([
        dcc.Graph(figure=fig1, style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(figure=fig2, style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(figure=fig3, style={'display': 'inline-block', 'width': '33%'})
    ])
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
