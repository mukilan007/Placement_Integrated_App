from flask import Blueprint, request, render_template, session, redirect
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS
from cryptography.fernet import Fernet

login_blueprint = Blueprint(BlueprintName.LOGIN, __name__, static_folder='static', template_folder='templates')

key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
fernet = Fernet(key)


def login():
    return render_template("login.html")


def register():
    return render_template("register.html")


def user_login():
    user_email = request.form['Email']
    user_password = request.form['Password']
    if user_email == "mukilan007k@gmail.com":
        session['user_email'] = user_email
        return render_template("homepage.html")
    return f"<h1> {user_email} </h1>"
# if len(user)>0:


def logout():
    session.pop('user_email')
    return redirect('/login')


login_blueprint.add_url_rule(rule="/login", endpoint=Endpoint.LOGIN, view_func=login)
login_blueprint.add_url_rule(rule="/register", endpoint=Endpoint.REGISTER, view_func=register)
login_blueprint.add_url_rule(rule="/home", endpoint=Endpoint.USERLOGIN, view_func=user_login,
                             methods=[HTTP_REQUESTS_CONSTANTS.POST])
login_blueprint.add_url_rule(rule="/logout", endpoint=Endpoint.LOGOUT, view_func=logout)
