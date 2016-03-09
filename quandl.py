import Quandl 
import numpy as np
from bokeh.plotting import figure, show, output_file, vplot

def datetime(x):
    return np.array(x, dtype=np.datetime64)

stock_name = "YHOO"
#stock_name = "GOOG"
stock_call  = "WIKI/"+stock_name

key_calls =["Open", "High", "Low", "Close", "Adj. Open", "Adj. High", "Adj. Low", "Adj. Close"]
key_names =["Opening", "High", "Low", "Closing", "Adjust Opening", "Adjust High", "Adjust Low", "Adjust Closing"]
index = key_calls.index("Adj. Open")
key_call   = key_calls[index]
key_name   = key_names[index]

in_data = Quandl.get(stock_call, collapse="yearly")

#print in_data.dtypes

p = figure(x_axis_type = "datetime")
p.title = "Stock Price Data from Quandl"
p.grid.grid_line_alpha=0.3
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = key_name + ' Price [$]'

p.line(datetime(in_data[key_call].index), in_data[key_call], line_color='blue', line_width=2, legend='%s' % stock_name)
output_file("stocks.html", title="Quandl")
show(p)  # open a browser
