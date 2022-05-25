from flask import Blueprint, render_template, request, jsonify, make_response

from constants import HTMLUserDetail, DBDetail, Restaurant_DBDetail
from restaurant_login.services.restaurant_service import AccountService
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS
from metadata.main import db_account

project_blueprint = Blueprint(BlueprintName.DISH, __name__, static_folder='static', template_folder='templates')


def get_session():
    AccountService_session = AccountService
    return AccountService_session.get_session()


def add_food():
    payload = request.form.to_dict()
    session = get_session()
    db_account[session].insert_one(payload)
    return render_template('new_user.html')


def search():
    payload = request.form.to_dict()
    # db_account.RestaurantMetadata.createIndex({"location": "text"})
    location = payload["location"]
    # a = db_account.RestaurantMetadata.find({"$text": {"$search": location}})
    a = db_account.RestaurantMetadata.find({"station_location": location})
    return make_response(jsonify(f"{a, location}"), 500)


project_blueprint.add_url_rule(rule="/add/food", endpoint=Endpoint.CREATE_ACCOUNT, view_func=add_food,
                               methods=[HTTP_REQUESTS_CONSTANTS.POST])
project_blueprint.add_url_rule(rule="search", endpoint=Endpoint.SEARCH_REST, view_func=search,
                               methods=[HTTP_REQUESTS_CONSTANTS.POST])
# dish_blueprint.add_url_rule(rule="/update/food", endpoint=Endpoint.USER_LOGIN, view_func=user_login, methods=[HTTP_REQUESTS_CONSTANTS.POST])
# dish_blueprint.add_url_rule(rule="/delete/food", endpoint=Endpoint.LOGOUT, view_func=logout, methods=[HTTP_REQUESTS_CONSTANTS.GET])
# dish_blueprint.add_url_rule(rule="/remove/all", endpoint="delete", view_func=delete, methods=[HTTP_REQUESTS_CONSTANTS.DELETE])
