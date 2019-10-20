# encoding:utf-8
from config import cfg
from flask import jsonify
import re

telPattern = "^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$"
namePattern = u"^[\u4e00-\u9fa5]{2,8}$"

result = ["名字不能为空", "性别不能为空", "年级不能为空", "学院不能为空", "校区不能为空", "号码不能为空", "未选择时间"]

# 检查姓名及手机号格式


def checkFormat(option, pattern):
    pattern = re.compile(pattern)
    return bool(re.match(pattern, option))

# 检查报名信息


def checkInfo(name, gender, grade, college, campus, tele, time):
    infoList = [name, gender, grade, college, campus, tele, time]
    for i in infoList:
        if not i and i != 0:
            return {
                "errcode": 400,
                "errmsg": result[infoList.index(i)]
            }
    if not checkFormat(name, namePattern):
        return {
            "errcode": 401,
            "errmsg": "名字不规范"
        }
    if not checkFormat(tele, telPattern):
        return {
            "errcode": 402,
            "errmsg": "号码不规范"
        }
    return {
        "errcode": 0
    }
