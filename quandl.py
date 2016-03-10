import requests
import simplejson as json
import numpy as np
from bokeh.plotting import figure, show, save, output_file, vplot


def stock_plot(stock, key):
    MyAPIKey = "95ujF6cdywLzzj9uPSeS"
    api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=%s' % (stock, MyAPIKey)
    try:
        json_data = requests.get(api_url)
    except:
        return False, "Stock Name is not correct."

    #print json_data.json()['dataset']['column_names']
    data_list =  zip(*json_data.json()['dataset']['data'])
    key_calls = [x.encode('UTF8') for x in json_data.json()['dataset']['column_names']]
    try :
        index = key_calls.index(key)
    except :
        return False, "Data Key is not correct."

    date = np.array(list(data_list[0]), dtype=np.datetime64)
    in_data = np.asarray(data_list[index])

    p = figure(x_axis_type = "datetime")
    p.title = "Stock Price Data from Quandl"
    p.grid.grid_line_alpha=0.3
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = key + ' Price [$]'
    
    p.line(date, in_data, line_color='blue', line_width=2, legend='%s' % stock)
    output_file("templates/stocks.html", title="Quandl")
    save(p)  # open a browser
    return True,"Good Job"


if __name__=="__main__":    
    stock_plot("YHOO","Open")
