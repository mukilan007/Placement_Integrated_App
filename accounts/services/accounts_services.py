from accounts.schema.userschema import Register
from base.auth.Authentication import token_validate, fernet
from bson.objectid import ObjectId
from constants import HTMLUserDetail, DBDetail
from flask import request, render_template, session, redirect, jsonify, make_response, json
from json import dumps
from metadata.main import db_account


class AccountService:
    """
            This service is used to maintain the account of the user
    """
    def __init__(self):
        self.session = None

    def db_register(self):
        """
                getting information from signup page,
                comparing to DB collection and creating new account
                :return: redirecting to new user home page
        """
        respond = Register(self.session).sign_up()
        if db_account.UserMetadata.find_one({DBDetail.E_MAIL_ID: respond['email']}):
            return jsonify({"error": "Email address already exist"}), 400
        respond[DBDetail.PASSWORD] = fernet.encrypt(respond[HTMLUserDetail.PASSWORD].encode())
        db_account.UserMetadata.insert_one(respond)
        return render_template("homepage.html")

    @staticmethod
    def login_view():
        payloads = request.form
        user_email = request.form['E-mail']
        user_password = request.form['password']
        payload = list(db_account.UserMetadata.find({DBDetail.E_MAIL_ID: f"{user_email}"}))
        db_email = None
        db_password = None
        for i in payload:
            db_email = i[DBDetail.E_MAIL_ID]
            db_password = fernet.decrypt(i[DBDetail.PASSWORD]).decode()
            i[DBDetail.ID] = str(i[DBDetail.ID])
        if user_email == db_email and user_password == db_password:
            session["payload"] = payload
            for i in payload:
                session[DBDetail.ID] = i[DBDetail.ID]
                session[DBDetail.FIRST_NAME] = i[DBDetail.FIRST_NAME]
            # token = jwt.encode({'user': payload, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},
            #                    app.config['SECRET_KEY'])
            # jsonify({'token': token.decode('UTF-8')})
            return render_template("homepage.html")
        return make_response(jsonify(f"{payloads}"), 500)

    # if len(user)>0:

    @token_validate
    def remove(self):
        try:
            user_id = session[DBDetail.ID]
            name = session[DBDetail.FIRST_NAME]
            db_account.UserMetadata.delete_one({DBDetail.ID: ObjectId(user_id)})
            session.clear()
            return dumps(f"{name} thanks for using Quick food, and your account was deleted")
        except Exception:
            return dumps("cannot find the account. please entered the valid details")

    @token_validate
    def logout_view(self):
        session.clear()
        return render_template("login.html")

    # def get_account(self):
