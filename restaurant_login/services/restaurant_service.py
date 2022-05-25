from accounts.schema.userschema import Register
from base.auth.Authentication import token_validate, fernet
from bson.objectid import ObjectId
from constants import HTMLUserDetail, DBDetail, Restaurant_DBDetail
from flask import request, render_template, session, redirect, jsonify, make_response, json
from json import dumps
from metadata.main import db_account


def get_id(inc_by, _filter):
    inc_updt = {'$inc': {"total_count": inc_by}}
    response = db_account["Restaurant_Counter"].find_one_and_update(_filter, inc_updt, new=True, upsert=True)
    counter = None
    if response:
        counter = response["total_count"]
    return counter


def _generate_rest_id():
    filter_conditions = {"type": "hotel"}
    nxt_count = get_id(inc_by=1, _filter=filter_conditions)
    rest_id = f"REST-{nxt_count}"
    return rest_id


class AccountService:
    @staticmethod
    def get_session():
        return session.get(Restaurant_DBDetail.ID)

    @staticmethod
    def Restaurant_db_register(payload):
        if db_account.RestaurantMetadata.find_one({"vendor_email": payload["vendor_email"]}):
            return jsonify({"error": "Email address already exist"}), 400
        payload[Restaurant_DBDetail.PASSWORD] = fernet.encrypt(payload[Restaurant_DBDetail.PASSWORD].encode())
        payload["vendor_pan_no"] = fernet.encrypt(payload["vendor_pan_no"].encode())
        rest_id = _generate_rest_id()
        payload["_id"] = rest_id
        db_account.RestaurantMetadata.insert_one(payload)
        session["payload"] = list(payload)
        return render_template("new_user.html")

    @staticmethod
    def Restaurant_login_view(payload):
        user_email = payload['E-mail']
        user_password = payload['password']
        db_payload = list(db_account.RestaurantMetadata.find({Restaurant_DBDetail.E_MAIL_ID: f"{user_email}"}))
        db_email = None
        db_password = None
        for i in db_payload:
            db_email = i[Restaurant_DBDetail.E_MAIL_ID]
            db_password = fernet.decrypt(i[Restaurant_DBDetail.PASSWORD]).decode()
        if user_email == db_email and user_password == db_password:
            session["payload"] = db_payload
            for i in db_payload:
                session[Restaurant_DBDetail.ID] = i[Restaurant_DBDetail.ID]
                session[Restaurant_DBDetail.NAME] = i[Restaurant_DBDetail.NAME]
            # token = jwt.encode({'user': payload, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=40)},
            #                    app.config['SECRET_KEY'])
            # jsonify({'token': token.decode('UTF-8')})
            return render_template("new_user.html")
        return make_response(jsonify(f"{payload}"), 500)

    @staticmethod
    def Restaurant_logout_view():
        session.clear()
        return render_template("restaurant_login.html")

    @staticmethod
    def Restaurant_remove():
        try:
            user_id = session[Restaurant_DBDetail.ID]
            name = session[Restaurant_DBDetail.NAME]
            db_account.RestaurantMetadata.delete_one({DBDetail.ID: ObjectId(user_id)})
            session.clear()
            return dumps(f"{name} thanks for using Quick food, and your account was deleted")
        except Exception:
            return dumps("cannot find the account. please entered the valid details")
