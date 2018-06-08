from flask import render_template, flash
from app import app, db

from app.models.forms import LoginForm
from app.models.tables import User
from flask_login import login_user

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first
        print(user)

        import pdb; pdb.set_trace()
        if user() and user().password == form.password.data:
            print(form.password.data, user().password)
            login_user(user)
            flash("Logger in.")
    else:
        flash("Invalid login.")
        print(form.errors)
    return render_template('login.html', form=form)

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(username="Vanosk").first()
    print(r.email, r.name)
    return "OK"
    #
    # i = User("teste", "123", "Teste Nunes", "teste@hotmail.com")
    # db.session.add(i)
    # db.session.commit()
    # return "OK"