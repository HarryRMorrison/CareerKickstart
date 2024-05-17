from flask import render_template, request, jsonify, redirect, url_for, flash
from app import app, db
from app.models import User
from app.forms import LoginForm, SignupForm
from app.controller import PostController, UserController
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/explore', methods=['GET'])
def load_explorepage():
    arguments = request.args
    if len(arguments) > 0:
        if len(arguments) == 1 and arguments.get('query', '') == '':
            return PostController.get_top_questions()
        else:
            return PostController.get_searched_questions(arguments)
    else:
        return PostController.get_top_questions()

@app.route('/getcard', methods = ['GET'])
def send_card_template():
    return render_template('card.html', question={})

@app.route('/create', methods=['GET', 'POST'])
@login_required
def load_createpage():
    if not current_user.is_authenticated:
        flash("Login or Sign up to Post a Question")
        return redirect(url_for('login'))
    return PostController.create_post()

@app.route('/signup', methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        print('New User:', form.data)
        return UserController.register(form.data)
    print('failed to validate')
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    login = LoginForm()
    signup = SignupForm()
    if login.validate_on_submit():
        print('Logging in:', login.data)
        return UserController.login(login.data)
    return render_template('login.html', form1=login, form2=signup)

@app.route('/logout')
def logout():
    print("logout:"+current_user.get_id())
    logout_user()
    return redirect('/home')
