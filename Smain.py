# plotly_graph.py
import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio

def generate_graph(stock_name):
    try:
        # Fetch stock data
        stock_data = yf.Ticker(stock_name)
        hist = stock_data.history(period="1mo")

        if hist.empty:
            raise ValueError("No data found for the specified stock.")

        # Prepare data for Plotly
        dates = hist.index
        close_prices = hist['Close']

        # Create a Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=close_prices, mode='lines+markers', name='Close Price',
                                  hovertemplate='Date: %{x}<br>Price: %{y:.2f}<extra></extra>'))

        # Update layout
        fig.update_layout(title=f"{stock_name} Stock Price",
                          xaxis_title="Date",
                          yaxis_title="Price (USD)",
                          hovermode='closest')

        # Convert Plotly figure to JSON
        response = pio.to_json(fig)
        return response

    except Exception as e:
        print(f"Error generating graph: {e}")
        raise
