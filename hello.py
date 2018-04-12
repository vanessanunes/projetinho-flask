# -*- coding: utf-8 -*-
from flask import Flask

'''
mkvirtualenv flask -> para criar 
virtualenv flask -> para rodar
http://127.0.0.1:5000/ -> para acessar
para sair da lenv -> deactivate

pego por: http://www.devfuria.com.br/python/flask/
ver também: http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html
'''

app = Flask("projetinho")

@app.route("/")
def hello():
    return "Hello world"

@app.route("/<name>") # nome da page
def nome(name): # metodo, e pode receber parametro
    # nao deu certo
    return "Olá {}".format(name)

if __name__ == "__main__":
    app.run()


