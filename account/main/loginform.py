from flask import Blueprint, request, render_template
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS

login_blueprint = Blueprint(BlueprintName.LOGIN, __name__, static_folder='static', template_folder='templates')


def login():
    return render_template("login.html")

def register():
    return render_template("register.html")


def user_login():
    user_email = request.form['Email']
    user_password = request.form['Password']
    if user_email == "mukilan007k@gmail.com":
        return render_template("homepage.html")
    return f"<h1> {user_email} </h1>"


login_blueprint.add_url_rule(rule="/", endpoint=Endpoint.LOGIN, view_func=login)
login_blueprint.add_url_rule(rule="/register", endpoint=Endpoint.REGISTER, view_func=register)
login_blueprint.add_url_rule(rule="/log_in", endpoint=Endpoint.USERLOGIN, view_func=user_login,
                             methods=[HTTP_REQUESTS_CONSTANTS.POST])
