from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from app import app, db
from app.models import User, Question, Answer
from app.forms import LoginForm, SignupForm, QuestionForm
from app.controller import PostController

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/getcard', methods=['GET'])
def send_card_template():
    question_demo = {}
    return render_template('card.html', question=question_demo)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def load_createpage():
    if request.method == 'POST':
        return PostController.create_post()
    else:
        return render_template("create.html")

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
            login_user(user)
            return jsonify({"message": "Logged in."}), 200
    return jsonify({"error": "Entered credentials are invalid."}), 401

@app.route('/question/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = Question.query.get_or_404(question_id)
    answers = Answer.query.filter_by(question_id=question_id).order_by(Answer.date_created.desc()).all()

    question_data = {
        'title': question.title,
        'description': question.description,
        'user': {
            'username': question.user.username,
            'profile_photo': question.user.profile_photo if hasattr(question.user, 'profile_photo') else 'default_profile_photo.jpg',
        },
        'votes': question.likes,
        'answers': [{
            'answer': answer.answer,
            'user': {
                'username': answer.user.username,
                'profile_photo': answer.user.profile_photo if hasattr(answer.user, 'profile_photo') else 'default_profile_photo.jpg',
            }
        } for answer in answers]
    }
    if request.headers.get('Accept') == 'application/json':
        return jsonify(question_data)
    
    return render_template('requestPage.html', question=question, answers=answers, current_user=current_user)

@app.route('/answer', methods=['POST'])
@login_required
def create_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    answer_text = data.get('answer')
    if not question_id or not answer_text:
        return jsonify({"error": "Missing required fields."}), 400
    answer = Answer(
        question_id=question_id,
        user_id=current_user.user_id,
        answer=answer_text
    )
    db.session.add(answer)
    db.session.commit()
    return jsonify({"message": "Answer created successfully.", "answer": answer.to_dict()}), 201

@app.route('/explore')
def explore():
    return PostController.get_top_questions()

@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('q')
    return PostController.get_searched_questions(search_query)

@app.route('/nextset', methods=['GET'])
def next_set():
    page_num = request.args.get('page', 1, type=int)
    return PostController.get_next_question_set(page_num)

@app.route('/nextsearch', methods=['GET'])
def next_search():
    page_num = request.args.get('page', 1, type=int)
    arguments = request.args.to_dict()
    return PostController.get_next_searched_questions(arguments, page_num)
