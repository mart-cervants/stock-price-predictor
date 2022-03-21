from logging import debug
from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route('/') # used for initial test
def home(): # used for initial test
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])  
def predict():
    if request.method == 'POST':
        Open = request.form.get('Open')
        High = request.form.get('High')
        Low = request.form.get('Low')
        AdjClose = request.form.get('AdjClose')
        Volume = request.form.get('Volume')


    prediction = utils.preprocess(Open, High, Low, AdjClose, Volume)

    return render_template('./predictions.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)