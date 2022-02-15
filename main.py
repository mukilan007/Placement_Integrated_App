from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/home')
def home():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)
