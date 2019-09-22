# -*- coding: utf-8 -*-
import requests
from common.login import Login
import json


class Request:
    def __init__(self):
        self.s = requests.Session()
        self.token = Login().token()
        self.headers = {
            'Token': self.token
        }

    # post 请求
    def post(self, url, data):
        result = self.s.post(url, data=data, headers=self.headers)
        return json.loads(result.text)
