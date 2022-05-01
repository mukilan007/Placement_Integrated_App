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

    # def restaurant_sign_up(self):
    #     data = {
    #         'Vendor_Prefix':
    #         'Name_of_Vendor':
    #     'Vendor_Address':
    #     'Vendor_Country':
    #     'Vendor_State':
    #     'Vendor_City':
    #     'Vendor_Pincode':
    #     'Vendor_Personal_Contact_No':
    #     'Vendor_Personal_Email_Id':
    #     'Vendor_PAN_No':
    #     'Vendor_Upload_Pan_Document':
    #
    #     }
