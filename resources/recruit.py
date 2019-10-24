# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from utils import checkInfo
from database.database import database

class recruit(Resource):
    def post(self):
        data = request.get_json(force=True)
        check = database().isRecruit(data['tele'])
        if check['errcode']==401:
            result = checkInfo(data['name'], data['gender'], data['grade'],
                               data['college'], data['campus'], data['tele'], data['time'])
            if result['errcode']==0:
                #时间数组转字符串
                data['time']=','.join(data['time'])
                return database().updateUser(data)
            else:
                return result
        else:
            return check
        
