from flask_restful import Resource
from flask import jsonify, request
from utils import checkInfo
from database.database import database

class recruit(Resource):
    def post(self):
        data = request.get_json(force=True)
        result = checkInfo(data['name'], data['gender'], data['grade'],
                           data['college'], data['campus'], data['tele'], data['time'])
        if result['errcode']==0:
            return database().updateUser(data)
        else:
            return result
        
