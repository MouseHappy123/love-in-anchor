from flask_restful import Resource
from flask import jsonify, request
from database.database import database

class colleges(Resource):
    def post(self):
        data = request.get_json(force=True)
        return database().showCollege(data['campus'])
        
