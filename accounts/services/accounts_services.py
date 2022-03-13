from flask import request, render_template, session, redirect, jsonify
from accounts.schema.userschema import Register
from metadata.main import db_account


class AccountService():
    """
            This service is used to maintain the account of the user
    """

    def signin(self):
        """
                redirecting to user signin page
        """
        return render_template("login.html")

    def create_account(self):
        """
                redirecting to new user signup page
        """
        return render_template("register.html")

    def db_register(self):
        """
                getting information from signup page,
                comparing to DB collection and creating new account
        :return: redirecting to new user home page
        """
        respond = Register().sign_up()
        if db_account.UserMetadata.find_one({"email": respond['email']}):
            return jsonify({"error": "Email address already exist"}), 400
        # respond['password'] = fernet.encrypt(respond["password"].encode())
        db_account.UserMetadata.insert_one(respond)
        return render_template("homepage.html")

    def login_view(self):
        user_email = request.form['Email']
        user_password = request.form['Password']
        db_email = list(db_account.UserMetadata.find({"email": f"{user_email}"}))
        value = None
        db_password = None
        for i in db_email:
            value = i["email"]
            # db_password = fernet.decrypt(i["password"]).decode()
            db_password = i['password']
        if user_email == value and user_password == db_password:
            # session['user'] = db_email
            # for i in db_email:
            #     session['id'] = i["_id"]
            return render_template("homepage.html")
        return "Incorrect email id or password, Try Again... "

    # if len(user)>0:

    def logout_view(self):
        session.pop('user_email')
        return redirect('/login')

    # def get_account(self):
