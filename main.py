import os

from accounts.route.loginform import login_blueprint
from redirect.route.redirectapi import redirect_blueprint
from restaurant_login.route.restaurant_login import restaurant_blueprint
from flask import Flask, redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

app.register_blueprint(login_blueprint, url_prefix="/BIT/Quickfood/account")
app.register_blueprint(redirect_blueprint, url_prefix="/BIT/Quickfood/2")
app.register_blueprint(restaurant_blueprint, url_prefix="/BIT/Quickfood/restaurant")


@app.route('/')
def home():
    return redirect('/BIT/Quickfood/2/login')


if __name__ == "__main__":
    app.run(debug=True)
