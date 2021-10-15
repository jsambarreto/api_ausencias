from flask import Flask
import json

import connection as cn 
app = Flask(__name__)

@app.route('/escola')
def escola():
    name_tabela = 'DASHBOARD_ausencias'
    result = cn.recupera_dados(name_tabela)
    return result

@app.route('/escola/<id>')
def escola_id(id=0):
    name_tabela = 'DASHBOARD_ausencias'
    result = cn.recupera_dados_id(name_tabela, id)
    return result

@app.route('/escola/<id>/<ano>')
def escola_id_ano(id=0, ano=0):
    name_tabela = 'DASHBOARD_ausencias'
    result = cn.recupera_dados_ano(name_tabela, id, ano)
    return result