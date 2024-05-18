from flask import render_template, request, jsonify, redirect, url_for, session
from app import app, db
from app.models import User
from app.forms import LoginForm, SignupForm 
from flask_mysqldb import MySQL
import MySQLdb.cursors

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

@app.route("/display")
def display():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = % s',
                       (session['id'], ))
        account = cursor.fetchone()
        return render_template("profilePageDisplay.html", account=account)
    return redirect(url_for('login'))

@app.route("/update", methods=['GET', 'POST'])
def update():
    form = EditProfileForm(request.form)
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'about me' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            about_me = request.form['about me']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT * FROM accounts WHERE username = % s',
                      (username, ))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'name must contain only characters and numbers !'
            else:
                cursor.execute('UPDATE accounts SET username =% s,\
                password =% s, email =% s WHERE id =% s', (
                    username, password, email, (session['id'], ), ))
                mysql.connection.commit()
                msg = 'You have successfully updated !'
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template("profilePage.html", msg=msg)
    return redirect(url_for('login'))