from wtforms import Form, StringField, PasswordField, validators, BooleanField, SubmitField
from flask_wtf import RecaptchaField


class ReigstrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.DataRequired()])
    password = PasswordField('New Password',
                             [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match'),
                              validators.Length(min=8, max=80)])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    # recaptcha = RecaptchaField('Captcha', [validators.DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(Form):
    username = StringField('Username', [validators.InputRequired(), validators.Length(min=4, max=25)])
    password = StringField('Password', [validators.InputRequired(), validators.Length(min=6, max=25)])
    recaptcha = RecaptchaField('Captcha', [validators.DataRequired()])
