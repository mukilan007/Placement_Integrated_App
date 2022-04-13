import os

from accounts.route.loginform import login_blueprint
from flask import Flask, redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

app.register_blueprint(login_blueprint, url_prefix="/BIT/NMN/account")


@app.route('/')
def home():
    return redirect('/BIT/NMN/account/login')


if __name__ == "__main__":
    app.run(debug=True)
