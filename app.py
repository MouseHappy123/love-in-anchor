import flask
import flask_restful
from flask_cors import CORS
from config import cfg
from resources.checkTime import checkTime
from resources.recruit import recruit
from resources.judgeRecruit import judgeRecruit
from resources.colleges import colleges
from resources.innerQuery import innerQuery
from resources.checkLogin import checkWXLogin
from resources.checkSubscribe import checkWXSubscribe
from werkzeug.middleware.proxy_fix import ProxyFix

app=flask.Flask(__name__)
CORS(app,resources=r'/*',supports_credentials=True)
app.secret_key=cfg['secret_key']
api=flask_restful.Api(app)
api.add_resource(checkTime,'/checkTime')
api.add_resource(recruit,'/recruit')
api.add_resource(judgeRecruit,'/judgeRecruit')
api.add_resource(colleges,'/colleges')
api.add_resource(innerQuery,'/innerQuery')
api.add_resource(checkWXLogin,'/checkLogin')
api.add_resource(checkWXSubscribe,'/checkSubscribe')

if __name__=='__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(port=8001)