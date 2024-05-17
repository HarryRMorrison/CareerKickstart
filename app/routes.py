from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from app import app, db
from app.models import User, Answer
from app.forms import LoginForm, SignupForm, QuestionForm

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/getcard', methods = ['GET'])
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
            return jsonify({"message": "Logged in."}), 200
    return jsonify({"error": "Entered credentials are invalid."}), 401

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
    def to_dict(self):
        return {
            "ans_id": self.ans_id,
            "question_id": self.question_id,
            "user_id": self.user_id,
            "answer": self.answer,
            "date_created": self.date_created,
            "likes": self.likes
        }
Answer.to_dict = to_dict
