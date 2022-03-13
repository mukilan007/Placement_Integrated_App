from flask import request


class Register:
    def __init__(self):
        self.data = {
            "first_name": request.form["first_name"],
            # "last_name": request.form["last_name"],
            "email": request.form["E-mail"],
            "password": request.form["password"],
            # "contact_no": request.form["contact_no"]
        }

    def sign_up(self):
        return self.data