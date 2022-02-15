from flask import Blueprint, request, render_template, Flask
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS
from main import app

login_blueprint = Blueprint(BlueprintName.LOGIN, __name__)


def user_login():
    user_email = request.form['user email']
    user_password = request.form['user password']
    if user_email == "mukilan007k@gmail.com":
        return "<h1>TEST</>"
    return "<h1>TEST</>"


app.add_url_rule(rule="/log_in", endpoint=Endpoint.USERLOGIN, view_func=user_login,
                            methods=[HTTP_REQUESTS_CONSTANTS.POST])
