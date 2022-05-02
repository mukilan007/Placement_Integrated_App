from flask import Blueprint, request, json

from restaurant_login.services.restaurant_service import AccountService
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS

restaurant_blueprint = Blueprint(BlueprintName.RESTAURANT, __name__, static_folder='static', template_folder='templates')


def self_service():
    return AccountService()


def create_account():
    payload = request.form.to_dict()
    service = self_service()
    return service.Restaurant_db_register(payload)


def user_login():
    payload = request.form.to_dict()
    service = self_service()
    return service.Restaurant_login_view(payload)


def logout():
    service = self_service()
    return service.Restaurant_logout_view()


def delete():
    service = self_service()
    return service.Restaurant_remove()


restaurant_blueprint.add_url_rule(rule="/create/account", endpoint=Endpoint.CREATE_ACCOUNT, view_func=create_account, methods=[HTTP_REQUESTS_CONSTANTS.POST])
restaurant_blueprint.add_url_rule(rule="/home", endpoint=Endpoint.USER_LOGIN, view_func=user_login, methods=[HTTP_REQUESTS_CONSTANTS.POST])
restaurant_blueprint.add_url_rule(rule="/logout", endpoint=Endpoint.LOGOUT, view_func=logout, methods=[HTTP_REQUESTS_CONSTANTS.GET])
restaurant_blueprint.add_url_rule(rule="/delete", endpoint="delete", view_func=delete, methods=[HTTP_REQUESTS_CONSTANTS.DELETE])
