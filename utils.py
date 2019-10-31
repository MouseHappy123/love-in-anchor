# encoding:utf-8
from config import cfg
from flask import jsonify,session,request
import re
import requests
import json
import time

telPattern = "^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$"
namePattern = u"^[\u4e00-\u9fa5]{2,8}$"

result = ["名字不能为空", "性别不能为空", "年级不能为空", "学院不能为空", "校区不能为空", "号码不能为空", "未选择时间"]
resultType = ["name", "gender", "grade", "college", "campus", "tele", "time"]

# 检查姓名及手机号格式
def checkFormat(option, pattern):
    pattern = re.compile(pattern)
    return bool(re.match(pattern, option))

# 检查报名信息
def checkInfo(name, gender, grade, college, campus, tele, time):
    infoList = [name, gender, grade, college, campus, tele, time]
    Type = []
    msg = []
    for i, val in enumerate(infoList):
        if i == 0 and val:
            if not checkFormat(name, namePattern):
                Type.append(resultType[i])
                msg.append("名字不规范")
        if i == 5 and val:
            if not checkFormat(tele, telPattern):
                Type.append(resultType[i])
                msg.append("号码不规范")
        if not val and val != 0:
            Type.append(resultType[i])
            msg.append(result[i])
    if len(Type) > 0 and len(msg) > 0:
        return {
            "errcode": 400,
            "errmsg": {
                "type": Type,
                "msg": msg
            }
        }
    return {
        "errcode": 0
    }

#检查是否授权微信登录
def checkLogin():
    if "open_id" not in session:
        sess_id = request.cookies.get("PHPSESSID")
        if sess_id is not None:
            r = requests.get("https://hemc.100steps.net/2017/wechat/Home/Index/getUserInfo", timeout=5,
                             cookies=dict(PHPSESSID=sess_id))
            try:
                t = json.loads(r.text)
                if "openid" in t:
                    session["open_id"] = t["openid"]
            except:
                pass
    if "open_id" not in session:
        return {
            "errcode":400, 
            "errmsg":"未授权登录"
        }
    return {
            "errcode":0, 
            # "errmsg":session['open_id']
    }

# 判断用户是否关注公众号
def checkSubscribe():
    if "open_id" in session:
        sess_id = request.cookies.get("PHPSESSID")
        response = requests.get('https://hemc.100steps.net/2017/wechat/Home/Index/getSubscribe?state=https://hemc.100steps.net/2017/wechat/Home/Index/getSubscribe',
                                timeout=5,cookies=dict(PHPSESSID=sess_id)).text
        try:
            t=json.loads(response)
            if "subscribe" in t:
                session['check_sub'] = t['subscribe']
        except:
            pass
        if not session['check_sub']:
            return {
                "errcode":401, 
                "errmsg":"未关注"
            }
        else:
            return {
                "errcode":0,
                "errmsg":"已关注"
            }
    else:
        return {
            "errcode":400, 
            "errmsg":"未授权登录"
        }

#判断时间
def checkTime():
    format="%Y-%m-%d %H:%M:%S"
    begin=time.mktime(time.strptime(cfg['begin'],format))
    end=time.mktime(time.strptime(cfg['end'],format))
    now=time.time()
    #比较时间
    if now<begin:
        return {"errcode":400,"errmsg":"活动还没开始"}
    elif now>end:
        return {"errcode":401,"errmsg":"活动已结束"}
    else:
        return {"errcode":0}