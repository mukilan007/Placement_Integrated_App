from flask import request


class Register:
    def __init__(self):
        self.data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["E-mail"],
            "password": request.form["password"],
            "contact_no": request.form["contact_no"],
            # "created_by": created_by(),
            # "created_at": created_at(),
            # "modified_by": modified_by(),
            # "modified_at": modified_at(),
            "is_deleted": False
        }

    def sign_up(self):
        return self.data