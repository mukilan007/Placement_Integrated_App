from flask import Flask, render_template, request
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


@app.route('/login', methods=['POST'])
def homepage():
    user_email = request.form['Email']
    user_password = request.form['Password']
    if user_email == "mukilan007k@gmail.com":
        return render_template("homepage.html")
    return f"<h1> {user_email} </h1>"


if __name__ == "__main__":
    app.run(debug=True)
