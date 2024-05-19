from flask import render_template, request, jsonify, redirect, url_for, flash
from app import db
from app.blueprints import main
from app.models import User, Question, Answer
from app.forms import LoginForm, SignupForm, AnswerForm, EditProfileForm
from app.controller import PostController, UserController
from flask_login import current_user, login_user, logout_user, login_required

@main.route('/')
@main.route('/home')
def index():
    return render_template('home.html')

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

@main.route('/getcard', methods = ['GET'])
def send_card_template():
    return render_template('card.html', question={})

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
    

@main.route('/question/<int:question_id>', methods=['GET'])
def load_postpage(question_id):
    return PostController.get_post_page(question_id)

@main.route('/create', methods=['GET', 'POST'])
@login_required
def load_createpage():
    if not current_user.is_authenticated:
        flash("Login or Sign up to Post a Question")
        return redirect(url_for('main.login'))
    return PostController.create_post()

@main.route('/signup', methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        print('New User:', form.data)
        return UserController.register(form.data)
    print('failed to validate')
    return redirect(url_for('main.login'))

@main.route('/login', methods=['POST', 'GET'])
def login():
    login = LoginForm()
    signup = SignupForm()
    if login.validate_on_submit():
        print('Logging in:', login.data)
        return UserController.login(login.data)
    return render_template('login.html', form1=login, form2=signup)

@main.route('/logout')
def logout():
    print("logout:"+current_user.get_id())
    logout_user()
    flash("Logout Successful")
    return redirect('/home')

@main.route('/profilepage/<Username>', methods=['GET', 'POST'])
@login_required
def load_profile_page(Username):
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    return UserController.edit_profile(Username)

@main.route('/currentpfp', methods=['GET'])
@login_required
def current_user_profile_page():
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    return redirect('/profilepage/'+User.query.get(current_user.get_id()).username)

@main.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('q')
    return PostController.get_searched_questions(search_query)

@main.route('/nextset', methods=['GET'])
def next_set():
    page_num = request.args.get('page', 1, type=int)
    return PostController.get_next_question_set(page_num)

@main.route('/nextsearch', methods=['GET'])
def next_search():
    page_num = request.args.get('page', 1, type=int)
    arguments = request.args.to_dict()
    return PostController.get_next_searched_questions(arguments, page_num)
  
@main.route("/display")
def display():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = % s',
                       (session['id'], ))
        account = cursor.fetchone()
        return render_template("profilePageDisplay.html", account=account)
    return redirect(url_for('login'))
