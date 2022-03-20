from flask import Flask, render_template
from flask import request
import main
import InvestApi
import requests

def toViewList(dictList):
    table = []
    for year in dictList:
        for id in dictList[year].keys():
            str = []
            bond = InvestApi.getIdBonds(id)
            str.append(year)
            str.append(bond['name'])
            str.append(int(dictList[year][id]))
            str.append(bond['price'])
            table.append(str)
    return table


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/process_data/', methods=['POST'])
def doit():
    money = request.form['money']
    year = request.form['year']
    g = main.getDictUserBuy(year,money)
    return render_template('admin.html', bonds = toViewList(g))

app.run()