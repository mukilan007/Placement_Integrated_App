from flask import Blueprint, render_template

from accounts.services.accounts_services import AccountService
from constants import BlueprintName, Endpoint, HTTP_REQUESTS_CONSTANTS

dish_blueprint = Blueprint(BlueprintName.LOGIN, __name__, static_folder='static', template_folder='templates')

# dish_blueprint.add_url_rule(rule="/add/food", endpoint=Endpoint.CREATE_ACCOUNT, view_func=create_account, methods=[HTTP_REQUESTS_CONSTANTS.POST])
# dish_blueprint.add_url_rule(rule="/update/food", endpoint=Endpoint.USER_LOGIN, view_func=user_login, methods=[HTTP_REQUESTS_CONSTANTS.POST])
# dish_blueprint.add_url_rule(rule="/delete/food", endpoint=Endpoint.LOGOUT, view_func=logout, methods=[HTTP_REQUESTS_CONSTANTS.GET])
# dish_blueprint.add_url_rule(rule="/remove/all", endpoint="delete", view_func=delete, methods=[HTTP_REQUESTS_CONSTANTS.DELETE])
