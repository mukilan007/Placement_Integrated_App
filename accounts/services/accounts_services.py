from flask import request, render_template, session, redirect, jsonify
from accounts.schema.userschema import Register
from metadata.main import db_account


class AccountService():
    """
    This service is used to maintain the account of the user
    """

    def  signin(self):
        return render_template("login.html")

    def create_account(self):
        return render_template("register.html")

    def db_register(self):
        respond = Register().sign_up()
        if db_account.UserMetadata.find_one({"email": respond['email']}):
            return jsonify({"error": "Email address already exist"}), 400
        # respond['password'] = fernet.encrypt(respond["password"].encode())
        db_account.UserMetadata.insert_one(respond)
        return render_template("homepage.html")

    def login_view(self):
        user_email = request.form['Email']
        user_password = request.form['Password']
        if user_email == "mukilan007k@gmail.com":
            session['user_email'] = user_email
            return render_template("homepage.html")
        return f"<h1> {user_email} </h1>"

    # if len(user)>0:

    def logout_view(self):
        session.pop('user_email')
        return redirect('/login')

    # def get_account(self):
