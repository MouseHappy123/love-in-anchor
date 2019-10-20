# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from database.database import database

class innerQuery(Resource):
    def post(self):
        data = request.get_json(force=True)
        if(data['password']=="123456"and data['username']=="BBT"):
            return database().query()
        else:
         return jsonify({
            "errcode":400,
            "errmsg":"用户名或密码错误"
        })
