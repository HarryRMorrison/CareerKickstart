from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from app.models import User
from app.forms import LoginForm, SignupForm 
from app.controller import PostController

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
    question_demo = {}
    return render_template('card.html', question=question_demo)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def load_createpage():
    return PostController.create_post()

@app.route('/login', methods=['GET','POST'])
def load_login():
    return render_template('login.html')  

@app.route('/signup', methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return jsonify({"error": "This username or email already exists."}), 400
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "You have been registered."}), 201
    return jsonify({"error": "Invalid form data."}), 400

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username_email = form.username_email.data
        password = form.password.data
        user = User.query.filter((User.username == username_email) | (User.email == username_email)).first()
        if user and user.check_password(password):
            return jsonify({"message": "Logged in."}), 200
    return jsonify({"error": "Entered credentials are invalid."}), 401

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)
