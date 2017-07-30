from flask_login import UserMixin
from sqlalchemy import *
from werkzeug.security import generate_password_hash

from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    username = db.Column('username', db.Text(15), unique=True, primary_key=True)
    email = db.Column('email', db.Text(50), unique=True)
    password = db.Column('password', db.Text(80))
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password, authenticated):
        self.username = username
        self.email = email
        self.password = password
        self.authenticated = authenticated

    '''Used for checking account activation TO-DO later'''

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


def create_new_user(form):
    hashed_password = generate_password_hash(form.password.data, method='sha256')
    new_user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password,
                    authenticated=False)
    db.session.add(new_user)
    db.session.commit()
