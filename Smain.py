# stock_graph.py
import yfinance as yf
from bokeh.plotting import figure
from bokeh.embed import json_item
from bokeh.models import HoverTool
import datetime

def generate_stock_graph(stock_name):
    # Fetch stock data
    stock_data = yf.Ticker(stock_name)
    hist = stock_data.history(period="1mo")  # Last month’s data

    # Prepare data for Bokeh
    dates = hist.index
    close_prices = hist['Close']

    # Create a Bokeh figure
    p = figure(title=f"{stock_name} Stock Price", x_axis_label="Date", y_axis_label="Price (USD)",
               x_axis_type="datetime", plot_width=800, plot_height=400)

    # Line plot with circle markers for close prices
    p.line(dates, close_prices, legend_label="Close Price", line_width=2)
    p.circle(dates, close_prices, size=6, color="red", alpha=0.6)

    # Add hover tool
    hover = HoverTool(tooltips=[("Date", "@x{%F}"), ("Price", "@y{$0,0.00}")],
                      formatters={'@x': 'datetime'}, mode='vline')
    p.add_tools(hover)

    # Convert to JSON format for embedding
    return json_item(p, "stock_plot")