from constants import Random
from cryptography.fernet import Fernet
from flask import jsonify, session
from functools import wraps

fernet = Fernet(Random.SECRET_KEY)
# app.config['SECRET_KEY'] = Random.SECRET_KEY


# def token_validate(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         token = request.args.get('token')
#
#         if not token:
#             return jsonify({'message': 'you have not logged in'}), 403
#
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify({'message': 'your session was expired. Login again'}), 403
#
#         return f(*args, **kwargs)
#
#     return wrap

def token_validate(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'payload' in session:
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "you need to login"})
    return wrap
