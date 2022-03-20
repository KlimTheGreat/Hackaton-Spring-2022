from flask import Flask, render_template
from flask import request
import requests
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/process_data/', methods=['POST'])
def doit():
    index = request.form['money']
    print(index)
    return hello();
app.run()