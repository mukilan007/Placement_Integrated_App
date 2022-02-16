import os

from account.main.loginform import login_blueprint
from flask import Flask, redirect
from pymongo import MongoClient

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

app.register_blueprint(login_blueprint, rule="/placement/BIT")


@app.route('/')
def home():
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)

