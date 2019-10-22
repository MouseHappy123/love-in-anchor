# encoding:utf-8
from sqlalchemy import Column, String, Integer, Text, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import cfg
from flask import jsonify
engine = create_engine("mysql+pymysql://"+cfg["username"]+":"+cfg["password"] +
                       "@"+cfg["host"]+"/"+cfg["database"]+"?charset=utf8mb4")
#建库
if not database_exists(engine.url):
    create_database(engine.url)
Base = declarative_base()


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    gender = Column(Integer, nullable=False)
    grade = Column(Text, nullable=False)
    college = Column(Text, nullable=False)
    campus = Column(Integer, nullable=False)
    tele = Column(String(11), nullable=False)
    time = Column(Text, nullable=False)

    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4"
    }


class school(Base):

    __tablename__ = 'school'

    id = Column(Integer, primary_key=True, autoincrement=True)
    campus = Column(Text, nullable=True)
    college = Column(Text, nullable=True)

    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4"
    }


Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session=DBSession()
data = []
data.append(school(id=1, campus=0, college='材料科学与工程学院'))
data.append(school(id=2, campus=0, college='化学与化工学院'))
data.append(school(id=3, campus=0, college='轻工科学与工程学院'))
data.append(school(id=4, campus=0, college='食品科学与工程学院'))
data.append(school(id=5, campus=0, college='数学学院'))
data.append(school(id=6, campus=0, college='物理与光电学院'))
data.append(school(id=7, campus=0, college='经济与贸易学院'))
data.append(school(id=8, campus=0, college='计算机科学与工程学院'))
data.append(school(id=9, campus=0, college='生物科学与工程学院'))
data.append(school(id=10, campus=0, college='环境与能源学院'))
data.append(school(id=11, campus=0, college='软件学院'))
data.append(school(id=12, campus=0, college='工商管理学院(非体尖)'))
data.append(school(id=13, campus=0, college='公共管理学院'))
data.append(school(id=14, campus=0, college='马克思主义学院'))
data.append(school(id=15, campus=0, college='外国语学院'))
data.append(school(id=16, campus=0, college='法学院'))
data.append(school(id=17, campus=0, college='新闻与传播学院'))
data.append(school(id=18, campus=0, college='艺术学院'))
data.append(school(id=19, campus=0, college='设计学院'))
data.append(school(id=20, campus=0, college='医学院'))
data.append(school(id=21, campus=0, college='国际教育学院'))
data.append(school(id=22, campus=1, college='体育学院'))
data.append(school(id=23, campus=1, college='建筑学院'))
data.append(school(id=24, campus=1, college='工商管理学院(体尖)'))
data.append(school(id=25, campus=2, college='机械与汽车工程学院'))
data.append(school(id=26, campus=2, college='土木与交通学院'))
data.append(school(id=27, campus=2, college='电力学院'))
data.append(school(id=28, campus=2, college='电子与信息学院'))
data.append(school(id=29, campus=2, college='自动化科学与工程学院'))
data.append(school(id=30, campus=2, college='微电子学院'))
data.append(school(id=31, campus=2, college='生物医学科学与工程学院'))
data.append(school(id=32, campus=2, college='分子科学与工程学院'))
data.append(school(id=33, campus=2, college='吴贤能智能工程学院'))
for i in range(33):
    session.add(data[i])
session.commit()
session.close()
