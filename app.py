from flask import Flask
import json

from connection import recupera_dados,recupera_dados_id

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/escola')
def escola():
    name_tabela = 'DASHBOARD_ausencias'
    result = recupera_dados(name_tabela)
    return result

@app.route('/escola/<id>')
def escola_id(id=0):
    name_tabela = 'DASHBOARD_ausencias'
    result = recupera_dados_id(name_tabela, id)
    return result