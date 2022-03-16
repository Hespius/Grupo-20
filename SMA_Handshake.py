import os
import time

import pandas
from flask import Flask

class Cliente:
    #funcao de cadastro do cliente 
    #funcao pedido
    #função acompanhamento

class Produto:
 #FUNCAO CADASTRO
 #FUNCAO ESTOQUE
 #FUNCAO ARMAZENAR SAFRA 
 #FUNCAO DESPACHAR PEDIDO

app = Flask(__name__)

@app.route("/olamundo", methods=["GET"])
def ola_mundo():
    return {"key": "ola mundo"}

app.run()