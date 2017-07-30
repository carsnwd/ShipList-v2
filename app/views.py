from app import app, forms, db
from werkzeug.security import check_password_hash
from flask import render_template, request, flash
from flask_login import login_user, logout_user

from app.models import create_new_user, User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        user = User.query.filter_by(username=username).first()
        print("Checking User if it exists...")
        if user:
            print("User exists...checking password")
            if check_password_hash(user.password, login_form.password.data):
                print("Password correct, logging in.")
                login_user(user)
                return render_template('index.html')
            else:
                print("Password Incorrect")
        print("User doesn't exist")
        return render_template('login.html', form=login_form)
    print("Form validate " + str(login_form.validate()))
    return render_template('login.html', form=login_form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    registration_form = forms.ReigstrationForm(request.form)
    print(registration_form.validate())
    if request.method == 'POST' and registration_form.validate():
        print("Creating new user")
        create_new_user(registration_form)
        login_form = forms.ReigstrationForm(request.form)
        return render_template('login.html', form=login_form)
    return render_template('signup.html', form=registration_form)


@app.route('/post')
def post():
    return render_template('postlisting.html')


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
