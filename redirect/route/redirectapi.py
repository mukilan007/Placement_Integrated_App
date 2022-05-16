from flask import Blueprint, render_template

from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS

redirect_blueprint = Blueprint(BlueprintName.REDIRECT, __name__, static_folder='static', template_folder='templates')


def login():
    """
            redirecting to user signin page
    """
    return render_template("login.html")


def register():
    """
            redirecting to new user signup page
    """
    return render_template("register.html")


def new_register():
    return render_template("new_restaurant.html")


def restaurant_login():
    return render_template("restaurant_login.html")


def new_feedback():
    return render_template("feedback.html")


def homepage():
    return render_template("homepage.html")




redirect_blueprint.add_url_rule(rule="/login", endpoint=Endpoint.LOGIN, view_func=login,
                                methods=[HTTP_REQUESTS_CONSTANTS.GET])
redirect_blueprint.add_url_rule(rule="new/register", endpoint=Endpoint.NEW_REGISTER, view_func=new_register,
                                methods=[HTTP_REQUESTS_CONSTANTS.GET])
redirect_blueprint.add_url_rule(rule="/register", endpoint=Endpoint.REGISTER, view_func=register,
                                methods=[HTTP_REQUESTS_CONSTANTS.GET])
redirect_blueprint.add_url_rule(rule="/restaurant/login", endpoint=Endpoint.RESTAURANT_LOGIN,
                                view_func=restaurant_login, methods=[HTTP_REQUESTS_CONSTANTS.GET])
redirect_blueprint.add_url_rule(rule="/feedback", endpoint=Endpoint.FEEDBACK, view_func=new_feedback,
                                methods=[HTTP_REQUESTS_CONSTANTS.GET])
redirect_blueprint.add_url_rule(rule="/home", endpoint=Endpoint.HOME, view_func=homepage,
                                methods=[HTTP_REQUESTS_CONSTANTS.GET])
