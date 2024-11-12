import plotly.graph_objects as go

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Create a figure
fig = go.Figure()

# Add a line chart trace
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Line Chart'))

# Update the layout (optional)
fig.update_layout(
    title='Simple Line Chart with Plotly',
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    template='plotly_dark'  # optional, you can change the template to any other
)

# Show the figure
fig.show()