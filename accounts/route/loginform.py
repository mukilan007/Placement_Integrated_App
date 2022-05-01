from flask import Blueprint, render_template

from accounts.services.accounts_services import AccountService
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS

login_blueprint = Blueprint(BlueprintName.LOGIN, __name__, static_folder='static', template_folder='templates')


def self_service():
    return AccountService()


def create_account():
    service = self_service()
    return service.db_register()


def user_login():
    service = self_service()
    return service.login_view()


def logout():
    service = self_service()
    return service.logout_view()


def delete():
    service = self_service()
    return service.remove()


login_blueprint.add_url_rule(rule="/create/account", endpoint=Endpoint.CREATE_ACCOUNT, view_func=create_account, methods=[HTTP_REQUESTS_CONSTANTS.POST])
login_blueprint.add_url_rule(rule="/home", endpoint=Endpoint.USER_LOGIN, view_func=user_login, methods=[HTTP_REQUESTS_CONSTANTS.POST])
login_blueprint.add_url_rule(rule="/logout", endpoint=Endpoint.LOGOUT, view_func=logout, methods=[HTTP_REQUESTS_CONSTANTS.GET])
login_blueprint.add_url_rule(rule="/delete", endpoint="delete", view_func=delete, methods=[HTTP_REQUESTS_CONSTANTS.DELETE])


