# -*- coding: utf-8 -*-
# http://flask.pocoo.org/docs/0.12/tutorial/setup/#tutorial-setup
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # instancia da aplicação
app.config.from_object(__name__) # carrega a configura para esse arquivo

# carrega as configuraçoes defalts e sobrescreve as variaveis de desenvolvimento
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# def connect_db():
#     """Connects to the specific database."""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv

@app.route("/")
def hello():
    return "Hello world"

@app.route("/<name>") # nome da page
def nome(name): # metodo, e pode receber parametro
    # nao deu certo
    return "Olá {}".format(name)

if __name__ == "__main__":
    app.run()


