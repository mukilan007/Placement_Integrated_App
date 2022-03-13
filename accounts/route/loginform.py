from flask import Blueprint

from accounts.services.accounts_services import AccountService
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS
from cryptography.fernet import Fernet

login_blueprint = Blueprint(BlueprintName.LOGIN, __name__, static_folder='static', template_folder='templates')

key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
fernet = Fernet(key)


def self_service_instance():
    return AccountService()


def login():
    service = self_service_instance()
    return service.signin()


def register():
    service = self_service_instance()
    return service.create_account()


def create_account():
    service = self_service_instance()
    return service.db_register()


def user_login():
    service = self_service_instance()
    return service.login_view()


# if len(user)>0:


def logout():
    service = self_service_instance()
    return service.logout_view()


login_blueprint.add_url_rule(rule="/login", endpoint=Endpoint.LOGIN, view_func=login)
login_blueprint.add_url_rule(rule="/register", endpoint=Endpoint.REGISTER, view_func=register)
login_blueprint.add_url_rule(rule="/create/account", endpoint=Endpoint.CREATE_ACCOUNT, view_func=create_account, methods=[HTTP_REQUESTS_CONSTANTS.POST])
login_blueprint.add_url_rule(rule="/home", endpoint=Endpoint.USERLOGIN, view_func=user_login,
                             methods=[HTTP_REQUESTS_CONSTANTS.POST])
login_blueprint.add_url_rule(rule="/logout", endpoint=Endpoint.LOGOUT, view_func=logout)
