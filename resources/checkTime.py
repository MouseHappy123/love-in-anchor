# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify,abort
import time
from config import cfg
class checkTime(Resource):
    def get(self):
        format="%Y-%m-%d %H:%M:%S"
        begin=time.mktime(time.strptime(cfg['begin'],format))
        end=time.mktime(time.strptime(cfg['end'],format))
        now=time.time()
        #比较时间
        if now<begin:
            return jsonify({"errcode":400,"errmsg":"活动还没开始"})
        elif now>end:
            return jsonify({"errcode":401,"errmsg":"活动已结束"})
        else:
            return jsonify({"errcode":0})