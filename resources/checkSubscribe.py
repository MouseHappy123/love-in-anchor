# -*- coding: utf-8 -*-
from flask_restful import Resource
from utils import checkSubscribe

class checkWXSubscribe(Resource):
    def get(self):
        return checkSubscribe()
