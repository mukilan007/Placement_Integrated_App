from base.schema.dateandtime.livetime import admin
from constants import HTMLUserDetail, DBDetail
from flask import request


class Register:
    def __init__(self, payload):
        # super().__init__(payload)
        self.session = payload
        # ser = , admin()
        self.data = {
            DBDetail.FIRST_NAME: request.form[HTMLUserDetail.FIRST_NAME],
            DBDetail.LAST_NAME: request.form[HTMLUserDetail.LAST_NAME],
            DBDetail.E_MAIL_ID: request.form[HTMLUserDetail.E_MAIL_ID],
            DBDetail.PASSWORD: request.form[HTMLUserDetail.PASSWORD],
            DBDetail.CONTACT_NUMBER: request.form[HTMLUserDetail.CONTACT_NUMBER],
            # DBDetail.CREATED_BY: ser.created_by(),
            # DBDetail.CREATED_AT: ser.created_at(),
            # DBDetail.MODIFIED_BY: ser.modified_by(),
            # DBDetail.MODIFIED_AT: ser.modified_at(),
            DBDetail.DELETED: False
        }

    def sign_up(self):
        return self.data
