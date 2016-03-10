from flask import Flask, render_template, request, redirect
import quandl as quandl

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
    success = quandl.stock_plot(app.vars['stock'], app.vars['key'])
    if success:
      return render_template('stocks.html')
    else:
      return render_template('error.html')
    
if __name__ == '__main__':
  app.run(debug=True)
