import requests
import simplejson as json
import numpy as np
from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, show, save, output_file, vplot
from bokeh.embed import components

app = Flask(__name__)
app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  if request.method == "GET":
    return render_template('index.html')
  else:
    app.vars['stock'] = request.form['stock']    
    app.vars['key'] = request.form['key']
    ### Read data
    MyAPIKey = "95ujF6cdywLzzj9uPSeS"
    api_url = 'https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=%s' % (app.vars['stock'], MyAPIKey)
    json_data = requests.get(api_url)
    try:
      data_list =  zip(*json_data.json()['dataset']['data'])
    except:
      return render_template('error.html')

    key_calls = [x.encode('UTF8') for x in json_data.json()['dataset']['column_names']]
    try :
        index = key_calls.index(app.vars['key'])
    except :
      return render_template('error.html')

    date = np.array(list(data_list[0]), dtype=np.datetime64)
    in_data = np.asarray(data_list[index])

    #Bokeh plot
    plot = figure(x_axis_type = "datetime")
    plot.title = "Stock Price Data from Quandl"
    plot.grid.grid_line_alpha=0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = app.vars['key'] + ' Price [$]'
    
    plot.line(date, in_data, line_color='blue', line_width=2, legend='%s' % app.vars['stock'])

    script, div = components(plot)
    return render_template('graph.html', name=app.vars['stock'], script=script, div=div)
    
if __name__ == '__main__':
  #app.run(debug=True)
  app.run((host='0.0.0.0')
