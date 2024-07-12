import json

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

data = {}
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('index1'))
    
@app.route('/index1', methods=['GET', 'POST'])
def index1():
    if request.method == 'GET':
        return render_template('index1.html')
    else:
        return redirect(url_for('form'))
    
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('index2.html')
    else:
        data['name'] = request.form['name']
        data['email'] = request.form['email']
        with open("data_base.json", "w", encoding='utf-8') as data_base:
            json.dump(data, data_base, ensure_ascii=False, indent=4)
        print(data)
        return render_template('index.html')



if __name__ == "__main__":
    app.run()