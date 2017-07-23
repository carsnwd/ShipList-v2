from app import app, forms, db
from app import models
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, url_for, flash
import flask_login



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login_user(user)
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = forms.ReigstrationForm(request.form)
    print(form.validate())
    if request.method == 'POST' and form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = models.User(username=form.username.data, email=form.email.data, password=hashed_password, authenticated=False)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered')
        return render_template(url_for('/login'))
    return render_template('signup.html', form=form)


@app.route('/post')
def post():
    return render_template('postlisting.html')


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
