from flask_login import UserMixin
from sqlalchemy import *
from app import db



class User(UserMixin, db.Model):

    __tablename__ = 'users'

    username = db.Column('username', db.Text(15), unique=True, primary_key=True)
    email = db.Column('email', db.Text(50), unique=True)
    password = db.Column('password', db.Text(80))
    authenticated = db.Column(db.Boolean, default=False)

    '''Used for checking account activation TO-DO later'''
    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False