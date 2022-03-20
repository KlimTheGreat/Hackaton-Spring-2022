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


application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/process_data/', methods=['POST', 'get'])
def doit():
    money = request.form['money']
    year = request.form['year']
    mainList = main.getDictUserBuy(year,money)
    return render_template('index.html', bonds = toViewList(mainList),result = None)


if __name__ == "__main__":
    application.run(host='0.0.0.0')
