from datetime import datetime
from constants import DBDetail, Date


class admin:
    def __init__(self, payload):
        self.user_detail = self.session(payload)

    def session(self, payload):
        for i in payload["payload"]:
            self.user_detail[DBDetail.ID] = i[DBDetail.ID]
            self.user_detail[DBDetail.NAME] = i[DBDetail.FIRST_NAME]
            self.user_detail['email id'] = i[DBDetail.E_MAIL_ID]

    def created_by(self):
        return self.user_detail

    def created_at(self):
        return datetime.now()

    def modified_by(self):
        return self.user_detail

    def modified_at(self):
        return datetime.now()

    def user_id(self):
        a = self.user_detail
        return a['user_id']
