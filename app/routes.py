from flask import render_template
from app import app
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/getcard', methods = ['GET'])
def send_card_template():
    question_demo = {}
    return render_template('card.html', question=question_demo)

@app.route('/explore')
def load_explorepage():
    posts = []
    return render_template("explorePage.html", posts=posts)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "This username or email already exists."}), 400
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "You have been registered."}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username_email = data.get('username_email')
    password = data.get('password')
    user = User.query.filter((User.username == username_email) | (User.email == username_email)).first()
    if user and user.check_password(password):
        return jsonify({"message": "Logged in."}), 200
    return jsonify({"error": "Entered credentials are invalid."}), 401