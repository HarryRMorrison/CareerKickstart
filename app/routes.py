from flask import render_template
from app import app

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