from accounts.schema.userschema import Register
from base.auth.Authentication import token_validate, fernet
from bson.objectid import ObjectId
from constants import HTMLUserDetail, DBDetail
from flask import request, render_template, session, redirect, jsonify, make_response, json
from json import dumps
from metadata.main import db_account


class AccountService:
    def __init__(self):
        self.session = None

    def Restaurant_signin(self):
        pass

    def Restaurant_create_account(self):
        pass

    def Restaurant_db_register(self, payload):
        if db_account.RestaurantMetadata.find_one({"vendor_email": payload["vendor_email"]}):
            return jsonify({"error": "Email address already exist"}), 400
        # respond[DBDetail.PASSWORD] = fernet.encrypt(respond[HTMLUserDetail.PASSWORD].encode())
        payload["vendor_pan_no"] = fernet.encrypt(payload["vendor_pan_no"].encode())
        db_account.RestaurantMetadata.insert_one(payload)
        return render_template("new_user.html")

    def Restaurant_login_view(self):
        pass

    def Restaurant_logout_view(self):
        pass

    def Restaurant_remove(self):
        pass
