from flask import Flask
from account.main.loginform import login_blueprint

app = Flask(__name__, template_folder='templates')

app.register_blueprint(login_blueprint, url_perfix="")


if __name__ == "__main__":
    app.run(debug=True)

