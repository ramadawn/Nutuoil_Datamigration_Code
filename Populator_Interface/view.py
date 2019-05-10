#import flask libraries
from flask import Flask, render_template, request
from display import display

#initialize flask application
app = Flask(__name__)

#template route
@app.route('/')


def student():
   return render_template('index.html')
 

#
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      display(result)
      return "done"
 
#debug mode
if __name__ == '__main__':
   app.run(debug = True)

