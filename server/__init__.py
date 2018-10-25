from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin



service = Flask(__name__)
#restfull
api = Api(service)

#database
service.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://restureese:@localhost/sertifikasi'
service.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
service.config['SECRET_KEY'] = 'You Will Never Learn'

# set optional bootswatch theme
service.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(service, name='microservice', template_mode='bootstrap3')



db = SQLAlchemy(service)

from server import routes
from server import models
from server import views
