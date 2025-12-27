import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [150, 200, 250, 300, 220],
    'Profit': [50, 70, 90, 120, 100]
})

# Create interactive bar chart
fig = px.bar(
    data, 
    x='Month', 
    y='Sales', 
    text='Profit',   # Shows profit on hover
    hover_data=['Profit']  # Extra info on hover
)

fig.update_traces(marker_color='skyblue', hovertemplate='Month: %{x}<br>Sales: %{y}<br>Profit: %{customdata[0]}')
fig.show()
