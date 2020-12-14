from sdarotApi import get_cookie, get_token_for_cookie
from datetime import datetime


class Token:
    cookie = ""
    token = ""
    created_time = ""

    def __init__(self):
        self.cookie = get_cookie()
        self.generate_new_token()

    def generate_new_token(self):
        self.token = get_token_for_cookie(self.cookie)
        self.created_time = datetime.now()
