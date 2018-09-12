from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'wufazhuce'


app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = '''{}+{}://{}:{}@{}:{}/{}?charset=utf8'''.format(
        DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
api = Api(app)


def register():
    from service.wufazhuce.urls import api
    api.init_app(app)


register()
