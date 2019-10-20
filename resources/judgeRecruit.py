# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from utils import checkInfo
from database.database import database

class judgeRecruit(Resource):
    def post(self):
        data = request.get_json(force=True)
        return database().isRecruit(data['tele'])
        
