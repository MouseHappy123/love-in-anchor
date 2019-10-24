# -*- coding: utf-8 -*-
from flask_restful import Resource
from utils import checkLogin

class checkWXLogin(Resource):
    def get(self):
        return checkLogin()
