import requests
import simplejson as json
import numpy as np
from bokeh.plotting import figure, show, save, output_file, vplot
from bokeh.embed import components

def stock_plot(stock, key):
    MyAPIKey = "95ujF6cdywLzzj9uPSeS"
    api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=%s' % (stock, MyAPIKey)
    json_data = requests.get(api_url)
    try:
        data_list =  zip(*json_data.json()['dataset']['data'])
    except:
        return False, 0, 0
    key_calls = [x.encode('UTF8') for x in json_data.json()['dataset']['column_names']]
    index = key_calls.index(key)

    date = np.array(list(data_list[0]), dtype=np.datetime64)
    in_data = np.asarray(data_list[index])

    plot = figure(x_axis_type = "datetime")
    plot.title = "Stock Price Data from Quandl"
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = key + ' Price [$]'
    
    plot.line(date, in_data, line_color='blue', line_width=2, legend='%s' % stock)
    script, div = components(plot)
    return True, script, div


if __name__=="__main__":    
    stock_plot("YHOO","Open")
