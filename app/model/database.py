from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()

def setup_db(app: Flask):
    host = config['mysql']['host']
    port = config['mysql']['port']
    database = config['mysql']['db']
    user = config['mysql']['user']
    password = config['mysql']['pass']
    dburl = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)

    app.config['SQLALCHEMY_DATABASE_URI'] = dburl
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
