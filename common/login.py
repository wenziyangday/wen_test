# -*- coding: utf-8 -*-
import requests


class Login:
    def __init__(self):
        self.url = ''
        self.data = {}

    def token(self):
        result = requests.post(self.url, data=self.data)
        return result
