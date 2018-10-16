from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy



service = Flask(__name__)
#restfull
api = Api(service)

#database
service.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://restureese:@localhost/sertifikasi'
service.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(service)

from server import routes
from server import models
