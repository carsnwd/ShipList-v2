from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import config

'''Flask'''
app = Flask(__name__)
app.config.from_object('config')

'''Database'''
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy()
db.init_app(app)

'''Models'''
from app import models

'''Views '''
from app import views

'''Flask-Login'''
login_manager = LoginManager()
login_manager.init_app(app)

'''Takes a unicode user id and returns the corresponding user object'''
@login_manager.user_loader
def load_user(user_id):
    return models.User.get(user_id)
