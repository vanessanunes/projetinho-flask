from flask import render_template
from app import app

# @app.route("/")
# # @app.route("/index")
# def index():
#     return 'Hello'

@app.route("/index/<user>")
@app.route("/index/", defaults={'user':None})
def index(user):
    return render_template('base.html', user=user)

@app.route("/login")
def login():
    return render_template('base.html')