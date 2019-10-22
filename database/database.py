# encoding:utf-8
from sqlalchemy import Column, String, Integer, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import cfg
from flask import jsonify
engine = create_engine("mysql+pymysql://"+cfg["username"]+":"+cfg["password"] +
                       "@"+cfg["host"]+"/"+cfg["database"]+"?charset=utf8mb4")
Base = declarative_base()


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    gender=Column(Integer,nullable=False)
    grade = Column(Text, nullable=False)
    college = Column(Text, nullable=False)
    campus = Column(Integer, nullable=False)
    tele = Column(String(11), nullable=False)
    time= Column(Text,nullable=False)

    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4"
    }

class School(Base):

    __tablename__ = 'school'

    id = Column(Integer, primary_key=True, autoincrement=True)
    campus = Column(Text, nullable=True)
    college = Column(Text, nullable=True)

    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4"
    }


class database(object):
    def __init__(self):
        self.createSession=sessionmaker(bind=engine)
    #是否报名
    def isRecruit(self,tele):
        Session=self.createSession()
        try:
            query=(Session.query(User).filter(User.tele==tele).first())
        except Exception as e:
            return {
                "errcode":403,
                "errmsg":str(e)
            }
        Session.close()
        if not query:
            return {
                "errcode":401,
                "errmsg":"还未报名"
            }
        else:
            return {
                "errcode":402,
                "errmsg":{
                    "name":query.name,
                    "tele":query.tele
                }
            }

    #更新报名信息
    def updateUser(self,data):
        Session=self.createSession()
        Session.add(User(name=data['name'],gender=data['gender'],grade=data['grade'],college=data['college'],campus=data['campus'],tele=data['tele'],time=data['time']))
        try:
            Session.commit()
        except Exception as e:
            return jsonify({
                "errcode":403,
                "errmsg":str(e)
            })
        Session.close()
        return jsonify({
                "errcode":0,
                "errmsg":"success"
            })

    #显示学院
    def showCollege(self,campus):
        Session=self.createSession()
        try:
            query=(Session.query(School).filter(School.campus==campus).all())
        except Exception as e:
            return jsonify({
                "errcode":400,
                "errmsg":str(e)
            })
        Session.close()
        if not query:
            return jsonify({
                "errcode":401,
                "errmsg":"未查询到"
            })
        else:
            res=[]
            for i in query:
                res.append(i.college)
            return jsonify({
                "errcode":0,
                "errmsg":res
            })
    #内部查询
    def query(self):
        Session=self.createSession()
        try:
            query=(Session.query(User).all())
        except Exception as e:
            return jsonify({
                "errcode":400,
                "errmsg":str(e)
            })
        Session.close()
        if not query:
            return jsonify({
                "errcode":401,
                "errmsg":"未查询到"
            })
        else:
            res=[]
            for i in query:
                res.append({"name":i.name,"gender":i.gender,"grade":i.grade,"college":i.college,"campus":i.campus,"tele":i.tele,"time":i.time})
            return jsonify({
                "errcode":0,
                "datas":res
            })

