from flask import Blueprint, request, json

from restaurant_login.services.restaurant_service import AccountService
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS

restaurant_blueprint = Blueprint(BlueprintName.RESTAURANT, __name__, static_folder='static', template_folder='templates')


def self_service():
    return AccountService()


def login():
    service = self_service()
    return service.Restaurant_signin()


def create_account():
    payload = request.form.to_dict()
    service = self_service()
    return service.Restaurant_db_register(payload)


def user_login():
    service = self_service()
    return service.Restaurant_login_view()


def logout():
    service = self_service()
    return service.Restaurant_logout_view()


def delete():
    service = self_service()
    return service.Restaurant_remove()


restaurant_blueprint.add_url_rule(rule="/create/account", endpoint=Endpoint.CREATE_ACCOUNT, view_func=create_account, methods=[HTTP_REQUESTS_CONSTANTS.POST])
