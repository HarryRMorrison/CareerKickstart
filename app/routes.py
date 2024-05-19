from flask import render_template, request, jsonify, redirect, url_for, flash
from app import db
from app.blueprints import main
from app.models import User, Question, Answer
from app.forms import LoginForm, SignupForm, AnswerForm, EditProfileForm
from app.controller import PostController, UserController
from flask_login import current_user, login_user, logout_user, login_required

# Routes are used to map URLs to specific functions in your application
# Allowing the server to handle requests to different endpoints and execute the corresponding logic to return responses to the client.
# Routes are mapped to Blueprint main to allow for multiple config options

# Home route
@main.route('/')
@main.route('/home')
def index():
    return render_template('home.html')

# Explore page route searched and standard
@main.route('/explore', methods=['GET'])
def load_explorepage():
    arguments = request.args
    if len(arguments) > 0:
        if len(arguments) == 1 and arguments.get('query', '') == '':
            return PostController.get_top_questions()
        else:
            return PostController.get_searched_questions(arguments)
    else:
        return PostController.get_top_questions()

# Get card route for format retrieval
@main.route('/getcard', methods = ['GET'])
def send_card_template():
    return render_template('card.html', question={})

# Creates a new answer
@main.route('/newanswer/<int:qid>/', methods = ['POST'])
def make_new_answer(qid):
    if not current_user.is_authenticated:
        flash("Login or Sign up to Answer a Question")
        return redirect(url_for('main.login'))
    form = AnswerForm(request.form)
    if form.validate_on_submit():
        print('New Answer:', form.data)
        return PostController.create_answer(qid,form.data)
    return jsonify({"error":"An error occurred"}), 500
    
# Displays question
@main.route('/question/<int:question_id>', methods=['GET'])
def load_postpage(question_id):
    return PostController.get_post_page(question_id)

# Create a new question page load or form retrieval
# Used in both pop up and page
@main.route('/create', methods=['GET', 'POST'])
@login_required
def load_createpage():
    if not current_user.is_authenticated:
        flash("Login or Sign up to Post a Question")
        return redirect(url_for('main.login'))
    return PostController.create_post()

# Sign up form route
@main.route('/signup', methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        print('New User:', form.data)
        return UserController.register(form.data)
    print('failed to validate')
    return redirect(url_for('main.login'))

# Login page
@main.route('/login', methods=['POST', 'GET'])
def login():
    login = LoginForm()
    signup = SignupForm()
    if login.validate_on_submit():
        print('Logging in:', login.data)
        return UserController.login(login.data)
    return render_template('login.html', form1=login, form2=signup)

# Logout route
@main.route('/logout')
def logout():
    print("logout:"+current_user.get_id())
    logout_user()
    flash("Logout Successful")
    return redirect('/home')

# Profile page route
@main.route('/profilepage/<Username>', methods=['GET', 'POST'])
@login_required
def load_profile_page(Username):
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    return UserController.edit_profile(Username)

# For currentpfp on navbar
@main.route('/currentpfp', methods=['GET'])
@login_required
def current_user_profile_page():
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    return redirect('/profilepage/'+User.query.get(current_user.get_id()).username)

# Search feature for page
@main.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('q')
    return PostController.get_searched_questions(search_query)

# Next set route for mapping questions
@main.route('/nextset', methods=['GET'])
def next_set():
    page_num = request.args.get('page', 1, type=int)
    return PostController.get_next_question_set(page_num)

# Next search route for pagination and questions that user has requested
@main.route('/nextsearch', methods=['GET'])
def next_search():
    page_num = request.args.get('page', 1, type=int)
    arguments = request.args.to_dict()
    return PostController.get_next_searched_questions(arguments, page_num)
